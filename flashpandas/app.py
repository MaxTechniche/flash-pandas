import time
import datetime
import dash
import dash_bootstrap_components as dbc
from flask_pymongo import PyMongo
from os import getenv


meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}]

APP = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.LUMEN,
        "https://use.fontawesome.com/releases/v5.9.0/css/all.css",
    ],
    meta_tags=meta_tags,
)

APP.title = "Flash Pandas"

APP.config.suppress_callback_exceptions = False
APP.server.secret_key = getenv("SECRET_KEY")
mongo_db = getenv("MONGO_DB_URI")
APP.server.config["MONGO_URI"] = mongo_db

DB = PyMongo(APP.server)

# DB.init_app(APP.server)

users = DB.db.users
cards = DB.db.cards
comments = DB.db.comments


# return APP
# MODELS
class Card:
    def __init__(
        self, title, q_text, a_text, tags=[], public=False, creator=None
    ) -> None:
        self.title = title
        self.q_text = q_text
        self.a_text = a_text
        self.tags = tags
        self.public = public
        self.creator = creator

    def to_json(self):
        return {
            "title": self.title,
            "question_text": self.q_text,
            "answer_text": self.a_text,
            "tags": self.tags,
            "public": self.public,
            "creator": self.creator,
            "flagged": False,
            "flag_reason": "",
            "creation_time": datetime.datetime.utcnow(),
        }
