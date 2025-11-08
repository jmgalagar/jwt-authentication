
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager #import JWT

db = SQLAlchemy()
jwt = JWTManager() #JWT extension initialization