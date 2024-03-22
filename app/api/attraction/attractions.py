from flask import jsonify, request
from sqlalchemy import desc
from .attractionModel import Attraction, Food, Region


def get_attractions_list():  
    keyword = request.args.get('q')  
    page = request.args.get('page', 1,type=int)  
    per_page = request.args.get('pageSize', 5,type=int) 
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
        query = query.filter(Attraction.name.like(f"%{keyword}%"))     # 这里怎么改全文引擎搜索，提高效率

    # 添加分页  
    attractions = query.paginate(page=page, per_page=per_page).items  
    # attractions = query.all()  

    attractions_list = [attraction._asdict() for attraction in attractions]  
    total_count = query.count() 
    return jsonify({'code':200,'data':{'attractions_list':attractions_list,'total_count': total_count},'message':'success'})


# 详情
def detail_attraction():
    id=request.args.get('attId',type=int)
    # 查询景点详情  
    attraction = Attraction.query.get(id)  
   
    detail_data = {  
                'attraction_id': attraction.attraction_id,  
                'name': attraction.name,  
                'transport':attraction.transport,
                'video':attraction.video_link,
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

# 周围美食
def near_food():
     id=request.args.get('attId',type=int)
     food_results=Food.query.filter_by(attractionId=id).all()
     food_list=[
          {
                'foodId': food.foodId,  
                'name': food.name,  
                'img': food.img,  
                'label': food.label,  
                
          }
          for food in food_results
     ]

     return jsonify({'code': 200, 'data': food_list, 'message': 'success'})

# 周围景点
def near_attraction():
    attr_id = request.args.get('attId', type=int)  
    current_attraction = Attraction.query.get(attr_id)  
    if not current_attraction:  
        return jsonify({'code': 404, 'message': 'Attraction not found'}), 404  
    current_region = Region.query.filter_by(city=current_attraction.city).first().region  
    if not current_region:  
        return jsonify({'code': 500, 'message': 'Failed to determine region'}), 500  
    recommended_attractions = Attraction.query.filter(  
        Attraction.flag == current_attraction.flag,  
        Attraction.city == current_attraction.city,
        Attraction.attraction_id != attr_id  # 排除当前景点 
    ).order_by(desc(Attraction.average_score)).limit(4).all()   
    att_list = [attr.to_dict() for attr in recommended_attractions]  
    return jsonify({'code': 200, 'data': att_list, 'message': 'success'})  