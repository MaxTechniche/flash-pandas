
from .app import create_app
from .pages import home, learn, test


from pprint import pprint

import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Button import Button
from dash_bootstrap_components._components.NavLink import NavLink
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from .dbmodels import DB, User

app = create_app()
server = app.server

pages = {
    'learn': {
        'url': '/learn', 
        'button': {
            'color': 'warning',
            'outline': True,
            'style': {
                'margin-right': '1%'}
            },
    },
    'home': {
        'url': '/', 
        'button': {
            'color': 'success',
            'outline': True,
            'style': {
                'margin-right': '1%'}
            }, 
    },
    'test': {
        'url': '/test', 
        'button': {
            'color': 'primary',
            'outline': True,
            'style': {
                'margin-right': '1%'}
            },
    }
}

my_blue = '#C8E4F4'

url = dcc.Location(id='url')

navbar = \
    dbc.Navbar(
        dbc.Row(
            [
                dbc.NavLink(
                    dbc.Button(
                        children=f"{name.capitalize()}", 
                        id=f"{name}",
                        color=info['button']['color'],
                        outline=info['button']['outline'],
                    ),
                    href=info['url'],
                    style={'margin': '0px', 'padding': '5px'}
                ) 
                for name, info in pages.items()
            ], 
            style={'margin': 'auto'}
        ), 
        id='nav',
    )

page = html.Div(id='page-content', style={'margin': '1rem'})

footer = \
    html.Div(
        [
            html.A(
                dbc.Button(
                    "YouTube",
                    id='youtube',
                    color='danger',
                    outline=True,
                    size='sm'
                ),
                href="https://youtube.com/MaxTechniche",
                style={'margin': '1%'}
            ),
            html.A(
                dbc.Button(
                    "GitHub",
                    id='github',
                    color='dark',
                    outline=True,
                    size='sm'
                ),
                href="https://github.com/MaxTechniche",
                style={'margin': '1%'}
            ),
        ], 
        style={'text-align': 'center'}
    )

app.layout = dbc.Container(
    [
        url,
        navbar,
        page,
        footer
    ], 
    style={
        'word-wrap': 'break-word', 
        'position': 'relative', 
        'min-height': '95vh'
    }
)


@app.callback(Output('page-content', 'children'),
                Input('url', 'pathname'))
def display_page(pathname):
    DB.drop_all()
    DB.create_all()
    if pathname == '/':
        return home.layout
    try:
        return globals()[f"{ pathname.replace('/', '') }"].layout
    except KeyError:
        return 'Path not found.'

