#!/usr/bin/env python3

from flask import jsonify
from .models import Listing

def create_listing(data):
    try:
        listing = Listing.create(**data)
        return jsonify(listing), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def delete_listing(listing_id):
    try:
        listing = Listing.get_by_id(listing_id)
        listing.delete()
        return jsonify({'message': 'Listing deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def update_listing(listing_id, data):
    try:
        listing = Listing.get_by_id(listing_id)
        listing.update(**data)
        return jsonify(listing), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def get_listing(listing_id):
    try:
        listing = Listing.get_by_id(listing_id)
        return jsonify(listing), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def get_listings(filters):
    try:
        listings = Listing.query(filters)
        return jsonify(listings), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

