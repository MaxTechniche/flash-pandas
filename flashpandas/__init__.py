
from flask.globals import current_app
from .app import APP, users, questions
from .pages import home, learn, test, login, signup, search, create, signout, account


from pprint import pprint

from flask import session
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

# Use in future when you have access to larger SQL storage
# from .dbmodels import DB, users, questions

app = APP
server = app.server

logged_in_pages = {
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
    'account': {
        'url': '/account',
        'color': 'info'
    },
    'signout': {
        'url': '/signout',
        'color': 'dark'
    }
}

logged_out_pages = {
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



logged_in_navbar = \
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
            for name, info in logged_in_pages.items()
        ],
        style={'margin': 'auto'}
    )


logged_out_navbar = \
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
            for name, info in logged_out_pages.items()
        ],
        style={'margin': 'auto'}
    )
    

navbar = \
    dbc.Navbar(
        children=logged_out_navbar,
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
    Output('nav', 'children'), 
    Output('page-content', 'children')],
    Input('url', 'pathname'))
def display_page(pathname):
    # print(session.get('username', None))
    if session.get('username', None):
        path_actives = {name: False for name in logged_in_pages}
        current_pages = logged_in_pages
    else:
        path_actives = {name: False for name in logged_out_pages}
        current_pages = logged_out_pages



    if pathname == '/':
        path_actives['home'] = True
        current_nav = get_nav(current_pages, path_actives)
        return [current_nav] + [home.layout]

    if pathname == '/login':
        path_actives['login'] = True
        current_nav = get_nav(current_pages, path_actives)
        if session.get('username', None):
            return [current_nav] + [login.logged_in_layout]
        else:
            return [current_nav] + [login.logged_out_layout]


    if pathname == '/signup':
        path_actives["signup"] = True
        current_nav = get_nav(current_pages, path_actives)
        return [current_nav] + [signup.layout]


    if pathname in ['/signout', '/logout']:
        session.pop('username', None)
        path_actives['signout'] = True
        current_nav = get_nav(current_pages, path_actives)
        return [current_nav] + [signout.layout]


    try:
        path_actives[f"{ pathname.replace('/', '') }"] = True
        current_nav = get_nav(current_pages, path_actives)
        return [current_nav] + [globals()[f"{ pathname.replace('/', '') }"].layout]
    except KeyError:
        current_nav = get_nav(current_pages, path_actives)
        return [current_nav] + 'Path not found.'


def get_nav(pages, paths):

    return dbc.Row(
        [        
            dbc.NavLink(
                dbc.Button(
                    children=name.capitalize(),
                    id=name,
                    color=info['color'],
                    outline=True,
                    active=paths[name],
                ),
                href=info['url'],
                style={'padding': '5px'}
            )
            for name, info in pages.items()
        ],
        style={'margin': 'auto'}
    )


# @app.callback(
#     Output('user-details', 'children'),
#     Input('user-details', 'children')
# )
# def print_user(user):
#     print(user)
#     return user
