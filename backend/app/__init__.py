import os
import sys

# Ensure backend root is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from config import Config  # Ensure this import works

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    CORS(app)

    from app.routes.resume_routes import resume_bp
    from app.routes.analysis_routes import analysis_bp
  

    app.register_blueprint(resume_bp, url_prefix="/api/resume")
    app.register_blueprint(analysis_bp, url_prefix="/api/analysis")


    return app
