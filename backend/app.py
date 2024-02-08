#!/usr/bin/python3

from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data for demonstration
properties = [
    {'id': 1, 'name': 'Property 1', 'price': 100000},
    {'id': 2, 'name': 'Property 2', 'price': 150000},
    {'id': 3, 'name': 'Property 3', 'price': 200000}
]

# GET endpoint to retrieve all properties
@app.route('/api/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

# GET endpoint to retrieve a specific property by ID
@app.route('/api/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = next((p for p in properties if p['id'] == property_id), None)
    if property:
        return jsonify(property)
    else:
        return jsonify({'error': 'Property not found'}), 404

# POST endpoint to create a new property
@app.route('/api/properties', methods=['POST'])
def create_property():
    data = request.json
    properties.append(data)
    return jsonify(data), 201

# PUT endpoint to update an existing property
@app.route('/api/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    data = request.json
    property = next((p for p in properties if p['id'] == property_id), None)
    if property:
        property.update(data)
        return jsonify(property)
    else:
        return jsonify({'error': 'Property not found'}), 404

# DELETE endpoint to delete a property
@app.route('/api/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    global properties
    properties = [p for p in properties if p['id'] != property_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

