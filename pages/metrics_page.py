import dash
from dash import html, dcc
import plotly.io as pio
import pandas as pd
import plotly.graph_objects as go

dash.register_page(__name__, path='/')
crypto_name = 'apeusd'



ohlc_df = pd.read_csv('historical_price/' + crypto_name + '.csv')[-1000:]
ohlc_df.index = pd.to_datetime(ohlc_df['time'], unit = 'ms')
#ohlc_df.index = ohlc_df.index.tz_localize('UTC').tz_convert('US/Eastern')

#first_date = ohlc_df.iloc[0]['time']


#ohlc_df['time'] = pd.to_datetime(ohlc_df['time'], format = '%Y-%m-%d %H:%M', origin = first_date)
#ohlc_df = ohlc_df[~ohlc_df.index.duplicated(keep='first')]
ohlc_df = ohlc_df.resample('min').ffill()[1:]
print(ohlc_df.tail())
o = ohlc_df['open']
h = ohlc_df['high']
c = ohlc_df['close']
l = ohlc_df['low']

fig1 = go.Figure(data=go.Ohlc(x=ohlc_df.index.tolist(),
                                open=o,
                                high=h,
                                close=c,
                                low=l,
                                name='Crypto/Fiat Pair: ' + crypto_name)
)


layout = html.Div(children=[
    html.H1(children='Price Graphs'),

    html.Div(children='''
        The following figures depict information about the crypto/fiat pair of your choice.
    '''),
    dcc.Graph(figure = fig1)

])