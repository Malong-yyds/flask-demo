# manage.py
from app import create_app

# 创建flask的应用对象
app = create_app()

# @app.after_request  
# def after_request(response):  
#     response.headers.add('Access-Control-Allow-Origin', '*')  
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')  
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')  
#     return response  

if __name__ == '__main__':
    app.run()

