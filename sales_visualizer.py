import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Read the processed sales data from the CSV file
df = pd.read_csv('formatted_data.csv')

# Initialize the Dash app with external stylesheets
app = dash.Dash(__name__, external_stylesheets=['styles.css'])

# Define the layout of the app
app.layout = html.Div([
    html.H1("Sales Data Visualizer", className='header'),
    
    # Radio button container with horizontal layout
    html.Div([
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            labelStyle={'display': 'inline-block'},
            className='radio-button'
        ),
    ], className='radio-container'),

    dcc.Graph(id='sales-chart'),
], className='app-container')

# Define callback to update the chart based on selected region
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('sales-chart', 'relayoutData'), Input('region-filter', 'value')]
)
def update_sales_chart(relayoutData, selected_region):
    # Filter data based on the selected region
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Sort the data by date
    filtered_df['date'] = pd.to_datetime(filtered_df['date'])
    filtered_df = filtered_df.sort_values(by='date')

    # Create a line chart with Plotly Express
    fig = px.line(filtered_df, x='date', y='sales', labels={'date': 'Date', 'sales': 'Sales'})

    # Check if relayoutData is not None before accessing its properties
    if relayoutData and 'xaxis.range' in relayoutData:
        x_range = relayoutData['xaxis.range']
        price_increase_date = pd.Timestamp('2021-01-15')

        if x_range[0] < price_increase_date and x_range[1] > price_increase_date:
            fig.add_vline(x=price_increase_date, line_width=2, line_dash="dash", line_color="red", annotation_text="Price Increase")

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)