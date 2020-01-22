from importlib import reload
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster.birch import Birch
from sklearn.metrics import silhouette_score, davies_bouldin_score
import attributes as at
import plot_helper as ph
import pandas as pd
import os

#
# Subset of Attributes
# 
attributes = at.attributes
columns = [a['col'] for a in attributes]
names = [a['name'] for a in attributes]

base_path = '.'
df = pd.read_csv(f'{base_path}/data/deepsolar_tract.csv', index_col=0)
df = df[columns]

#
# NaN Count
#
nan_count = df.isnull().any(axis=1).sum()
print(nan_count)
print(len(df))
df.dropna(inplace=True)
print(len(df))

#
# Group By FIPS
#
df = df.groupby(['state', 'fips']).mean().reset_index()

#
# Maps
#
map_attributes = list(filter(lambda a: a['col'] in ['solar_system_count', 'total_panel_area', 'frost_days'], attributes))
for ma in map_attributes:
    col = ma['col']
    name = ma['name']
    map_df = df[['state', col]].groupby(['state']).sum().reset_index()
    locations = list(map(str.upper, map_df['state']))
    z = map_df[col]

    ph.plot_us_map(
        locations,
        z,
        'viridis',
        name,
        name + ' by State',
        '/maps/' + col + '_by_state'
    )

#     map_df = df[['fips', col]].groupby(['fips']).sum().reset_index()
#     fips = [int(str(f)[:-6]) for f in map_df['fips']]
#     values = map_df[col]

#     ph.plot_fips(
#         fips,
#         values,
#         name,
#         name + ' by State',
#         '/maps/' + col + '_by_fips'
#     )

#
# Histograms
#
hist_attributes = list(filter(lambda a: a['col'] not in ['state', 'fips'], attributes))
for ha in hist_attributes:
    col = ha['col']
    name = ha['name']

    ph.plot_hist(
        df[[col]],
        50,
        col,
        dict([(col, name)]),
        '/hist/' + col
    )

#
# Box Plots
#
box_plots_attributes = list(filter(lambda a: a['col'] not in ['state', 'fips'], attributes))
for bp in box_plots_attributes:
    col = bp['col']
    name = bp['name']
    ph.plot_box_plot(df[col], col, dict([(col, name)]), './box/' + col)

df.to_csv('data/data_to_cluster.csv')