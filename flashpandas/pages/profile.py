import time
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.RadioItems import RadioItems
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

from flashpandas.app import APP, users, cards
from flask import session

user_info = html.Div([dbc.Label(id="user-info")], style={"text-align": "center"})


delete_form = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("Enter username to confirm"),
                dbc.Input(
                    id="username-input",
                    autoComplete=False,
                    style={"max-width": "250px", "margin": "auto"},
                ),
                dbc.Label(children=[], id="error-code"),
                html.Div(id="username-display-update"),
                dbc.RadioItems(
                    options=[
                        {
                            "label": "Delete private cards (permanent)",
                            "value": "delete",
                        },
                        {"label": "Make your cards public", "value": "public"},
                    ],
                    value="delete",
                    id="private-cards-option",
                    style={"padding-bottom": "15px"},
                ),
                # dbc.Checkbox(),
                dbc.Button(
                    "Delete Account", id="delete-button", color="danger", size="sm"
                ),
            ],
            style={
                "text-align": "center",
                "padding": "10px",
                "border": "1px solid red",
                "border-radius": "3px",
                "margin": "0px",
            },
        ),
    ],
    style={"padding-top": "75px"},
)


layout = html.Div([user_info, delete_form])


@APP.callback(
    [Output("error-code", "children")],
    Input("delete-button", "n_clicks"),
    [State("username-input", "value"), State("private-cards-option", "value")],
)
def delete_account(n_clicks, value, private_option):
    if n_clicks:
        if session.get("username", None):
            if session["username"] == value:
                time.sleep(3)
                if private_option == "delete":
                    cards.delete_many({"creator": session["username"], "public": False})
                elif private_option == "public":
                    cards.update_many(
                        {"creator": session["username"]}, {"$set": {"public": True}}
                    )
                users.delete_one({"username": value})
                session.pop("username", None)
                return [dcc.Location("url", "/")]
            else:
                return ["Username does not match"]
        return ["You are not logged in. How did you get here?"]
    return [""]


@APP.callback(
    Output("user-info", "children"), Input("username-display-update", "children")
)
def display_user_info(info):
    return "Username:  " + session.get("username", None)
