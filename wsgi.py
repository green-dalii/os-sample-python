from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template('index.html')

@application.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    application.run()
