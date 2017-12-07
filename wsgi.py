from flask import Flask
from flask import render_template
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template('index.html')

@application.route("/wxapp")
def wxapp():
    return 'Hello form OpenShift!'

@application.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    application.run()
