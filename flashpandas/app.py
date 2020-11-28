import time
import datetime
import dash
import dash_bootstrap_components as dbc
from flask_pymongo import PyMongo
from os import getenv

APP = dash.Dash(__name__, 
    external_stylesheets=[
        dbc.themes.LUMEN, 
        'https://use.fontawesome.com/releases/v5.9.0/css/all.css',
    ], 
)

APP.title = 'Flash Pandas'

APP.server.config.suppress_callback_exceptions = True
APP.server.secret_key = getenv('SECRET_KEY')
mongo_db = getenv('MONGO_DB_URI')
APP.server.config['MONGO_URI'] = mongo_db

DB = PyMongo(APP.server)

# DB.init_app(APP.server)

users = DB.db.users
cards = DB.db.cards


    # return APP
# MODELS
class Card:
    def __init__(self, title, q_text, a_text, tags=[], public=False, contributor=[]) -> None:
        self.title = title
        self.q_text = q_text
        self.a_text = a_text
        self.tags = tags
        self.public = public
        self.contributor = contributor

    def to_json(self):
        return {
            'title': self.title,
            'question_text': self.q_text,
            'answer_text': self.a_text,
            'tags': self.tags,
            'public': self.public,
            'contributor': self.contributor,
            'flagged': False,
            'creation_time': datetime.datetime.utcnow()
        }
