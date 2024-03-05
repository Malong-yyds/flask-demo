from flask import Blueprint


# 创建蓝图对象
review_bp = Blueprint("review_bp", __name__)

# 导入并注册其他模块中的路由（如果需要）  
from .reviews import add_like_count as add_like_count_route,post_review as post_review_route,reviews_attraction as reviews_attraction_route 

review_bp.add_url_rule('/like', view_func=add_like_count_route, methods=['POST']) 
review_bp.add_url_rule('/add', view_func=post_review_route, methods=['POST']) 
review_bp.add_url_rule('/detail', view_func=reviews_attraction_route, methods=['GET']) 