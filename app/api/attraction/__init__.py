from flask import Blueprint


# 创建蓝图对象
attaction_bp = Blueprint("attaction_bp", __name__)

# 导入并注册其他模块中的路由（如果需要）  
from .attractionList import get_attractions_list as get_attractions_list_route 
attaction_bp.add_url_rule('/list', view_func=get_attractions_list_route, methods=['GET']) 
# attaction_bp.add_url_rule('/register', view_func=register_route, methods=['POST']) 