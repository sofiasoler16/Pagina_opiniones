from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail


import os

from config import Config

db = SQLAlchemy()
api = Api()
jwt = JWTManager()
mail = Mail()

def create_app():
    load_dotenv()
    app = Flask(__name__)


    app.config.from_object('Config')


    db.init_app(app)

    import main.resources as resources

    api.init_app(app)

    
    jwt.init_app(app)


    mail.init_app(app)



    return app
