import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from flashpandas.app import APP, users, cards

logged_out_layout = html.Div(['Must be logged in in order to create.', dbc.NavLink(dbc.Button('Login'), href='/login')], style={'text-align': 'center'})

layout = html.Div('Create coming later', style={'text-align': 'center'})
