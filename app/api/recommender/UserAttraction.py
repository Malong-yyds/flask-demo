from extension import db

class UserAttraction(db.Model):  
    __tablename__ = 'user_attraction'  # 指定表名，如果不指定，默认为类名的小写形式  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 自增主键  
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 外键关联用户表  
    attractionId = db.Column(db.Integer, db.ForeignKey('attraction.attraction_id'), nullable=False)  # 外键关联景点表  
    rating = db.Column(db.Float, nullable=False)  # 评分字段  
   
    # 定义与用户表和景点表的关系  
    user = db.relationship('User', backref='attractions')  # 假设User是用户表的模型类  
    attraction = db.relationship('Attraction', backref='ratings')  # 假设Attraction是景点表的模型类  
  
    # 可以添加其他方法或属性  
    def __repr__(self):  
        return f"<UserAttraction {self.id}: User {self.userId} rated Attraction {self.attractionId} with {self.rating}>"
