import time
from bcrypt import hashpw, gensalt
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from flask import session

from flashpandas.app import APP, users, cards

layout = \
    html.Div([
        html.Div("Create Account", style={'text-align': 'center', 'font-size': '20px'}),
        dbc.Col(
            [
                # dbc.Label('Email: needed to reset password', id='email-label'),
                # dbc.Input(
                #     id='email-entry',
                #     style={'max-width': '250px', 'margin-bottom': '20px'}
                # ),
                dbc.Label('Username: 6-30 characters'),
                dbc.Input(
                    id='username-signup-entry',
                    style={'max-width': '250px', 'margin-bottom': '20px'}
                ),
                dbc.Label('Password: 6-30 characters'),
                dbc.Input(
                    id='password-signup-entry',
                    type='password',
                    style={'max-width': '250px'}
                ),
                dbc.Checkbox(
                    id='pass-signup-toggle'
                ),
                dbc.Label('Show Password', style={'margin-left': '5px'}),
                html.Div(),
                dbc.Button(
                    "Create Account",
                    id='signup-button',
                    color='success'
                ),
                dbc.Label(
                    children=[''],
                    id='info-signup-label',
                    style={'margin-left': '10px'}
                )
            ]
        ),],
        style={'text-alignment': 'center'}
    )


@APP.callback(
    Output('password-signup-entry', 'type'),
    Input('pass-signup-toggle', 'checked')
)
def toggle_signup_password_visibility(checked):
    if checked:
        return 'text'
    else:
        return 'password'

@APP.callback(
    Output('info-signup-label', 'children'),
    Input('signup-button', 'n_clicks'),
    [State('username-signup-entry', 'value'),
    State('password-signup-entry', 'value')]
)
def check_signup(n_clicks, username, password):
    if n_clicks:
        if not username or not password:
            return 'user credentials not entered'

        if len(username) > 30:
            return 'Username too long'

        if len(username) < 6:
            return 'Username too short'

        if len(password) > 30:
            return 'Password too long'

        if len(password) < 6:
            return 'Password too short'

        user_info = users.find_one({'username': username})

        if user_info:
            return "Username already in use"

        time_of_creation = time.time()
        time.sleep(1)
        session['username'] = username
        users.insert_one({
            'username': username, 
            'password': hashpw(bytes(password, 'utf-8'), gensalt()), 
            'creation': time_of_creation})
        return dcc.Location('url', '/')
    return ''
