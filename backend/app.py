#!/usr/bin/python3

from flask import Flask
from backend.routes.user_routes import user_routes_blueprint
from backend.routes.property_routes import property_routes_blueprint

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(user_routes_blueprint, url_prefix='/api')
    app.register_blueprint(property_routes_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
