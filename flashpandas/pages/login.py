import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Checkbox import Checkbox
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from flashpandas.app import APP, users, questions


layout = \
    dbc.Row(
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
                dbc.Label('Show Password', style={'margin-left': '5px'}),
                html.Div(),
                dbc.Button(
                    "Login",
                    id='login-button',
                    color='success'
                ),
                dbc.Label(
                    children=[''],
                    id='info-label',
                    style={'margin-left': '10px'}
                )
            ]
        ),
        style={'text-alignment': 'center'}
    )

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
    [Output('info-label', 'children'),
    Output('user-details', 'children')],
    Input('login-button', 'n_clicks'),
    [State('username-entry', 'value'),
    State('password-entry', 'value')]
)
def check_login(login_click, username, password):
    if login_click:
        if not username or not password:
            return 'user credentials not entered', None
        else:
            # user_info = users.find_one()
            return dcc.Location(pathname='/', id='login-successful'), 'Logged in'
    return '', None
