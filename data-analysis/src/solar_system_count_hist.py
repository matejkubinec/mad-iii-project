import plotly.express as px
import pandas as pd
import os

base_path = os.path.dirname(os.path.realpath(__file__))
data_path = f'{base_path}/data/deepsolar_tract.csv'
df = pd.read_csv(data_path)

st_cols = [df['state'], df['solar_system_count']]
st_keys = ['state', 'solar_system_count']
st_df = pd.concat(st_cols, axis=1, keys=st_keys)

st_sum = st_df.groupby(['state']).sum().reset_index()

fig = px.histogram(st_sum, x='solar_system_count', labels={'solar_system_count': 'Solar System Count'})
# fig.show()

fig.write_image(f'{base_path}/images/solar_system_count_hist.jpg')
