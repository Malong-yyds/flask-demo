# config.py
# demodemo\config.py  
class Config:  
    MYSQL_HOST = 'localhost'  
    MYSQL_USER = 'root'  
    MYSQL_PASSWORD = 'root'  
    MYSQL_DATABASE = 'back'  
    MYSQL_FLAVOR = 'mysql+pymysql'  
    SQLALCHEMY_DATABASE_URI = f"{MYSQL_FLAVOR}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY ='my-secret-key'
    JWT_TOKEN_LOCATION='headers'
    JWT_HEADER_NAME='Authorization'
    JWT_HEADER_TYPE='Bearer'