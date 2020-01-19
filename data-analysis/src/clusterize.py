import plotly.figure_factory as ff
import plotly.graph_objects as go
from sklearn.cluster import Birch
import pandas as pd
import numpy as np
import os


def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin(['', np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


base_path = os.path.dirname(os.path.realpath(__file__))
data_path = f'{base_path}/data/deepsolar_tract.csv'
df = pd.read_csv(data_path)

df.drop(['fips', 'county', 'state', 'voting_2012_dem_win',
         'voting_2016_dem_win'], axis=1, inplace=True)

df = df.select_dtypes(exclude=['object', 'bool'])
df = clean_dataset(df)

cols = [
    'solar_system_count',
    'number_of_solar_system_per_household',
    'avg_electricity_retail_rate',
    'electricity_consume_total',
    'education_less_than_high_school_rate',
    'education_high_school_graduate_rate',
    'education_college_rate',
    'education_bachelor_rate',
    'education_master_rate',
    'education_professional_school_rate',
    'education_doctoral_rate'
]

data_df = df[cols]

birch_instance = Birch(n_clusters=5)

fitted = birch_instance.fit(data_df)

labels = fitted.labels_
labels = [str(l) for l in labels]
labels_str = ' '.join(labels)

with open(f'{base_path}/data/birch_5_labels.txt', 'w') as f:
    f.write(labels_str)
