import dash
import dash_html_components as html
import dash_core_components as dcc
from matplotlib.pyplot import figure
import pandas as pd
#adaimport plotly.express as px
import plotly.graph_objects as go

app = dash.Dash()
#crypto_name = input('Please enter the crypto/fiat pair of your choice: (ada/usd -> adausd): ')
crypto_name = 'apeusd'


ohlc_df = pd.read_csv('historical_price/' + crypto_name + '.csv')[:100]
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

#ohlc_df.set_index('time', inplace=True)

fig = go.Figure(data=go.Ohlc(x=ohlc_df.index.tolist(),
                                open=o,
                                high=h,
                                close=c,
                                low=l,
                                name='Crypto/Fiat Pair: ' + crypto_name)
)


app.layout = html.Div(children=[
    html.H1(children='Crypto Metrics Dashboard'),
    html.Div(children = '''
        This is a dashboard for crypto metrics.
        '''),

    dcc.Graph(figure = fig)    


])

app.run_server(debug=True)
