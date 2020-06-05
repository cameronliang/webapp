# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# -----------------------------------------------------------------------------

#def data_generator():
    # Read data and predictions from model. 
#    data_x = np.linspace(1,12,200)
#    data_y = np.sin(data_x)
#    sample_data =np.array([data_x,data_y])

#    return sample_data
# -----------------------------------------------------------------------------

#def fig_generator(sample_data):
#    import plotly.graph_objects as go
#    data_x,data_y = sample_data 
#    plot_data = go.scatter(x=data_x, y=data_y)
#    plot_layout = go.Layout(title='projection')

#    fig = go.Figure(data = plot_data)
#    return (fig.data,fig.layout)

# Load Data 
fname = '../model_prediction/model_prediction.csv'
data_x,data_y = np.loadtxt(fname,unpack=True,skiprows=1,delimiter=',')
#data_y = np.sin(data_x)
#sample_data = np.array([data_x,data_y])


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

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label':'Product1', 'value':1},
            {'label':'Product2', 'value':2},
            {'label':'Product3', 'value':3},
        ]
    ),

    dcc.Graph(id='graph')
])

###############################################################################

## create callback buttons
@app.callback(
    Output('graph', 'figure'),
    [Input('my-dropdown', 'value')])

def update_plot(input_value):
    if input_value == 1:
        my_data_y = data_y
    else:
        my_data_y = np.ones_like(data_y)
    figure = {
        'data':[
            {
                'x': data_x, 
                'y': my_data_y
            }
        ]
    }
    
    return figure 

if __name__ == '__main__':
    app.run_server(debug=True)