from extension import db

class Attraction(db.Model):  
    __tablename__ = 'attraction'  
    attraction_id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(80), nullable=False)  
    # detail_page_link = db.Column(db.String(512))  
    image_link = db.Column(db.String(512))  
    address = db.Column(db.String(120))  
    average_score = db.Column(db.Float)  
    review_count = db.Column(db.Integer) 
    opening_hours=db.Column(db.String(80)) 	
    official_phone	=db.Column(db.String(45)) 
    description	=db.Column(db.Text) 
    tips=db.Column(db.String(512)) 
    flag = db.Column(db.String(2))  # 假设flag是非空的整数 
    city = db.Column(db.String(4))
    def to_dict(self):  
        return {  
            'id': self.attraction_id,  
            'name': self.name,
            'image_link':self.image_link
            # 'description': self.description,  
            # 添加其他需要序列化的属性  
        } 