# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go

import numpy as np
import pandas as pd


# -----------------------------------------------------------------------------
# Read data and predictions from model. 
my_sample_data = np.random.random_sample(([100,3]))
df = pd.DataFrame(my_sample_data,columns=['val1','val2','val3'])

# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# -----------------------------------------------------------------------------

###############################################################################


app.layout = html.Div(children=[
    html.H1(
        children='Your Amazon AnalyticS (YAAS)',
        style={'textAlign':'center'}
    ),

    html.Div(children='Dash: A web application framework for Python.', 
        style={'textAlign':'center'}
        ),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label':'Product1', 'value':'p1'},
            {'label':'Product2', 'value':'p2'},
            {'label':'Product3', 'value':'p3'},
        ]
    ),

    #dcc.Markdown(children=markdown_text),
    dcc.Graph(
        id='example-graph',
        figure={ # figure command is the same as plotly
            'data': [
                {'x': [1, 2, 3], 'y': [4, 4, 2],  'name': 'SF'},
            ],
        }
    )
])

###############################################################################



if __name__ == '__main__':
    app.run_server(debug=True)