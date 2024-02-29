# demodemo\ihome\api\model.py

from extension import db

from werkzeug.security import generate_password_hash, check_password_hash  
class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(80), unique=True, nullable=False)  
    password = db.Column(db.String(255), nullable=False)  # 通常密码会经过哈希处理  
  
    def __repr__(self):  
        return f"<User {self.username}>"
  
    def set_password(self, password):  
        self.password = generate_password_hash(password)  
  
    def check_password(self, password):  
        return check_password_hash(self.password, password)
     
     