import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Read the processed sales data from the CSV file
df = pd.read_csv('formatted_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Sales Data Visualizer"),
    dcc.Graph(id='sales-chart'),
])

@app.callback(
    Output('sales-chart', 'figure'),
    [Input('sales-chart', 'relayoutData')]
)
def update_sales_chart(relayoutData):
    global df
    # Sort the data by date
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date')

    # Create a line chart with Plotly Express
    fig = px.line(df, x='date', y='sales', labels={'date': 'Date', 'sales': 'Sales'})

    # Highlight the period before and after the price increase (January 15, 2021)
    if 'xaxis.range' in relayoutData:
        x_range = relayoutData['xaxis.range']
        price_increase_date = pd.Timestamp('2021-01-15')

        if x_range[0] < price_increase_date and x_range[1] > price_increase_date:
            fig.add_vline(x=price_increase_date, line_width=2, line_dash="dash", line_color="red", annotation_text="Price Increase")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
