from os import getenv

import dash
import dash_bootstrap_components as dbc

from .dbmodels import DB
from pymongo import MongoClient


# def create_APP():
APP = dash.Dash(__name__, 
    external_stylesheets=[
        dbc.themes.LUMEN, 
        'https://use.fontawesome.com/releases/v5.9.0/css/all.css',
    ], 
)

APP.title = 'Flash Pandas'

# SQLAlchemy
APP.server.config.suppress_callback_exceptions = True
# APP.server.config["SQLALCHEMY_DATABASE_URI"] = 
# APP.server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# MongoAlchemy 
# APP.server.config['MONGOALCHEMY_SERVER_AUTH'] = False

mongo_db = getenv('MONGO_DB_URI')

APP.server.secret_key = getenv('SECRET_KEY')

APP.server.config['MONGO_URI'] = mongo_db

DB.init_app(APP.server)

users = DB.db.users
questions = DB.db.questions


    # return APP
