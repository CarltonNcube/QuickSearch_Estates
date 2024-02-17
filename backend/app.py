#!/usr/bin/python3

from flask import Flask, jsonify, render_template
from routes.property_routes import property_bp

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    # Perform some operation to retrieve data
    data = {'key': 'value'}
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

app.register_blueprint(property_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

