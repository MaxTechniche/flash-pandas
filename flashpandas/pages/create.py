import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from flashpandas.app import APP, users, cards, Card

logged_out_layout = html.Div(['Must be logged in in order to create.', dbc.NavLink(dbc.Button('Login'), href='/login')], style={'text-align': 'center'})


header = html.Div(
    [
        dbc.Label('Card Creation', style={'font-size': '20px', 'margin-bottom':  '0px'}),
        dcc.Markdown('---'),
    ], style={'text-align': 'center'}
)

question_and_answer = dbc.Row([
    dbc.Col([
        dbc.Label('Question Input'),
        dbc.Textarea(
            id='question-input', 
            persistence=True, 
            persistence_type='local',
            style={'margin-bottom': '15px'}),
        dbc.Label('Question View'),
        dcc.Markdown(id='question-view', style={'border': '2px solid #C8E4F4', 'border-radius': '3px', 'padding': '5px', 'margin-bottom': '15px'}),
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
        dcc.Markdown(id='answer-view', style={'border': '2px solid #C8E4F4', 'border-radius': '3px', 'padding': '5px', 'margin-bottom': '15px'}),
        dcc.Markdown('---')
    ], style={'min-width': '200px'})
])

tags_and_title = dbc.Row(
    [
        dbc.Col([
            dbc.Label('Categories (comma separated)'),
            dbc.Input(
                id='tags-input', 
                persistence=True, 
                persistence_type='local',)
        ], style={'min-width': '200px'}),
        dbc.Col([
            dbc.Label('Title or Summary'),
            dbc.Input(
                id='title-input', 
                persistence=True, 
                persistence_type='local',)
        ], style={'min-width': '200px'})
    ]
)

public_and_submit = html.Div(
    [
        dcc.Markdown('---'),
        html.Div(
            [
                dbc.Checkbox(
                    id='public-check', 
                    persistence=True, 
                    persistence_type='local',),
                dbc.Label("Make Public", style={'padding-left': '5px'}),
            ],
        ),
        dbc.Col([
            dbc.Button(
                'Submit Card',
                id='card-submit',
                color='success'
            ),
            dbc.Label(id='error-info')
        ])
    ], style={'text-align': 'center'}
)


layout = html.Div(
    children=[
        header,
        question_and_answer,
        tags_and_title,
        public_and_submit,
    ], id='create-layout',
)

@APP.callback(
    Output('error-info', 'children'),
    Input('card-submit', 'click'),
    [State('question-text', 'value'),
    State('answer-text', 'value'),
    State('tags-input', 'value'),
    State('title-input', 'value'),
    State('public-check', 'checked')])
async def submit_card(n_clicks, q_text, a_text, tags, title, public):
    return 'Puppies'


@APP.callback(
    [Output('question-view', 'children'),
    Output('answer-view', 'children')],
    [Input('question-input', 'value'),
    Input('answer-input', 'value')])
def mirror_text(question, answer):
    return [question, answer]

