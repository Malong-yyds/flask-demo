from flask import jsonify, request

from ..attraction.attractionModel import Attraction

from .TagModel import Tag


def get_attractions_by_tag():  
    tag_value=request.args.get('groupId',type=int)
    # 使用join将Tag和Attraction表连接在一起，并通过tag值进行过滤  
    attractions = Attraction.query.join(Tag, Attraction.attraction_id == Tag.attId).filter(Tag.tag == tag_value).all()  

    # 将查询结果转换为字典列表  
    attraction_list = [attr.to_dict() for attr in attractions] 
      
    return jsonify({'code': 200, 'data': attraction_list, 'message': 'success'})