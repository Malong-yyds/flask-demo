 
from datetime import datetime, timedelta
import jwt 


# 密钥，用于签名和验证JWT  
SECRET_KEY = 'my-secret-key' 


# 生成JWT  
def create_token(user_id: int, expires_in: int = 3600):  
    payload = {  
        'iss': 'http://example.org',  
        'iat': datetime.utcnow(),  
        'nbf': datetime.utcnow() + timedelta(seconds=10),  
        'exp': datetime.utcnow() + timedelta(seconds=expires_in),  
        'aud': 'http://example.com/resources',  
        'sub': user_id,  
        'jti': 'unique_jwt_id'  
    }  
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')  

