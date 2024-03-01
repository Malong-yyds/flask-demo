from extension import db

class Attraction(db.Model):  
    __tablename__ = 'attraction'  
    attraction_id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(80), nullable=False)  
    detail_page_link = db.Column(db.String(255))  
    image_link = db.Column(db.String(255))  
    address = db.Column(db.String(120))  
    average_score = db.Column(db.Float)  
    review_count = db.Column(db.Integer)  
    flag = db.Column(db.Integer, nullable=False)  # 假设flag是非空的整数  