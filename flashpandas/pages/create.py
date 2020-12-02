import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from pymongo.errors import DuplicateKeyError
from flask import session

from flashpandas.app import APP, users, cards, Card

logged_out_layout = html.Div(
    [
        "Must be logged in in order to create.",
        dbc.NavLink(dbc.Button("Login"), href="/login"),
    ],
    style={"text-align": "center"},
)


header = html.Div(
    [
        dbc.Label("Card Creation", style={"font-size": "20px", "margin-bottom": "0px"}),
        dcc.Markdown("---"),
    ],
    style={"text-align": "center"},
)

question_and_answer_input = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label(
                    children=[
                        "Question Input (uses ",
                        html.A(
                            "Markdown",
                            href="https://www.markdownguide.org/",
                            target="_blank",
                        ),
                        ")",
                    ]
                ),
                dbc.Textarea(
                    id="question-input",
                    persistence=True,
                    persistence_type="memory",
                    style={"margin-bottom": "15px"},
                ),
            ],
            style={"min-width": "250px"},
        ),
        dbc.Col(
            [
                dbc.Label(
                    children=[
                        "Answer Input (uses ",
                        html.A(
                            "Markdown",
                            href="https://www.markdownguide.org/",
                            target="_blank",
                        ),
                        ")",
                    ]
                ),
                dbc.Textarea(
                    id="answer-input",
                    persistence=True,
                    persistence_type="memory",
                    style={"margin-bottom": "15px"},
                ),
            ],
            style={"min-width": "250px"},
        ),
    ]
)

question_and_answer_view = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("Question View"),
                dcc.Markdown(
                    id="question-view",
                    style={
                        "border": "2px solid #C8E4F4",
                        "border-radius": "3px",
                        "padding": "5px",
                        "margin-bottom": "15px",
                    },
                ),
                dcc.Markdown("---"),
            ],
            style={"min-width": "250px"},
        ),
        dbc.Col(
            [
                dbc.Label("Answer View"),
                dcc.Markdown(
                    id="answer-view",
                    style={
                        "border": "2px solid #C8E4F4",
                        "border-radius": "3px",
                        "padding": "5px",
                        "margin-bottom": "15px",
                    },
                ),
                dcc.Markdown("---"),
            ],
            style={"min-width": "250px"},
        ),
    ]
)

tags_and_title = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("Tags (future goal) (comma separated)"),
                dbc.Input(
                    id="tags-input",
                    persistence=True,
                    persistence_type="memory",
                ),
            ],
            style={"min-width": "200px"},
        ),
        dbc.Col(
            [
                dbc.Label("Title or Summary"),
                dbc.Input(
                    id="title-input",
                    persistence=True,
                    persistence_type="memory",
                ),
            ],
            style={"min-width": "200px"},
        ),
    ]
)

public_and_submit = html.Div(
    [
        dcc.Markdown("---"),
        html.Div(
            [
                dbc.Checkbox(
                    id="public-check",
                    persistence=True,
                    checked=False,
                    persistence_type="memory",
                ),
                dbc.Label("Make Public", style={"padding-left": "5px"}),
            ]
        ),
        dbc.Col(
            [
                dbc.Button("Submit Card", id="card-submit", color="success"),
                html.Div(),
                dbc.Label(id="error-info", style={"padding-top": "10px"}),
            ]
        ),
    ],
    style={"text-align": "center"},
)


layout = html.Div(
    children=[
        header,
        question_and_answer_input,
        question_and_answer_view,
        tags_and_title,
        public_and_submit,
    ],
    id="create-layout",
)


@APP.callback(
    [Output("question-view", "children"), Output("answer-view", "children")],
    [Input("question-input", "value"), Input("answer-input", "value")],
)
def mirror_text(question, answer):
    return [question, answer]


@APP.callback(
    Output("error-info", "children"),
    Input("card-submit", "n_clicks"),
    [
        State("question-input", "value"),
        State("answer-input", "value"),
        State("tags-input", "value"),
        State("title-input", "value"),
        State("public-check", "checked"),
    ],
)
def submit_card(n_clicks, q_input, a_input, tags, title, public):
    if n_clicks:
        if not q_input:
            return "No question provided"
        if not a_input:
            return "No answer provided"

        card = Card(
            title=title or "",
            q_text=q_input,
            a_text=a_input,
            tags=tags.strip().split(",") if tags else [],
            public=public or False,
            creator=session.get("username", None),
        )

        cards.insert_one(card.to_json())

        return dcc.Location("url", "/cards")

    return ""
