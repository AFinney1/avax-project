import dash
from dash import html, dcc


with open('LSTM_figures/lstm_page.html', 'r') as f:
    lstm_page_html = f.read()


dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='This is our LSTM page'),

    html.Div(children='''
        This is our LSTM page content.
    '''),

])