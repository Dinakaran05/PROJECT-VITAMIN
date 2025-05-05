from flask import Flask, render_template, request, redirect,session, url_for
from flask_cors import CORS, cross_origin
import os
from detect import vitamindefience
import secrets
import sqlite3


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    if request.method == "GET":
        return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
   if request.method == "POST":
    image_file = request.files['file']
    print(image_file)
    classifier = vitamindefience()  # creating a object of plantleaf class
    result = classifier.vitamindefienceImage(image_file)
    return result
   else:
       print('Loading Error')


if __name__ == "__main__":
    app.run()