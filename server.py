from flask import Flask
from flask import request
from sunset_classifier import SunsetClassifier


app = Flask(__name__)
sc = SunsetClassifier()


@app.route("/")
def root():
    return sc.classify(request.args.get('url'))
