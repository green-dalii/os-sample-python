# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from gevent import monkey
#from flask_sqlalchemy import SQLAlchemy

import database

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

application = Flask(__name__)
#数据库路径配置
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/database.db'
#数据库对象改动信号
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#数据库请求结束自动提交变动
application.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#db = SQLAlchemy(application)

# """数据库模型定义"""
# #用户表
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     user = db.Column(db.String(64), unique=False, nullable=False, index=True)
#     nickName = db.Column(db.String(64), unique=False, nullable=False, index=True)
#     permission = db.Column(db.Integer,nullable=False)
#     bill1 = db.relationship('Bill1',backref='user',lazy='dynamic')
        
# #账单表
# class Bill1(db.Model):
#     """define bill data model"""
#     __tablename__ = 'bill1'
#     id = db.Column(db.Integer, primary_key=True)
#     customerName = db.Column(db.Unicode(64), unique=False, nullable=False, index=True)#客户名
#     date = db.Column(db.DateTime(),unique=False, nullable=False, index=True)#日期时间
#     item = db.Column(db.Unicode(64),unique=False,nullable=False,index=True)#类别
#     perPrice = db.Column(db.Float(),unique=False,nullable=False,index=False)#单价
#     quantity = db.Column(db.Float(),unique=False,nullable=False,index=False)#数量
#     totalPrice = db.Column(db.Float(),unique=False,nullable=False,index=False)#总价
#     payed = db.Column(db.Boolean(),unique=False,nullable=False,index=False)#支付状态
#     checkUser_id = db.Column(db.Integer,db.ForeignKey('user.id'))

db,User,Bill1 = database.init_db(application)

#创建数据库
db.create_all()
print('--------------database Added-----------------\h')

"""----------------------------------测试数据库-----------------------------------"""
#创建初始用户
admin_user = User(user=u'黄川川',nickName='Greener-Dalii',permission=0)
db.session.add(admin_user)
db.session.commit()
print('---------------added user to database-----------------\h')

@application.route("/")
def hello():
    return render_template('index.html')

@application.route("/wxapp/check")
def wxapp():
    return '已连接至鑫诚云'

@application.route("/wxapp/testdb/<nickName>")
def testdb(nickName):
    a=User.query.filter_by(nickName=nickName).all()
    if a == []:
        print('*************None**************')
        return 'No!!!!!!!!!!',403
    else:
        print('############Yes##########',a.user)
        return 'Yes!!!!!!!!!!'

@application.route("/wxapp/upload",methods=['POST'])
def upload():
    print('****------*****',request.get_json(force=True))
    return 'Got It!!!'

@application.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    application.run()
