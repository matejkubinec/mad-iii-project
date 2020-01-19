import plotly.figure_factory as ff
import plotly.graph_objects as go

import pandas as pd
import os

base_path = os.path.dirname(os.path.realpath(__file__))
data_path = f'{base_path}/data/deepsolar_tract.csv'
df = pd.read_csv(data_path)

st_cols = [df['state'], df['solar_system_count']]
st_keys = ['state', 'solar_system_count']
st_df = pd.concat(st_cols, axis=1, keys=st_keys)

st_sum = st_df.groupby(['state']).sum().reset_index()
locations = [st.upper() for st in st_sum['state']]
z = list(st_sum['solar_system_count'])

fig = go.Figure(data=go.Choropleth(
    locations=locations,
    z=z,
    text='z',
    locationmode='USA-states',
    colorscale='Blues',
    colorbar_title="Solar Systems",
))

fig.update_layout(
    title_text='Solar System Count by State',
    geo_scope='usa',
)

# fig.show()
# fig.write_image(f'{base_path}/images/state_solar_sum.jpg')

st_df = st_df[st_df.state != 'ca']
st_df = st_df[st_df.state != 'fl']
st_df = st_df[st_df.state != 'az']

st_sum = st_df.groupby(['state']).sum().reset_index()
locations = [st.upper() for st in st_sum['state']]
z = list(st_sum['solar_system_count'])

fig = go.Figure(data=go.Choropleth(
    locations=locations,
    z=z,
    text='z',
    locationmode='USA-states',
    colorscale='Blues',
    colorbar_title="Solar Systems",
))

fig.update_layout(
    title_text='Solar System Count by State',
    geo_scope='usa',
)

# fig.show()
fig.write_image(f'{base_path}/images/state_solar_sum_cleaned.jpg')


