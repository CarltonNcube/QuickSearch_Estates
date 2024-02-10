#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from .middleware import token_required

property_bp = Blueprint('property', __name__)

# Dummy property data (replace with database integration)
properties = [
    {'id': 1, 'name': 'Property 1', 'price': 100000},
    {'id': 2, 'name': 'Property 2', 'price': 150000},
    {'id': 3, 'name': 'Property 3', 'price': 200000}
]

# Route handler for creating a new property
@property_bp.route('/api/properties', methods=['POST'])
@token_required
def create_property():
    data = request.json
    properties.append(data)
    return jsonify({'message': 'Property created successfully'}), 201

# Route handler for getting all properties
@property_bp.route('/api/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

# Route handler for getting a specific property by ID
@property_bp.route('/api/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = next((p for p in properties if p['id'] == property_id), None)
    if property:
        return jsonify(property)
    else:
        return jsonify({'error': 'Property not found'}), 404

# Route handler for updating an existing property
@property_bp.route('/api/properties/<int:property_id>', methods=['PUT'])
@token_required
def update_property(property_id):
    data = request.json
    property = next((p for p in properties if p['id'] == property_id), None)
    if property:
        property.update(data)
        return jsonify({'message': 'Property updated successfully'})
    else:
        return jsonify({'error': 'Property not found'}), 404

# Route handler for deleting a property
@property_bp.route('/api/properties/<int:property_id>', methods=['DELETE'])
@token_required
def delete_property(property_id):
    global properties
    properties = [p for p in properties if p['id'] != property_id]
    return jsonify({'message': 'Property deleted successfully'})

