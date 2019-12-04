import os
from flask import Flask, request, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
