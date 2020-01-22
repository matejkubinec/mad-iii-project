import plot_helper as ph
import attributes as at
import pandas as pd

#
# Plot Scores
#
k_list = []
silhouette = []
davies_bouldin = []
with open('./data/cluster_scores.txt', 'r') as file:
    line = file.readline()

    for score in line.split(';'):
        values = score.split(' ')

        if len(values) == 3:
            k, s, db = values

            k_list.append(k)
            silhouette.append(s)
            davies_bouldin.append(db)

scores_df = pd.DataFrame()
scores_df['k'] = k_list
scores_df['silhouette'] = silhouette
scores_df['davies_bouldin'] = davies_bouldin
ph.plot_line(scores_df, 'k', 'silhouette', 'Silhouette Score', '/clustering_evaluation/silhouette_coefficient')
ph.plot_line(scores_df, 'k', 'davies_bouldin', 'Davies Bouldin', '/clustering_evaluation/davies_bouldin')

#
# Load Data
#
k = 5
with open(f'./data/clustering/{k}.txt', 'r') as f: 
    labels = f.readline().split(' ')
cl_df = pd.read_csv('./data/data_to_cluster.csv', index_col=0)
cl_df['labels'] = labels

cl_df.sort_values(by=['electricity_consume_total'])

#
# Plot Maps
#
cl_us_map_df = cl_df[['state', 'labels']]
cl_us_map_df = cl_us_map_df.groupby(['state'])
cl_us_map_df = cl_us_map_df.agg(lambda x: x.value_counts().index[0])
cl_us_map_df = cl_us_map_df.reset_index()
ph.plot_us_map(
    [s.upper() for s in cl_us_map_df['state']],
    cl_us_map_df['labels'],
    'viridis',
    'Cluster',
    'States by Cluster',
    '/maps/states_cluster'
)

cl_fips_map_df = cl_df[['fips', 'labels']]
cl_fips_map_df = cl_fips_map_df.groupby(['fips'])
cl_fips_map_df = cl_fips_map_df.agg(lambda x: x.value_counts().index[0])
cl_fips_map_df = cl_fips_map_df.reset_index()
ph.plot_fips(
    [int(str(f)[:-6]) for f in cl_fips_map_df['fips']],
    cl_fips_map_df['labels'],
    'Cluster',
    'Counties by Cluster',
    '/maps/counties_cluster'
)

#
# Plot Bar
#
cols = filter(lambda c: c['col'] not in ['state', 'fips'], at.attributes)
cols = list(cols)

for col in cols:
    attr = col['col']
    name = col['name']
    bar_df = cl_df[['labels', attr]]
    bar_df = bar_df.groupby(['labels'])
    bar_df = bar_df.mean()
    bar_df = bar_df.reset_index()
    bar_df['labels'] = [int(l) for l in bar_df['labels']]
    ph.plot_bar(bar_df, 'labels', attr, 'Average: ' + name, 'labels', '/clustering_bar/' + attr)