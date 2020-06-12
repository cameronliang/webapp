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

def generate_table(table_array,max_rows=4):
    columns=['Recommended Price Multiplier', 'Original Revenue ($)', 'Projection ($)', 'Improvement Factor (%)']

    table = html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in columns])
        ),
        html.Tbody([
            html.Tr([html.Th(val) for val in table_array])
        ]),

    ]) 
    return table

# -----------------------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# -----------------------------------------------------------------------------
# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501

###############################################################################

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Your Amazon AnalyticS (YAAS)',
                        className='nine columns'),

                html.Div(children='''
                        Dashboard for Amazon Seller
                        ''',

                        className='nine columns'
                ),
                dcc.Dropdown(
                    id='my-dropdown',
                    options=[
                        {'label':'Product 1', 'value':'prod1'},
                        {'label':'Product 2', 'value':'prod2'},
                    ], className='six columns'
                ),
            ], className="row"
        ),

        # below for plots 
        html.Div(
            [
            html.Div([
                dcc.Graph(id='graph')
                ], className= 'six columns'
                ),

                html.Div([
                #generate_table(sample_df)
                html.Table(id='table')
                ], className= 'six columns'
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one')
)


###############################################################################

## create callback buttons
@app.callback(Output('graph','figure'),[Input('my-dropdown','value')])
def update_plot(input_value):
    df = ReadRevenueData(input_value)

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
            'title':'Cumulative Revenue',
            'xaxis':{
                'title':'Weeks'
            },
            'yaxis':{
                 'title':'Revenue'
            }
        }
    }
    return figure 

@app.callback(Output('table', 'children'), [Input('my-dropdown', 'value')])
def update_table(value):
    #dff = clean_data(global_df, value)
    sample_df = ReadRevenueData(value)

    # create function for generating output for table
    best_price = sample_df['best_price_changes'].iloc[-1]
    original_rev = sample_df['origin_revenue'].iloc[-1]
    best_rev = sample_df['best_revenue'].iloc[-1]
    improv_factor = (best_rev - original_rev)/original_rev
    table_array = np.array([round(best_price,2),round(original_rev,0),
                    round(best_rev,0),round(improv_factor*100,2)])

    #print(table_array)


    #dff = pd.DataFrame(data=table_array.T, columns=['Recommended Price', 'Original Revenue', 'Projection', 'Improvement Factor'])

    table = generate_table(table_array)
    
    return table



if __name__ == '__main__':
    app.run_server(debug=True)