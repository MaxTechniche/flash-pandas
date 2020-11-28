import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from flashpandas.app import APP, users, cards, Card

logged_out_layout = html.Div(['Must be logged in in order to create.', dbc.NavLink(dbc.Button('Login'), href='/login')], style={'text-align': 'center'})


card = dbc.Row([
    dbc.Col([
        dbc.Label('Question Input'),
        dbc.Textarea(
            id='question-input', 
            persistence=True, 
            persistence_type='local',
            style={'margin-bottom': '15px'}),
        dbc.Label('Question View'),
        dcc.Markdown(id='question-text', style={'border': '2px solid #C8E4F4', 'border-radius': '3px', 'padding': '5px', 'margin-bottom': '15px'}),
        dcc.Markdown('---')
    ], style={'min-width': '200px'}),
    dbc.Col([
        dbc.Label('Answer Input'),
        dbc.Textarea(
            id='answer-input',
            persistence=True, 
            persistence_type='local',
            style={'margin-bottom': '15px'}),
        dbc.Label('Answer View'),
        dcc.Markdown(id='answer-text', style={'border': '2px solid #C8E4F4', 'border-radius': '3px', 'padding': '5px', 'margin-bottom': '15px'}),
        dcc.Markdown('---')
    ], style={'min-width': '200px'})
])



layout = html.Div(
    children=[
        dbc.Label('Card Creation', style={'font-size': '20px', 'margin-bottom':  '0px'}),
        dcc.Markdown('---'),
        card,
        dbc.Button(
            "Submit Card",
            id='card-submit',
            color='success'
        ),
    ],
    id='create-layout',
    style={'text-align': 'center'}
)

@APP.callback(
    [Output('question-text', 'children'),
    Output('answer-text', 'children')],
    [Input('question-input', 'value'),
    Input('answer-input', 'value')])
def mirror_text(question, answer):
    return [question, answer]
