from flask import Blueprint

from app.api.group.tags import get_attractions_by_tag as get_attractions_by_tag_route

# 创建蓝图对象
group_bp = Blueprint("group_bp", __name__)

group_bp.add_url_rule('', view_func=get_attractions_by_tag_route, methods=['GET']) 