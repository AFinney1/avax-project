import dash
import dash_html_components as html
import dash_core_components as dcc
from matplotlib.pyplot import figure
import pandas as pd
#adaimport plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

app = dash.Dash(__name__, use_pages = True)
#crypto_name = input('Please enter the crypto/fiat pair of your choice: (ada/usd -> adausd): ')
crypto_name = 'apeusd'



app.layout = html.Div([
	html.H1('Multi-page Crypto/Fiat Dashboard: Metrics and Forcasting'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])



app.run_server(debug=True)
