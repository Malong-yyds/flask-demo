# coding:utf-8
# demodemo\ihome\__init__.py
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from extension import db

def create_app():
    
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    # 初始化 JWTManager  
    jwt = JWTManager(app)  
    app.config['SQLALCHEMY_REFLECT'] = True  # 启用表反射  
    # 使用app初始化db
    db.init_app(app)

    # 注册蓝图
    from app.api import user,attraction,review
    app.register_blueprint(user.user_bp, url_prefix="/api/user")
    app.register_blueprint(attraction.attaction_bp, url_prefix="/api/attraction")
    app.register_blueprint(review.review_bp, url_prefix="/api/review")

      
    return app
