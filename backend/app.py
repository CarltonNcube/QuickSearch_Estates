#!/usr/bin/python3

from flask import Flask, jsonify
from routes.property_routes import property_bp

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    # Perform some operation to retrieve data
    data = {'key': 'value'}
    return jsonify(data)

app.register_blueprint(property_bp)

if __name__ == '__main__':
    app.run(host='172.17.0.6', port=5000, debug=True)
