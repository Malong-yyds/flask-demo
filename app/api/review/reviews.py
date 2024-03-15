# app\api\review\reviews.py
from datetime import datetime
from flask import jsonify, request  
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename  
from .reviewModel import Review
from extension import db
import os

@jwt_required()
def reviews_attraction():
    id=request.args.get('attId',type=int)
    page = request.args.get('page', 1,type=int)  
    per_page = request.args.get('pageSize', 5,type=int) 
    # 查询景点用户评价  
    # 使用 paginate 进行分页查询  
    reviews_pagination = Review.query.filter_by(attraction_id=id).order_by(Review.time_posted.desc()).paginate(page=page, per_page=per_page)  
  
    # 提取当前页的数据  
    reviews = reviews_pagination.items 
    
    reviews_list = [  
            {  
                'review_id': review.review_id,  
                'comment_content': review.comment_content,  
                'rating': review.rating,  
                'time_posted': review.time_posted.strftime('%Y-%m-%d'),  
                'like_count': review.like_count,  
                'username': review.user.username,  # 通过关系获取用户名  
                'image_paths':review.image_paths
            }  
            for review in reviews  
        ]
 
    total_pages = reviews_pagination.pages  
    total_items = reviews_pagination.total  
    return jsonify({'code': 200, 'data': {'reviews_list':reviews_list,'total':total_items}, 'message': 'success'})



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
    attId = request.form.get('attId')  
    userId = request.form.get('userId')  
    rating = request.form.get('rating')  
    content = request.form.get('content')  
    timePosed = datetime.now().date()  
    image_paths = []  
 
    # 获取所有以 'image_paths' 开头的文件 ，因为多文件image_paths[0],image_paths[1]
    images = [file for key, file in request.files.items() if key.startswith('image_paths')]   

    # 如果没有图片上传，则继续执行，不返回错误  
    if not images:  
        pass  
  
    # 检查上传的文件数量是否超过限制  
    elif len(images) > 3:  
        return jsonify({'code': 400, 'message': 'Maximum 3 images allowed'}), 400  
  
    # 遍历文件列表，保存文件并获取文件路径  
    for image in images:  
        # 检查文件是否有内容  
        if image.filename == '':  
            continue  
   
  # 检查文件类型  
        if image and image.filename.endswith(('.png', '.jpg', '.jpeg')):  
            # 生成安全的文件名  
            filename = os.path.join('app/static/', secure_filename(image.filename))  
            # 保存文件  
            image.save(filename)  
            # 将文件路径添加到列表中  
            image_paths.append(filename.replace('app/',''))  
        else:  
            # 如果文件不是有效的图片类型，返回错误  
            return jsonify({'code': 400, 'message': 'Invalid image file'}), 400   
    
    new_review=Review( 
        attraction_id=attId, 
        userId=userId, 
        rating=rating, 
        comment_content=content, 
        time_posted=timePosed, 
        like_count=0,
        # 如果没有图片，image_paths为None
        image_paths=','.join(image_paths) if image_paths else None   )
    
    db.session.add(new_review)  
    db.session.commit()  

    return jsonify({'code':200,'message':'success'})