from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import desc
from ..attraction.attractionModel import Attraction
from .UserAttraction import UserAttraction  
from ..review.reviewModel import Review
from scipy.sparse import csr_matrix  
  
def collaborative_filtering_recommendations(user_id, user_preferences, num_recommendations):  
    """  
    使用基于用户的协同过滤算法生成推荐。  
    """  
    # 1. 获取所有用户的偏好  
    all_preferences = UserAttraction.query.all()  
  
    # 2. 构建用户-景点偏好矩阵  
    user_item_matrix = build_user_item_matrix(all_preferences)  
  
    # 3. 计算用户相似度矩阵  
    user_similarity_matrix = cosine_similarity(user_item_matrix)  
  
    # 4. 为给定用户生成推荐  
    return generate_recommendations_for_user(user_id, user_similarity_matrix, user_item_matrix, num_recommendations)  
  
def build_user_item_matrix(preferences):  
    """  
    构建用户-景点偏好矩阵。  
    """  
    # 初始化矩阵  
    num_users = len(set(p.userId for p in preferences))  
    num_attractions = len(set(p.attractionId for p in preferences))  
    user_item_matrix = csr_matrix((num_users, num_attractions), dtype=float)  
  
    # 填充矩阵  
    for preference in preferences:  
        user_index = preference.userId - 1  # 假设用户ID从1开始，转换为0索引  
        attraction_index = preference.attractionId - 1  # 假设景点ID从1开始，转换为0索引  
        user_item_matrix[user_index, attraction_index] = 1.0  # 用户对景点有偏好，设置为1.0  
  
    return user_item_matrix  
  
 

def generate_recommendations_for_user(user_id, user_similarity_matrix, user_item_matrix, num_recommendations):  
    """  
    为给定用户生成推荐列表。  
    """  
    # 获取相似用户  
    similar_users = user_similarity_matrix[user_id - 1].argsort()[::-1][1:num_recommendations + 1]  # 排除自己  
      
    # 初始化推荐字典  
    recommendations = {}  
      
    # 遍历所有景点，计算加权评分  
    for attraction_index in range(user_item_matrix.shape[1]):  
        weighted_rating = 0  
        similarity_sum = 0  
        for similar_user_index in similar_users:  
            if user_item_matrix[similar_user_index, attraction_index] > 0:  
                similarity = user_similarity_matrix[user_id - 1, similar_user_index]  
                weighted_rating += similarity * user_item_matrix[similar_user_index, attraction_index]  
                similarity_sum += similarity  
          
        # 如果至少有一个相似用户对该景点有偏好，则计算加权评分并添加到推荐列表中  
        if similarity_sum > 0:  
            recommendations[attraction_index + 1] = weighted_rating / similarity_sum  # 加1是因为ID从1开始  
      
    # 根据加权评分对推荐列表进行排序并取前num_recommendations个  
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:num_recommendations]  
    # print(sorted_recommendations) 
    # 提取推荐景点的ID  
    return [rec[0] for rec in sorted_recommendations]  
  
def get_user_preferences(user_id):  
    """  
    从数据库中获取指定用户的偏好列表。  
    """  
    return UserAttraction.query.filter_by(userId=user_id).all()  
  
# 在实际应用中，你可能还需要一个函数来将景点ID转换为具体的景点对象，以便在返回推荐结果时提供更有用的信息。  
def get_attraction_by_id(attraction_id):  
    """  
    根据景点ID获取景点对象。  
    """  
    return Attraction.query.get(attraction_id)  
  
@jwt_required()
def get_user_recommendations(): 
    user_id=request.args.get('userId',type=int) 
    user_preferences = get_user_preferences(user_id) 
    # 如果用户没有偏好，则返回空推荐列表  
    if not user_preferences:  
        return []   
    num_recommendations = 3  # 或者从请求参数中获取  
    recommendations = collaborative_filtering_recommendations(user_id, user_preferences, num_recommendations)  
    data=[get_attraction_by_id(rec).to_dict() for rec in recommendations]
  
    return jsonify({'code': 200, 'data': data, 'message': 'success'})



  
def get_popular_recommendations():  
    # 查询所有景点，并按照average_score降序排列，取前5名  
    attractions = Attraction.query.with_entities(  
        Attraction.attraction_id,  
        Attraction.name,  
        Attraction.image_link,  
        # Attraction.address,  
        # Attraction.average_score,  
        # Attraction.review_count  
    ).order_by(desc(Attraction.average_score)).limit(5).all()  
  
    # 将查询结果转换为字典列表  
    attractions_list = [attraction._asdict() for attraction in attractions]  
  
    return jsonify({'code': 200, 'data': attractions_list, 'message': 'success'})
