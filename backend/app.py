#!/usr/bin/python3

from flask import Flask, jsonify, render_template, request
from routes.property_routes import property_bp

app = Flask(__name__)

# Dummy data for testing purposes
properties = [
    {
        "id": 1,
        "address": "123 Main St",
        "price": 200000,
        "size": "2000 sqft",
        "location": "South Africa",
        "pictures": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
        "features": ["Swimming pool", "Garden", "Garage"]
    },
    {
        "id": 2,
        "address": "456 Elm St",
        "price": 300000,
        "size": "2500 sqft",
        "location": "South Africa",
        "pictures": ["https://example.com/image3.jpg", "https://example.com/image4.jpg"],
        "features": ["Balcony", "Fireplace", "Walk-in closet"]
    },
    {
        "id": 3,
        "address": "789 Oak St",
        "price": 400 000,
        "size": "3000 sqft",
        "location": "South Africa",
        "pictures": ["https://example.com/image5.jpg", "https://example.com/image6.jpg"],
        "features": ["Mountain view", "Large backyard", "Modern kitchen"]
    }
]

@app.route('/api/properties/search', methods=['POST'])
def search_properties():
    search_query = request.form.get('searchQuery')
    # Perform search logic based on search_query
    # For demonstration, just filter properties by location
    filtered_properties = [prop for prop in properties if prop['location'] == search_query]
    return jsonify(filtered_properties)

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

