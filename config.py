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