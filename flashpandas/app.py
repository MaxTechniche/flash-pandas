from os import getenv

import dash
import dash_bootstrap_components as dbc

from .dbmodels import DB
from dotenv import load_dotenv
load_dotenv()


def create_app():
    app = dash.Dash(__name__, 
        external_stylesheets=[
            dbc.themes.LUMEN, 
            'https://use.fontawesome.com/releases/v5.9.0/css/all.css'
        ]
    )

    app.title = 'Flash Pandas'

    # SQLAlchemy
    # app.server.config.suppress_callback_exceptions = True
    # app.server.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://oaymqsay:UJeG8QPe0kUGEpTKGMllsZDzPEdeBxCl@suleiman.db.elephantsql.com:5432/oaymqsay'
    # app.server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # MongoAlchemy 
    app.server.config['MONGOALCHEMY_SERVER_AUTH'] = False

    mongo_db = getenv('MONGO_DB_URI')
    print(mongo_db)

    app.server.config['MONGO_URI'] = \
                getenv('MONGO_DB_URI')

    DB.init_app(app.server)


    return app
