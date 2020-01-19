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
labels = load_labels()
# indexes = list(df.iloc[:, 0])

cols = [
    'labels',
    'solar_system_count',
    'education_less_than_high_school_rate',
    'education_high_school_graduate_rate',
    'education_college_rate',
    'education_bachelor_rate',
    'education_master_rate',
    'education_professional_school_rate',
    'education_doctoral_rate'
]


df['labels'] = labels
education_df = df[cols]

l = list(education_df['labels'])

less_highschool = education_df[['labels', 'education_less_than_high_school_rate']].groupby(['labels']).mean().reset_index()
high_school = education_df[['labels', 'education_high_school_graduate_rate']].groupby(['labels']).mean().reset_index()
college = education_df[['labels', 'education_college_rate']].groupby(['labels']).mean().reset_index()
bachelor = education_df[['labels', 'education_bachelor_rate']].groupby(['labels']).mean().reset_index()
master = education_df[['labels', 'education_master_rate']].groupby(['labels']).mean().reset_index()
professional_school = education_df[['labels', 'education_professional_school_rate']].groupby(['labels']).mean().reset_index()
doctoral = education_df[['labels', 'education_doctoral_rate']].groupby(['labels']).mean().reset_index()
solar_count = education_df[['labels', 'solar_system_count']].groupby(['labels']).mean().reset_index()

table_str = ''

val_loc = list(less_highschool['labels'])
val = round(float(less_highschool.loc[less_highschool['labels'] == '0']['education_less_than_high_school_rate']), 3)

rows = []
for cl in range(5):
    cl = str(cl)
    row = [
        cl,
        round(float(less_highschool.loc[less_highschool['labels'] == cl]['education_less_than_high_school_rate']), 3),
        round(float(high_school.loc[high_school['labels'] == cl]['education_high_school_graduate_rate']), 3),
        round(float(college.loc[college['labels'] == cl]['education_college_rate']), 3),
        round(float(bachelor.loc[bachelor['labels'] == cl]['education_bachelor_rate']), 3),
        round(float(master.loc[master['labels'] == cl]['education_master_rate']), 3),
        round(float(professional_school.loc[professional_school['labels'] == cl]['education_professional_school_rate']), 3),
        round(float(doctoral.loc[doctoral['labels'] == cl]['education_doctoral_rate']), 3),
        round(float(solar_count.loc[solar_count['labels'] == cl]['solar_system_count']), 3)
    ]
    rows.append(row)

rows = sorted(rows, key=lambda r: r[len(r) - 1], reverse=True)

headers = ['Cluster', 'Less Highschool', 'High School', 'College', 'Bachelor', 'Master', 'Professional', 'Doctoral', 'Solar Count']
table_str = tabulate(rows, headers=headers, tablefmt="github")

with open(f'{base_path}/tables/cluster_education.md', 'w') as f:
    f.write(table_str)
