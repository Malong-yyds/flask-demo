# coding:utf-8
# demodemo\ihome\__init__.py
from flask import Flask,jsonify
from config import Config
from extension import db

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    # 使用app初始化db
    db.init_app(app)

    # 注册蓝图
    from app.api import user
    app.register_blueprint(user.user_bp, url_prefix="/api/user")

      
    return app
