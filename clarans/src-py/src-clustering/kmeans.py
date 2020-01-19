from timeit import default_timer as timer
from sklearn.cluster import KMeans

def compute_kmeans(data, k):

    kmeans_instance = KMeans(k)

    start = timer()
    kmeans_instance.fit(data)
    end = timer()

    labels = kmeans_instance.labels_

    clusters = [[] for _ in range(k)]
    for i in range(len(data)):
        cl = labels[i]
        clusters[cl].append(i)

    seconds = end - start

    return clusters, [], seconds