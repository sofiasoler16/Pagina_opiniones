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

    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')

    # app.config.from_object(Config)

    db.init_app(app)

    from main.routes import initialize_routes
    initialize_routes(api)

    api.init_app(app)

    
    jwt.init_app(app)    



    mail.init_app(app)





    return app
