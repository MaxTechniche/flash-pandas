import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from flashpandas.app import APP, users, cards


layout = html.Div('Learn coming later', style={'text-align': 'center'})


# html.Div(
#     [
#         dcc.Markdown(
#             children='Enter name to add',
#             id='markdown'
#         ),
#         dbc.Input(
#             id='name',
#         ),
#         dbc.Button(
#             'add',
#             id='add',
#         )
#     ]
# )

# @APP.callback(
#     Output('markdown', 'children'),
#     Input('add', 'n_clicks'),
#     State('name', 'value')
# )
# def list_learn(clicks, name_value):
#     if clicks:
#         if name_value:
#             if users.find({'faves.color':'blue'}):
#                 print(users.find_one({'Name':name_value}))
#                 return f'{name_value} already in the database'
#             else:
#                 users.insert_one({'Name':name_value, 'faves': {'color': 'blue'}})
#                 return f'Added {name_value}'
#         else:
#             return 'no name entered'
#     else:
#         return 'Enter name to add'

