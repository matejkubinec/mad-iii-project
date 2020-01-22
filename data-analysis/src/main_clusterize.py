from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import attributes as at
import pandas as pd
import os

base_path = '.'
base_path = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(f'{base_path}/data/data_to_cluster.csv', index_col=False)

df.drop(['state', 'fips'], axis=1, inplace=True)

for k in range(2, 11):
    print(k)
    kmeans_instance = KMeans(n_clusters=k)
    kmeans_instance.fit(df)
    labels = kmeans_instance.labels_

    s_score = silhouette_score(df, labels)
    db_score = davies_bouldin_score(df, labels)

    with open('./data/cluster_scores.txt', 'a+') as f:
        f.write(f'{k} {s_score} {db_score};')

    with open(f'./data/clustering/{k}.txt', 'w') as f:
        f.write(' '.join([str(l) for l in labels]))

    print(str(k) + ': ok')