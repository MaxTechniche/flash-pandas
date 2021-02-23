import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import bson
from dash.dependencies import Output, State, Input
from flask import session
from pymongo.collection import ObjectId

from flashpandas.app import APP, users, cards
from pprint import pprint

qa_style = {
        'border-radius': '3px', 
        'padding': '5px', 
        'margin-bottom': '5px', 
        'background-color': '#ccc'
    }

card_flag_btns = []

# modal = dbc.Modal(
#     [
#         dbc.ModalHeader("Report Card"),
#         dbc.ModalBody(
#             [
#                 dbc.Label('Reason for reporting card (inappropriate, incorrect, etc.)'),
#                 dbc.Input(id='flag-reason')
#             ]
#         ),
#         dbc.ModalFooter(
#             dbc.Button('Submit', id='submit-flag', )
#         )
#     ], id='modal'
# )

layout = html.Div(
    [
        dbc.Row([
            dbc.Row([
                dbc.Button('Refresh', id='get-cards'),
                dbc.Row([
                    dbc.Row([
                        dbc.Checkbox(id='show-user-cards', checked=True, style={'margin-top': '5px', 'margin-right': '5px'}),
                        dbc.Label('My cards')
                    ], style={'margin-left': '30px', 'margin-right': '10px', 'margin-top': '7px'}),
                    dbc.Row([
                        dbc.Checkbox(id='show-public-cards', checked=True, style={'margin-top': '5px', 'margin-right': '5px'}),
                        dbc.Label('Public cards')
                    ], style={'margin-left': '10px', 'margin-right': '10px', 'margin-top': '7px'}),
                    dbc.Row([
                        dbc.Checkbox(id='show-questions', checked=True, style={'margin-top': '5px', 'margin-right': '5px'}),
                        dbc.Label('Show Questions')
                    ], style={'margin-left': '30px', 'margin-right': '10px', 'margin-top': '7px'}),
                    dbc.Row([
                        dbc.Checkbox(id='show-answers', checked=False, style={'margin-top': '5px', 'margin-right': '5px'}),
                        dbc.Label('Show Answers')
                    ], style={'margin-left': '10px', 'margin-right': '10px', 'margin-top': '7px'}),
                ])
            ], style={'margin': 'auto', 'text-align': 'center'}),
            dbc.Row([
                dbc.Button('Report Card', id='report-card'),
                dbc.Label(id='report-code', style={'margin': '7px', 'color': 'red'}),
                dbc.Row([
                    dbc.Input(id='card-id', placeholder='Card ID', style={'width': '200px'}),
                    dbc.Input(id='flag-reason', placeholder='Reason to report', style={'width': '150px'}),
                ], style={'margin': 'auto'})
            ], style={'margin': 'auto', 'text-align': 'center'})
        ], style={'margin': 'auto', 'text-align': 'center'}),
        html.Div('Loading...', id='card-list', style={'margin-top': '15px'}),
        html.Div(id='test')
        # modal
    ]
)


@APP.callback(
    Output('card-list', 'children'),
    [Input('get-cards', 'n_clicks'),
    Input('show-user-cards', 'checked'),
    Input('show-public-cards', 'checked'),
    Input('report-code', 'children')]
)
def get_cards(n_clicks, personal, public, children):

    card_list = []
    username = session.get('username', None)
    if username:
        if personal:
            for card in cards.find({'creator': username}):
                card_list.append(fill_card(card))
                # card_flag_btns.append(str(card['_id']))
    if public:
        for card in cards.find(
                {
                    'creator': {'$ne': username},
                    'public': True, 
                    'flagged': False, 
                }):
            card_list.append(fill_card(card))
            # card_flag_btns.append(str(card['_id']))

    if not card_list:
        return html.Div('No cards', style={'text-align': 'center'})

    return card_list

def fill_card(card):
    try:
        card_layout = \
            html.Div(
                [
                    html.Div(
                        card['title'] if card['title'] else '', 
                        style={
                            'text-align': 'center', 
                            'margin-bottom': '5px',
                            'font-size': '20px',
                            'font-weight': 'bold'
                        }),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        'Question', 
                                        style={
                                            'text-align': 'center', 
                                            'font-size': '16px'
                                        }),
                                    dcc.Markdown(
                                        card['question_text'], 
                                        id='question',
                                        style=qa_style),
                                ], style={'min-width': '200px'}
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        'Answer', 
                                        style={
                                            'text-align': 'center', 
                                            'font-size': '16px'
                                        }),
                                    dcc.Markdown(
                                        card['answer_text'], 
                                        id='answer',
                                        style=qa_style),
                                ], style={'min-width': '200px'}
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Label(
                                'Tags: ' + ', '.join(card['tags']) if card['tags'] else '', 
                                className='mr-auto'), 
                            dbc.Label(
                                'Creator: ' + card['creator'], 
                                className='ml-auto')
                        ], style={'margin': 'auto'}
                    ),
                    html.Div(
                        [
                            dbc.Label('Flagged: ' + card['flag_reason'] if card['flagged'] else '', 
                                style={'margin-right': '5px', 'color': 'red'}),
                            dbc.Label('Card ID: ' + str(card['_id']), 
                                style={'font-size': '12px'}),
                        ], style={'text-align': 'center'}
                    )
                    # Report Button
                    # html.Div(
                    #     dbc.Button('REPORT CARD', id=str(card['_id']), size='sm'), 
                    #     style={'text-align': 'center'}
                    # )
                ], 
                style={
                    'border': '1px solid #000', 
                    'border-radius': '10px', 
                    'padding': '5px', 
                    'margin-bottom': '30px', 
                    'background-color': '#f0f0f0'
                }
            )
    except Exception as e:
        print(e)
        return 'Error with card'
    return card_layout

            
@APP.callback(
    Output('report-code', 'children'),
    Input('report-card', 'n_clicks'),
    [State('card-id', 'value'),
    State('flag-reason', 'value')]
)
def report_card(n_clicks, card_id, reason):
    if n_clicks:
        if not card_id:
            return 'No ID provided'
        try:
            obj_id = ObjectId(card_id)
        except bson.errors.InvalidId:
            return 'Invalid ID'
        code = cards.update_one({'_id': obj_id}, {'$set': {'flagged': True, 'flag_reason': reason or 'Unknown', 'public': False}})
        if code.matched_count:
            return 'Card Reported'

    return ''

@APP.callback(
    Output('question', 'style'),
    Input('show-questions', 'checked')
)
def show_questions(show):
    if show:
        next = qa_style.copy()
        next.update({'filter': 'opacity(1)'})
        return next
    return qa_style

@APP.callback(
    Output('answer', 'style'),
    Input('show-answers', 'checked')
)
def show_answers(show):
    if show:
        next = qa_style.copy()
        next.update({'filter': 'opacity(1)'})
        return next
    return qa_style
