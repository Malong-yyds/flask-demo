
from datetime import datetime
from flask import jsonify, request
from flask_jwt_extended import jwt_required

from .reviewModel import Review
from extension import db

@jwt_required()
def add_like_count():

    data=request.get_json(force=True) 
    id = data['reviewId']  
    review=Review.query.get_or_404(id)
    review.like_count +=1
    # 提交更改到数据库  
    db.session.commit() 

    return jsonify({'code':200,'message':'success'})



@jwt_required()
def post_review():
   
    data=request.get_json()
    attId=data.get('attId',None)
    userId=data.get('userId',None)
    rating=data.get('rating',None)
    content=data.get('content',None)
    timePosed=datetime.now().date()
    new_review=Review( attraction_id=attId, userId=userId, rating=rating, comment_content=content, time_posted=timePosed, like_count=0)
    
    db.session.add(new_review)  
    db.session.commit()  

    return jsonify({'code':200,'message':'success'})