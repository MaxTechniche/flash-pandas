# from sqlalchemy import Table
# from sqlalchemy.schema import Table
from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

association_table = DB.Table('association',
    DB.Column('user_id', DB.Integer, DB.ForeignKey('user.id')),
    DB.Column('question_id', DB.Integer, DB.ForeignKey('question.id'))
)

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.VARCHAR(30), nullable=False)
    contributions = DB.relationship(
        "Question", 
        secondary=association_table,
        back_populates="contributors"
    )

class Question(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    question_text = DB.Column(DB.String(), nullable=False)
    answer_text = DB.Column(DB.String(), nullable=True)
    contributors = DB.relationship(
        "User",
        secondary=association_table,
        back_populates="contributions"
    )




# TODO Password encrypting (bcrypt)
