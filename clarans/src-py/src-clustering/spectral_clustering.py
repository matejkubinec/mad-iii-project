from timeit import default_timer as timer
from sklearn.cluster import SpectralClustering

def compute_spectral_clustering(data, k):

    spectral_instance = SpectralClustering(k)

    start = timer()
    spectral_instance.fit(data)
    end = timer()

    labels = spectral_instance.labels_

    clusters = [[] for _ in range(k)]
    for i in range(len(data)):
        cl = labels[i]
        clusters[cl].append(i)

    seconds = end - start

    return clusters, [], seconds