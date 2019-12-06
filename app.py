import os
from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://root:1ZmNgZ@myfirstcluster-eiytd.mongodb.net/myTestDB?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.myTestDB
collection = db.Recepten

@app.route('/')
def home_page():
    return "This is the global Home page"

@app.route('/europe')
def europe():
    return render_template('index.html')

@app.route('/north-america')
def northamerica():
    return "This is the North-america page"

@app.route('/asia')
def asia():
    return "This is the page for Asia"

@app.route('/dbplayground')
def playground():
    return "This is the page where we play with databases"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True)
