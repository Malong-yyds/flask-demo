from extension import db

class Tag(db.Model):  
    __tablename__ = 'tags'  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    tag = db.Column(db.Integer, nullable=False)  
    attId = db.Column(db.Integer, db.ForeignKey('attraction.attraction_id'), nullable=False)  # 外键关联景点表  
 
    
  
    # 可以添加其他方法或属性  
    def __repr__(self):  
        return f"<UserAttraction {self.id}: User {self.userId} rated Attraction {self.attractionId} with {self.rating}>"
