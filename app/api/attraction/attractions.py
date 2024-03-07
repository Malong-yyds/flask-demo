from flask import jsonify, request
from .attractionModel import Attraction


def get_attractions_list():  
    keyword = request.args.get('q') 
    city_values=['gz','sz','fs','zh','zs','dg','hz','jm','qy','st','cz','sg','mz','jy','sw','hy','yf','zq','mm','zj','yj']
   
    query = Attraction.query.with_entities(  
            Attraction.attraction_id,  
            Attraction.name,  
            Attraction.image_link,  
            Attraction.address,  
            Attraction.average_score,  
            Attraction.review_count  
        )  
    if keyword in ['1', '2', '3']: 
        query = query.filter_by(flag=keyword)   
   
    elif keyword in city_values:
        query = query.filter_by(city=keyword)     

    else: 
        query = query.filter(Attraction.name.like(f"%{keyword}%"))  
       
    attractions = query.all()  
    # 将查询结果转换为字典列表  
    # attractions_list=[
    #     {
    #         'attraction_id': attraction.attraction_id,  
    #         'name': attraction.name,  
    #         'image_link': attraction.image_link,  
    #         'address': attraction.address,  
    #         'average_score': attraction.average_score,  
    #         'review_count': attraction.review_count  
    #     } 
    #     for attraction in attractions 
    # ]
    attractions_list = [attraction._asdict() for attraction in attractions]  
    return jsonify({'code':200,'data':attractions_list,'message':'success'})


# 详情
def detail_attraction():
    id=request.args.get('attId',type=int)
    # 查询景点详情  
    attraction = Attraction.query.get(id)  
   
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
            }  
   
    return jsonify({'code': 200, 'data': detail_data, 'message': 'success'})