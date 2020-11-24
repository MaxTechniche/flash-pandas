import random

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

layout = html.Div(
    [
        dcc.Markdown(
            """
            ## Flash Pandas
            Flash Pandas is a website designed to help those interested in learning and/or testing their knowledge of Data Science concepts and technical problems.""",
            style={'text-align': 'center'}
        )
    ]
)
