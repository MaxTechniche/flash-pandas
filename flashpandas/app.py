import time
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
class Question:
    def __init__(self, q_text, a_text, summary=None, tags=[], q_images=[], a_images=[], contributors=[]) -> None:
        self.q_text = q_text
        self.a_text = a_text
        self.summary = summary
        self.tags = tags
        self.q_images = q_images
        self.a_images = a_images
        self.contributors = contributors
        self.time_of_creation = time.time()

    def to_json(self):
        j = {
            'summary': self.summary,
            'question_text': self.q_text,
            'question_image_links': self.q_images,
            'answer_text': self.a_text,
            'answer_image_links': self.a_images,
            'contributors': self.contributors,
            'tags': self.tags,
            'creation_time': self.time_of_creation
        }
