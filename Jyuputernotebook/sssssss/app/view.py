
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime

from .assets.database import db_session
from .assets.models import Data

df = pd.read_csv('assets/data.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()

dates = []
subscribers = []
reviews = []

for datum in data:
    data.append(datum.data)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)

diff_subscribers = pd.Series(subscribers).diff().values
diff_reviews = pd.Series(reviews).diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.h2(children='スクレイピング練習'),
    html.Div(children=[
        dcc.Graph(
            id='subscriner_graph',
            figure={
                'date': [
                    go.Scatter(
                        x=dates,
                        y=subscribers,
                        mode='lines+markers',
                        name='受講生総数',
                        opacity=0.7,
                        yaxis='y1'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,
                        name='増加人数',
                        yaxis='y2'
                    )
                ],
                'layout':go.Layout(
                    title='受講生総数の推移',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='受講生総数', side='left', showgrid=False,
                               range=[2500, max(subscribers) + 100]),
                    yaxis2=dict(title='増加人数', side='right', overlaying='y', showgrid=False,
                                range=[0, max(diff_subscribers[1:])]),
                    mergin=dict(
                        l=200, r=100, b=100, t=100)
                )
            }
        ),
        dcc.Graph(
            id='review_graph',
            figure={
                'date': [
                    go.Scatter(
                        x=dates,
                        y=reviews,
                        mode='lines+markers',
                        name='レビュー総数',
                        opacity=0.7,
                        yaxis='y1'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_reviews,
                        name='増加数',
                        yaxis='y2'
                    )
                ],
                'layout':go.Layout(
                    title='レビュー総数の推移',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='レビュー総数', side='left', showgrid=False,
                               range=[2500, max(reviews) + 10]),
                    yaxis2=dict(title='増加数', side='right', overlaying='y', showgrid=False,
                                range=[0, max(diff_reviews[1:])]),
                    mergin=dict(
                        l=200, r=100, b=100, t=100)
                )
            }
        )
    ])
], style={
    'textAlign': 'center',
    'width': '1200px',
    'margin': '0 auto'
})

if __name__ == '__main__':
    app.run_server(debug=True)
