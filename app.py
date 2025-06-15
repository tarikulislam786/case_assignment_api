from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
app = Flask(__name__)

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Blueprint imports
from models import *
from routes import assignment_bp
from auth import auth_bp

app.register_blueprint(assignment_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

