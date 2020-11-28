import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Label import Label
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from flashpandas.app import APP, users, cards
from flask import session

delete_form = dbc.Row(
    [
        dbc.Label('Username:'),
        dbc.Input(id='username-input', style={'max-width': '250px'}),
        dbc.Button("Delete Account", id='delete-button')
    ]
)
    

layout = html.Div(
    [
        dbc.Label(id='error-code'),
        html.Div(
            children=delete_form,
            id='delete-form'
        )
    ]
)

@APP.callback([
    Output('error-code', 'children'),
    Output('delete-form', 'children')],
    Input('delete-button', 'n_clicks'),
    State('username-input', 'value')
)
def delete_account(n_clicks, value):
    if n_clicks:
        if session.get('username', None):
            if session['username'] == value:
                users.delete_one({'username': value})
                session.pop('username', None)
                return 'Account Deleted', []
        else:
            return 'Username does not match', delete_form
    return '', delete_form
