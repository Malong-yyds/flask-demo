from extension import db

class Review(db.Model):  
    __tablename__ = 'review'  
    review_id = db.Column(db.Integer, primary_key=True)  
    attraction_id = db.Column(db.Integer, db.ForeignKey('attraction.attraction_id'), nullable=False)  
    userId =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    rating=db.Column(db.Integer)
    comment_content=db.Column(db.Text) 
    time_posted=db.Column(db.Date)
    like_count  =db.Column(db.Integer)
     # 添加关系字段  
    user = db.relationship("User", backref="review")