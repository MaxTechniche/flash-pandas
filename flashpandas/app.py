from os import getenv

import dash
import dash_bootstrap_components as dbc
import flask_sqlalchemy

from .dbmodels import DB


def create_app():
    app = dash.Dash(__name__, 
        external_stylesheets=[
            dbc.themes.LUMEN, 
            'https://use.fontawesome.com/releases/v5.9.0/css/all.css'
        ]
    )

    app.server.config.suppress_callback_exceptions = True
    app.title = 'Flash Pandas'

    app.server.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app.server)

    return app
