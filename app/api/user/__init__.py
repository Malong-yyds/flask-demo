# coding:utf-8
# demodemo\ihome\api\__init__.py
from flask import Blueprint


# 创建蓝图对象
user_bp = Blueprint("user_bp", __name__)

# 导入并注册其他模块中的路由（如果需要）  
from .login_register import login as login_route ,register as register_route 
user_bp.add_url_rule('/login', view_func=login_route, methods=['POST']) 
user_bp.add_url_rule('/register', view_func=register_route, methods=['POST']) 


# from .dsdas.we  import hello
# user_bp.add_url_rule('/llo',view_func=hello)

