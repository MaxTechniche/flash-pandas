from bcrypt import checkpw
import re
import time

import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Label import Label
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from flask import session

from flashpandas.app import APP, users, cards

url = dcc.Location(id='url', pathname='/login')

logged_out_layout = \
    html.Div([
        html.Div('Login', style={'text-align': 'center', 'font-size': '20px'}),
        dbc.Col(
            [
                dbc.Label('Username', id='user-label'),
                dbc.Input(
                    id='username-entry',
                    style={'max-width': '250px', 'margin-bottom': '20px'}
                ),
                dbc.Label('Password'),
                dbc.Input(
                    id='password-entry',
                    type='password',
                    style={'max-width': '250px'}
                ),
                dbc.Checkbox(
                    id='pass-toggle'
                ),
                dbc.Label(
                    'Show Password', 
                    style={'margin-left': '5px'}
                ),
                html.Div(),
                dbc.Button(
                    'Login',
                    id='login-button',
                    color='success'
                ),
                dbc.Label(
                    children=[''],
                    id='info-label',
                    style={'margin-left': '10px'}
                )
            ]
        ),],
        style={'text-alignment': 'center'}

    )

logged_in_layout = \
    html.Div(
        [
            dbc.Label('Already logged in', id='logged-in-label'),
            dbc.Button('Log Out', id='log-out')
        ], 
        style={'text-align': 'center'}
    )


@APP.callback(
    Output('url', 'pathname'),
    Input('log-out', 'n_clicks')
)
def log_out(n_clicks):
    if n_clicks:
        session.pop('username', None)
        return '/'
    else:
        return '/login'

@APP.callback(
    Output('password-entry', 'type'),
    Input('pass-toggle', 'checked')
)
def toggle_password_visibility(checked):
    if checked:
        return 'text'
    else:
        return 'password'

@APP.callback(
    Output('info-label', 'children'),
    Input('login-button', 'n_clicks'),
    [State('username-entry', 'value'),
    State('password-entry', 'value')]
)
def check_login(login_click, username, password):
    if login_click:
        # time.sleep(1)
        if not username or not password:
            return 'user credentials not entered'
        
        user_info = users.find_one({'username': username})

        if not user_info:
            return 'User not found'

        if not checkpw(bytes(password, 'utf-8'), user_info['password']):
            return 'username or password incorrect'

        session['username'] = username
        return dcc.Location(pathname='/', id='login-successful')
    return ''
