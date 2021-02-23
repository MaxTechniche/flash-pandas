import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from flask import session

from flashpandas.app import APP, users, cards, comments

layout = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Flash Pandas
            Flash Pandas is a website designed to help those interested in learning and/or testing their knowledge of Data Science concepts and technical problems.  

            Click on learn to view flash cards already created.  
            You must have an account to create a card, but you do not need an account to view public flash cards.""",
        ),
        dbc.Label(
            "If you'd like to submit a question, comment, concern, or complaint, please do so below. Include as much detail as you can. Email is NOT required unless you hope for a reply."
        ),
        dbc.Input(
            id="contact-email", placeholder="Email", style={"max-width": "300px"}
        ),
        dbc.Textarea(id="contact-text", placeholder="Comment"),
        html.Div(
            [
                dcc.Markdown(id="contact-code"),
                dbc.Button("Submit", id="contact-submit"),
            ],
            style={"text-align": "center"},
        ),
    ]
)


@APP.callback(
    Output("contact-code", "children"),
    Input("contact-submit", "n_clicks"),
    [State("contact-text", "value"), State("contact-email", "value")],
)
def submit_comment(n_clicks, comment, email):
    if n_clicks:
        if not comment:
            return "No text detected"

        code = comments.insert_one(
            {
                "comment": comment,
                "email": users.find_one({"username": session.get("username")})["email"],
            }
        )

        return """
            Submission Successful.  
            Here is your comment ID:  
            """ + str(
            code.inserted_id
        )

    return ""
