# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from gevent import monkey

from flask_sqlalchemy import SQLAlchemy

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/bill1.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

#Database Configuration
class Bill1(db.Model):
	"""define bill data model"""
	id = db.Column(db.Integer, primary_key=True)
	customerName = db.Column(db.Unicode(64), unique=False, nullable=False, index=True)
	date = db.Column(db.Date,unique=False, nullable=False, index=True)

	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

@application.route("/")
def hello():
    return render_template('index.html')

@application.route("/wxapp/check")
def wxapp():
    return '已连接至鑫诚云'

@application.route("/wxapp/upload",methods=['POST'])
def upload():
	print('****------*****',request.get_json(force=True))
    return 'Got It!!!'

@application.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    application.run()
