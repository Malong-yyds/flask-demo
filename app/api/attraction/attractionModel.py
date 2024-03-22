from extension import db

class Attraction(db.Model):  
    __tablename__ = 'attraction'  
    attraction_id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(80), nullable=False)  
    video_link = db.Column(db.String(512))  
    image_link = db.Column(db.String(512))  
    address = db.Column(db.String(120))
    transport = db.Column(db.String(255))  
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
    


class Food(db.Model):
    __tablename__ = 'food'
    foodId = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 自增主键  
    name=db.Column(db.String(45))
    img=db.Column(db.String(150))
    label=db.Column(db.String(45))
    attractionId=db.Column(db.Integer, db.ForeignKey('attraction.attraction_id'), nullable=False)  # 外键关联景点表