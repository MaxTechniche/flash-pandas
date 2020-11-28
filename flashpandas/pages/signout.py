from dash.dependencies import Output, Input
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from flashpandas.app import APP
from flask import session

# url = dcc.Location(id='url', pathname='/signout')
layout = html.Div(children=[dbc.Label('Signed out.', id='signout-label')], id='re-direct', style={'text-align': 'center'})

# @APP.callback(Output('rd-direct', 'children'), Input('signout-label', 'children'))
# def redirect_to_home(children):
#     session.pop('username', None)
#     time.sleep(2)
#     print('slept')
#     return dcc.Location(pathname='/', id='yeyayae')
