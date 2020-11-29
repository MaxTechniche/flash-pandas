import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from flask import session

from flashpandas.app import APP, users, cards
from pprint import pprint

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
            dbc.Button('Refresh', id='get-cards'),
            dbc.Input(id='card-id', placeholder='Card ID', className='ml-auto', style={'max-width': '250px'}),
            dbc.Button('Report Card', id='report-card')
        ]),
        html.Div(id='card-list', style={'margin-top': '15px'}),
        # modal
    ],
    id='get-cards',
)


@APP.callback(
    Output('card-list', 'children'),
    Input('get-cards', 'n_clicks')
)
def get_cards(n_clicks):

    card_list = []
    username = session.get('username', None)
    if username:
        for card in cards.find({'creator': username}):
            card_list.append(fill_card(card))
            # card_flag_btns.append(str(card['_id']))
    for card in cards.find(
            {
                'creator': {'$ne': username},
                'public': True, 
                'flagged': False, 
            }):
        card_list.append(fill_card(card))
        # card_flag_btns.append(str(card['_id']))

    return card_list

def fill_card(card):
    try:
        layout = \
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
                                        style={
                                            'border-radius': '3px', 
                                            'padding': '5px', 
                                            'margin-bottom': '5px', 
                                            'background-color': '#ccc'
                                        }),
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
                                        style={
                                            'border-radius': '3px', 
                                            'padding': '5px', 
                                            'margin-bottom': '5px', 
                                            'background-color': '#ccc'
                                        }),
                                ], style={'min-width': '200px'}
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Label(
                                'Tags: ' + card['tags'] if card['tags'] else '', 
                                className='mr-auto'), 
                            dbc.Label(
                                'Creator: ' + card['creator'], 
                                className='ml-auto')
                        ], style={'margin': 'auto'}
                    ),
                    html.Div(
                        dbc.Label('Card ID: ' + str(card['_id']), style={'font-size': '12px'}),
                        style={'text-align': 'center'}
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
    return layout

            