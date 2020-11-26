# from flask_sqlalchemy import SQLAlchemy

# DB = SQLAlchemy()

# association_table = DB.Table('association', DB.metadata,
#     DB.Column('user_username', DB.VARCHAR(20), DB.ForeignKey('user.username')),
#     DB.Column('question_id', DB.Integer, DB.ForeignKey('question.id'))
# )

# class User(DB.Model):
#     id = DB.Column(DB.Integer, primary_key=True)
#     username = DB.Column(DB.VARCHAR(20), primary_key=True, nullable=False, unique=True)
#     contributions = DB.relationship(
#         "Question", 
#         secondary=association_table,
#         back_populates="contributors"
#     )

# class Question(DB.Model):
#     id = DB.Column(DB.Integer, primary_key=True)
#     question_text = DB.Column(DB.String(), nullable=False)
#     answer_text = DB.Column(DB.String(), nullable=True)
#     contributors = DB.relationship(
#         "User",
#         secondary=association_table,
#         back_populates="contributions"
#     )
# from pymongo import MongoClient
from flask_pymongo import PyMongo

DB = PyMongo()
# class User(DB.Document):
#     id = DB.Column(DB.Integer, primary_key=True)
#     username = DB.Column(DB.VARCHAR(20), primary_key=True, nullable=False, unique=True)
#     contributions = DB.relationship(
#         "Question", 
#         secondary=association_table,
#         back_populates="contributors"
#     )

# class Question(DB.Document):
#     id = DB.Column(DB.Integer, primary_key=True)
#     question_text = DB.Column(DB.String(), nullable=False)
#     answer_text = DB.Column(DB.String(), nullable=True)
#     contributors = DB.relationship(
#         "User",
#         secondary=association_table,
#         back_populates="contributions"
    # )





# TODO Password encrypting (bcrypt)
