# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

def init_db(model):
    db = SQLAlchemy(model)

    """数据库模型定义"""
    #用户表
    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        user = db.Column(db.String(64), unique=True, nullable=False, index=True)
        nickName = db.Column(db.String(64), unique=False, nullable=False, index=True)
        permission = db.Column(db.Integer,nullable=False)
        bill1 = db.relationship('Bill1',backref='user',lazy='dynamic')
            
    #账单表
    class Bill1(db.Model):
        """define bill data model"""
        __tablename__ = 'bill1'
        id = db.Column(db.Integer, primary_key=True)
        customerName = db.Column(db.Unicode(64), unique=False, nullable=False, index=True)#客户名
        date = db.Column(db.DateTime(),unique=False, nullable=False, index=True)#日期时间
        item = db.Column(db.Unicode(64),unique=False,nullable=False,index=True)#类别
        perPrice = db.Column(db.Float(),unique=False,nullable=False,index=False)#单价
        quantity = db.Column(db.Float(),unique=False,nullable=False,index=False)#数量
        totalPrice = db.Column(db.Float(),unique=False,nullable=False,index=False)#总价
        payed = db.Column(db.Boolean(),unique=False,nullable=False,index=False)#支付状态
        checkUser_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    return db,User,Bill1