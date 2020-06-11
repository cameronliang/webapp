# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# -----------------------------------------------------------------------------


def ReadRevenueData(product_id):
    # Load Data 
    fname = '../cleaned_data/simulations/reveune.csv'
    df = pd.read_csv(fname)
    df = df.loc[df['product_id'] == product_id]
    #time = np.arange(1,len(df['origin_revenue']),1)
    return df

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

    html.Div(children='Predicting the Demand of your product', 
        style={'textAlign':'center'}
        ),

    #dcc.Input(id='input',value='Enter product ID', type='text'),
    #html.Div(id='output'),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label':'Product 1', 'value':'prod1'},
            {'label':'Product 2', 'value':'prod2'},
            #{'label':'Product 3', 'value':'prod3'},
        ]
    ),

    dcc.Graph(id='graph')
])

###############################################################################

## create callback buttons
@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='my-dropdown', component_property='value')]
    )

def update_plot(input_value):
    df = ReadRevenueData(input_value)
    #if input_value == 1:
    #    my_data_y1 = df['origin_revenue']
    #    my_data_y2 = df['best_revenue']
    #else:
    #    my_data_y1 = np.ones_like(df['origin_revenue'])
    #    my_data_y2 = np.ones_like(df['origin_revenue'])
    figure = {
        'data':[
            {
                'x': df['time'], 
                'y': df['origin_revenue'],
                'type':'line',
                'name':'Original Revenue'
            },
            {
                'x': df['time'], 
                'y': df['best_revenue'],
                'type':'line',
                'name':'Optimized Revenue'
            }
        ], 
        'layout':{
            'title': 'Cumulative Revenue'
            #'xaxis_title':"x Axis Title",
        }
    }
    
    return figure 

if __name__ == '__main__':
    app.run_server(debug=True)