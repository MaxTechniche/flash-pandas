import time
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from flask import session
from dash.dependencies import Output, State, Input
from .app import APP, users, cards
from .pages import home, learn, test, login, signup, search, create, signout, profile


app = APP
server = app.server

my_blue = "#C8E4F4"

user_details = html.Div(id="user-details", style={"display": "none"})

url = dcc.Location(id="url")


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink("Cards", href="/cards"),
        # dbc.NavLink('Test', href='/test'),
        dbc.NavLink("Create", href="/create", disabled=True, id="create-link"),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Login", href="/login"),
                dbc.DropdownMenuItem("Create Account", href="/signup"),
            ],
            id="account-dropdown",
            label="Account",
            nav=True,
            style={"margin-right": "20px"},
        ),
    ],
    brand="Flash-Pandas",
    brand_href="/",
    sticky="top",
    style={"margin": "0px", "margin-left": "20px", "margin-right": "20px"},
)


page = html.Div(id="page-content", style={"margin": "1rem"})

footer = dbc.Col(
    [
        "Built by Jacob Maxfield with Dash.",
        html.Div(
            [
                html.A(
                    dbc.Button(
                        "YouTube", id="youtube", color="danger", outline=True, size="sm"
                    ),
                    href="https://youtube.com/MaxTechniche",
                    style={"margin": "1%"},
                ),
                html.A(
                    dbc.Button(
                        "GitHub", id="github", color="dark", outline=True, size="sm"
                    ),
                    href="https://github.com/MaxTechniche",
                    style={"margin": "1%"},
                ),
            ],
            style={"margin-top": "5px"},
        ),
    ],
    style={"text-align": "center", "margin-bottom": "15px"},
)

app.layout = dbc.Container(
    [user_details, url, navbar, page, footer],
    style={"word-wrap": "break-word", "position": "relative", "min-height": "95vh"},
)


@app.callback(
    [
        Output("create-link", "disabled"),
        Output("account-dropdown", "children"),
        Output("page-content", "children"),
    ],
    Input("url", "pathname"),
)
def display_page(pathname):

    n_layout = None

    if pathname == "/":
        n_layout = [home.layout]

    if pathname == "/login":
        if session.get("username", None):
            n_layout = [login.logged_in_layout]
        else:
            n_layout = [login.logged_out_layout]

    if pathname == "/signup":
        n_layout = [signup.layout]

    if pathname in ["/signout", "/logout"]:
        session.pop("username", None)
        time.sleep(1)
        n_layout = [home.layout]

    if pathname == "/create":
        if not session.get("username", None):
            n_layout = [create.logged_out_layout]
        else:
            n_layout = [create.layout]

    if pathname == "/cards":
        n_layout = [learn.layout]

    if not n_layout:
        try:
            n_layout = [globals()[f"{ pathname.replace('/', '') }"].layout]
        except KeyError:
            n_layout = html.Div("Path not found.", style={"text-align": "center"})

    c_link = get_create_link()
    a_drop = get_account_dropdown()

    return [c_link, a_drop, n_layout]


def get_create_link():
    if session.get("username", None):
        return False
    return True


def get_account_dropdown():
    if session.get("username", None):
        return [
            dbc.DropdownMenuItem("Profile", href="/profile"),
            dbc.DropdownMenuItem("Sign Out", href="/signout"),
        ]
    else:
        return [
            dbc.DropdownMenuItem("Login", href="/login"),
            dbc.DropdownMenuItem("Create Account", href="/signup"),
        ]


def get_page_content():
    pass
