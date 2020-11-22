from os import getenv
from string import ascii_lowercase
import dash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from dash.dependencies import Output, State, Input
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from .pages import home, learn
from pprint import pprint

pages = {
    'home': '',
    'learn': 'learn'
}

def create_app():
    app = dash.Dash(__name__)

    # app.config['DATABASE_URI'] = getenv('DATABASE_URI')
    # DB = SQLAlchemy(app)

    url = dcc.Location(id='url')

    navbar = dbc.Navbar([
        dcc.Link(dbc.Button(f"{page.capitalize()}", id=f"{page}"), href=f"/{url}") for page, url in pages.items()
    ], id='nav', style={'text-align': 'center'})

    page = html.Div(id='page-content')

    app.layout = html.Div([
        url,
        navbar,
        page
    ])



    @app.callback(Output('page-content', 'children'),
                  Input('url', 'pathname'))
    def get_page(pathname):
        if pathname == '/':
            return home.url
        try:
            return globals()[f"{ pathname.replace('/', '') }"].url
        except KeyError:
            return 'Path not found.'

    return app
