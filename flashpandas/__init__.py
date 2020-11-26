
from .app import APP, users, questions
from .pages import home, learn, test, login, signup, search, create


from pprint import pprint

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

# Use in future when you have access to larger SQL storage
# from .dbmodels import DB, users, questions

app = APP
server = app.server

page_names = {
    'create': {
        'url': '/create',
        'color': 'purple'
    },
    'search': {
        'url': '/search',
        'color': 'yellow'
    },
    'learn': {
        'url': '/learn',
        'color': 'warning'
    },
    'home': {
        'url': '/',
        'color': 'success'
    },
    'test': {
        'url': '/test',
        'color': 'primary'
    },
    'login': {
        'url': '/login',
        'color': 'info'
    },
    'signup': {
        'url': '/signup',
        'color': 'dark'
    }
}


my_blue = '#C8E4F4'

user_details = html.Div(id='user-details', style={'display': 'none'})

url = dcc.Location(id='url')

navbar = \
    dbc.Navbar(
        dbc.Row(
            [
                dbc.NavLink(
                    dbc.Button(
                        children=name.capitalize(),
                        id=name,
                        color=info['color'],
                        outline=True,
                        active=False,
                    ),
                    href=info['url'],
                    style={'padding': '5px'}
                )
                for name, info in page_names.items()
            ],
            style={'margin': 'auto'}
        ), 
        id='nav',
        style={'padding': '0px'}
    )

page = html.Div(id='page-content', style={'margin': '1rem'})

footer = \
    dbc.Col(
        [
            "Built by Jacob Maxfield with Dash.",
            html.Div(
                [
                    html.A(
                        dbc.Button(
                            "YouTube",
                            id='youtube',
                            color='danger',
                            outline=True,
                            size='sm'
                        ),
                        href="https://youtube.com/MaxTechniche",
                        style={'margin': '1%'}
                    ),
                    html.A(
                        dbc.Button(
                            "GitHub",
                            id='github',
                            color='dark',
                            outline=True,
                            size='sm'
                        ),
                        href="https://github.com/MaxTechniche",
                        style={'margin': '1%'}
                    ),
                ],
                style={'margin-top': '5px'}
            )
        ],
        style={'text-align': 'center', 'margin-bottom': '15px'}
    )

app.layout = dbc.Container(
    [
        user_details,
        url,
        navbar,
        page,
        footer
    ], 
    style={
        'word-wrap': 'break-word', 
        'position': 'relative', 
        'min-height': '95vh'
    }
)


@app.callback([
    Output('page-content', 'children')] + [Output(page_name, 'active') for page_name in page_names],
    [Input('url', 'pathname'),
    State('user-details', 'children')])
def display_page(pathname, user):
    print(user)
    path_actives = {name: False for name in page_names}
    if pathname == '/':
        path_actives['home'] = True
        return [home.layout] + list(path_actives.values())

    try:
        path_actives[f"{ pathname.replace('/', '') }"] = True
        return [globals()[f"{ pathname.replace('/', '') }"].layout] + list(path_actives.values())
    except KeyError:
        return 'Path not found.'

# @app.callback(
#     Output('user-details', 'children'),
#     Input('user-details', 'children')
# )
# def print_user(user):
#     print(user)
#     return user
