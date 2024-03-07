from flask import Blueprint

from .recommend import get_user_recommendations as get_user_recommendations_route,get_popular_recommendations as get_popular_recommendations_toute


# 创建蓝图对象
recommender_bp = Blueprint("recommender_bp", __name__)

recommender_bp.add_url_rule('/user', view_func=get_user_recommendations_route, methods=['GET']) 
recommender_bp.add_url_rule('/popular', view_func=get_popular_recommendations_toute, methods=['GET']) 