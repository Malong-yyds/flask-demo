# demodemo\ihome\api\de.py

from flask import  jsonify, request

from ..token import create_token  


from .userModel import User
from extension import db 




def authenticate_user(username, password):  
    # 从数据库中查询用户  
    user = User.query.filter_by(username=username).first()   
    
    # 检查用户是否存在，并且密码是否匹配  
    if user and user.check_password(password):  
        return user  
    else:  
        return None
      

# 注册接口  
# @app.route("/register", methods=['POST'])  
def register():  
    data = request.get_json()  
    username = data.get('username', None)  
    password = data.get('password', None)  
      
    # 验证数据的有效性  
    if not username or not password:  
        return jsonify({'error': 'Username and password are required'}), 400  
      
    # 检查用户名是否已存在  
    if User.query.filter_by(username=username).first():  
        return jsonify({'error': 'Username already exists'}), 400  
  
     # 在数据库中创建新用户，并加密密码  
    new_user = User(username=username)  
    new_user.set_password(password)   
    db.session.add(new_user)  
    db.session.commit()  
      
    # 创建访问令牌  
    # access_token = create_access_token(identity=new_user.id)  
      
    return jsonify({'code': 200, 'msg': 'User registered successfully', }), 200


# @api_bp.route("/login",methods=['POST'])
def login():
    # 从请求中获取用户名和密码  
    data = request.get_json()  
    username = data.get('username', None)  
    password = data.get('password', None)  
  
    # 验证用户  
    user = authenticate_user(username, password)  
  
    # 如果用户存在  
    if user:  
        # 假设user[0]是用户的ID  
        user_id = user.id  
        # 生成token  
        token = create_token(user_id)  
        return jsonify({'code':200,'msg':'success','data': {'token':token,'id':user_id}}), 200  
    else:  
        # 如果用户不存在或密码错误  
        return jsonify({'error': 'Invalid username or password'}), 401




