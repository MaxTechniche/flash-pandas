from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(30), nullable=True)

class Question(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    answer_text = DB.Column(DB.String(500))




# TODO Password encrypting (bcrypt)
