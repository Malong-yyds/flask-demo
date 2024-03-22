from flask import Blueprint


# 创建蓝图对象
attaction_bp = Blueprint("attaction_bp", __name__)

# 导入并注册其他模块中的路由（如果需要）  
from .attractions import get_attractions_list as get_attractions_list_route ,detail_attraction as detail_attraction_route, getFood as getFoodRoute
attaction_bp.add_url_rule('/search', view_func=get_attractions_list_route, methods=['GET']) 
attaction_bp.add_url_rule('/detail', view_func=detail_attraction_route, methods=['GET']) 
attaction_bp.add_url_rule('/detail/food', view_func=getFoodRoute, methods=['GET']) 