# @app.route('/attractions', methods=['GET'])  
from flask import jsonify, request

from .attractionModel import Attraction

# from .attraction import Attraction


def get_attractions_list():  
    flag = request.args.get('flag', type=int, default=0) 
    print('dssdsdsdflag',flag) 
    if flag not in [1, 2, 3, 4]:  
        return jsonify({'error': 'Invalid flag value'}), 400  
      
    # 查询所有需要的字段  
    attractions = Attraction.query.with_entities(  
        Attraction.attraction_id,  
        Attraction.name,  
        Attraction.detail_page_link,  
        Attraction.image_link,  
        Attraction.address,  
        Attraction.average_score,  
        Attraction.review_count  
    ).filter_by(flag=flag).all()  
  
    # 将查询结果转换为字典列表  
    attractions_list = [attraction._asdict() for attraction in attractions]  
  
    return jsonify({'code':200,'data':attractions_list,'message':'success'})
