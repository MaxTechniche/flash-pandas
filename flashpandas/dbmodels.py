from typing import Sequence
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(30), nullable=True)


# TODO Password encrypting (bcrypt)
