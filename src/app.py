'''
File: app.py
File Created: 2020-07-25
Author: Parijat Khan (khanparijat@gmail.com)
-----
Copyright 2020 Parijat Khan
'''

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from floorplan import makeplan

st.title('Mall-monitor by <A-Team>')

fig = go.Figure()

makeplan(fig)

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40, 60, 20, 10, 5]

fig.add_trace(go.Scatter(
    x=[10, 10, 10, 40, 70, 97, 97, 90, 63, 30, 40, 40, 70, 70],
    y=[10, 25, 40, 45, 45, 40, 20, 5, 5, 5, 20, 30, 20, 30],
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4
    )
))

fig.update_shapes(dict(xref='x', yref='y'))

fig.update_layout(
    autosize=False,
    width=735,
    height=350,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    showlegend=False
)

st.plotly_chart(fig)

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)

