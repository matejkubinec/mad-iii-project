from load_labels import load_labels
from cleanup_dataset import cleanup_dataset
from tabulate import tabulate
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import os

base_path = os.path.dirname(os.path.realpath(__file__))
data_path = f'{base_path}/data/deepsolar_tract.csv'
df = pd.read_csv(data_path)
state_col = [st.upper() for st in df['state']]

df.drop(['fips', 'county', 'state', 'voting_2012_dem_win',
         'voting_2016_dem_win'], axis=1, inplace=True)
df = df.select_dtypes(exclude=['object', 'bool'])
df = cleanup_dataset(df)
df['labels'] = load_labels()

cols = [
    'labels',
    'solar_system_count',
    'number_of_solar_system_per_household',
    'avg_electricity_retail_rate',
    'electricity_consume_total'
]

names = [
    'Solar System Count',
    'Number Of Solar System Per Household',
    'Avg Electricity Retail Rate',
    'Electricity Consume Total'
]

attributes = [
    'solar_system_count',
    'number_of_solar_system_per_household',
    'avg_electricity_retail_rate',
    'electricity_consume_total'
]

for attr, name in zip(attributes, names):
    maximum = df[['labels', attr]].groupby(['labels']).max().reset_index()
    mean = df[['labels', attr]].groupby(['labels']).mean().reset_index()
    minimum = df[['labels', attr]].groupby(['labels']).min().reset_index()

    rows = []
    for cl in range(5):
        cl = str(cl)
        row = [
            cl,
            round(float(maximum.loc[maximum.labels == cl][attr]), 3),
            round(float(mean.loc[mean.labels == cl][attr]), 3),
            round(float(minimum.loc[mean.labels == cl][attr]), 3)
        ]
        rows.append(row)

    rows = sorted(rows, key=lambda r: r[0])

    headers = ['Cluster', attr + ': max', attr + ': mean', attr + ': min']
    table_str = tabulate(rows, headers=headers, tablefmt="github")

    with open(f'{base_path}/tables/{attr}.md', 'w') as f:
        f.write('# ' + name + '\n')
        f.write('\n')
        f.write(table_str)
