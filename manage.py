# coding:utf-8
# demodemo\manage.py

from app import create_app

# 创建flask的应用对象
app = create_app()


if __name__ == '__main__':
    app.run()

