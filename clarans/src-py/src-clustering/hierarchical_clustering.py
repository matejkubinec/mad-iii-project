from timeit import default_timer as timer
from sklearn.cluster import AgglomerativeClustering

def compute_agglomerative_clustering(data, k):

    # ward linkage
    agglomerative_instance = AgglomerativeClustering(k)

    start = timer()
    agglomerative_instance.fit(data)
    end = timer()

    labels = agglomerative_instance.labels_

    clusters = [[] for _ in range(k)]
    for i in range(len(data)):
        cl = labels[i]
        clusters[cl].append(i)

    seconds = end - start

    return clusters, [], seconds