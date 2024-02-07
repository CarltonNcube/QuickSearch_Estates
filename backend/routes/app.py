#!/usr/bin/env python3
from flask import Flask, request, jsonify
from backend.controllers.auth_controller import google, sign_out, signin, signup

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup_route():
    # Implement signup logic here
    return jsonify({'message': 'Signup route'})

@app.route('/signin', methods=['POST'])
def signin_route():
    # Implement signin logic here
    return jsonify({'message': 'Signin route'})

@app.route('/google', methods=['POST'])
def google_auth():
    # Implement Google OAuth logic here
    return jsonify({'message': 'Google OAuth route'})

@app.route('/signout', methods=['GET'])
def signout_route():
    # Implement signout logic here
    return jsonify({'message': 'Signout route'})

if __name__ == '__main__':
    app.run(debug=True)

