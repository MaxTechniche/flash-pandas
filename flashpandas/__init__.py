
from .app import create_app
from .pages import home, learn, test, login, signup


from pprint import pprint

import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Button import Button
from dash_bootstrap_components._components.NavLink import NavLink
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

# from .dbmodels import DB, User

app = create_app()
server = app.server

page_names = {
    'learn': {
        'url': '/learn', 
        'button': {
            'color': 'warning',
            'outline': True,
        }
    },
    'home': {
        'url': '/', 
        'button': {
            'color': 'success',
            'outline': True,
        }
    },
    'test': {
        'url': '/test', 
        'button': {
            'color': 'primary',
            'outline': True,
        }
    }
}

my_blue = '#C8E4F4'

url = dcc.Location(id='url')

navbar = \
    dbc.Navbar(
        [
            dbc.Row(
                [
                    dbc.NavLink(
                        dbc.Button(
                            children=f"{name.capitalize()}", 
                            id=f"{name}",
                            color=info['button']['color'],
                            outline=info['button']['outline'],
                            active=False
                        ),
                        href=info['url'],
                        style={'margin': '0px', 'padding': '5px'}
                    ) 
                    for name, info in page_names.items()
                ], 
                style={'margin': 'auto'}
            ),
            # dbc.Row(
            #     [
            #         dbc.NavLink(
            #             dbc.Button(
            #                 children="Login",
            #                 id='login',
            #                 color='info',
            #                 outline=True
            #             ),
            #             href='/login',
            #         ),
            #         dbc.NavLink(
            #             dbc.Button(
            #                 children="Sign Up",
            #                 id='signup',
            #                 color='link',
            #                 outline=True
            #             ),
            #             href='/signup'
            #         )
            #     ]
            # )
        ], 
        id='nav',
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
    Output('page-content', 'children')] + [
    Output(page_name, 'active') for page_name in page_names],
    Input('url', 'pathname'))
def display_page(pathname):
    # DB.drop_all()
    # DB.create_all()
    path_actives = {name: False for name in page_names}
    if pathname == '/':
        path_actives['home'] = True
        return [home.layout] + list(path_actives.values())

    try:
        path_actives[f"{ pathname.replace('/', '') }"] = True
        return [globals()[f"{ pathname.replace('/', '') }"].layout] + list(path_actives.values())
    except KeyError:
        return 'Path not found.'

