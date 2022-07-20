import dash
from dash import html, dcc
import plotly.io as pio

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


with open('LSTM_figures/test_predictions_apeusd.json', 'r') as f:
    predictions = pio.from_json(f.read())

with open('LSTM_figures/Forecast_apeusd.json', 'r') as f:
    forecast = pio.from_json(f.read())



# predictions.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

# forecast.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='Long Short Term Memory (LSTM) Forecast'),
    html.H1('', style={'background-image': 'url(https://upload.wikimedia.org/wikipedia/commons/2/22/North_Star_-_invitation_background.png)'}),

    html.Div(children='''
        This is a demo of the LSTM forecasting algorithm.
    '''),

    dcc.Graph(figure = predictions),
    dcc.Graph(figure = forecast)

])