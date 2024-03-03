# @app.route('/attractions', methods=['GET'])  
from flask import jsonify, request

from ..review.reviewModel import Review

from .attractionModel import Attraction


def get_attractions_list():  
    keyword = request.args.get('q') 
    
    if keyword  in ['1', '2', '3', '4']:  
        # 查询所有需要的字段  
        attractions = Attraction.query.with_entities(  
            Attraction.attraction_id,  
            Attraction.name,  
            Attraction.image_link,  
            Attraction.address,  
            Attraction.average_score,  
            Attraction.review_count  
        ).filter_by(flag=keyword).all()

    else:  
    # 根据关键词进行模糊查询 
        attractions = Attraction.query.with_entities(  
            Attraction.attraction_id,  
            Attraction.name,    
            Attraction.image_link,  
            Attraction.address,  
            Attraction.average_score,  
            Attraction.review_count  
        ).filter(Attraction.name.like(f"%{keyword}%")).all() 

    # 将查询结果转换为字典列表  
    attractions_list = [attraction._asdict() for attraction in attractions]  
  
    return jsonify({'code':200,'data':attractions_list,'message':'success'})


# 详情
def detail_attraction():
    id=request.args.get('attId',type=int)
    # 查询景点详情  
    attraction = Attraction.query.get(id)  
    reviews = Review.query.filter_by(attraction_id=id).all()
    reviews_list = [  
            {  
                'review_id': review.review_id,  
                'comment_content': review.comment_content,  
                'rating': review.rating,  
                'time_posted': review.time_posted.strftime('%Y-%m-%d'),  
                'like_count': review.like_count,  
                'username': review.user.username,  # 通过关系获取用户名  
            }  
            for review in reviews  
        ]
    # 组合景点信息和评价列表  
    detail_data = {  
                'attraction_id': attraction.attraction_id,  
                'name': attraction.name,  
                'image_link': attraction.image_link,  
                'address': attraction.address,  
                'average_score': attraction.average_score,  
                'review_count': attraction.review_count,  
                'opening_hours': attraction.opening_hours,  
                'official_phone': attraction.official_phone,  
                'description': attraction.description,  
                'tips': attraction.tips,  
                'reviews': reviews_list  
            }  
   
    return jsonify({'code': 200, 'data': detail_data, 'message': 'success'})