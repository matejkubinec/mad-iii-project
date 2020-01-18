from pyclustering.cluster.kmedoids import kmedoids
from timeit import default_timer as timer
import numpy as np


def compute_kmedoids(data, k):
    indexes = [i for i in range(len(data))]
    chosen_indexes = np.random.choice(indexes, k)

    kmedoids_instance = kmedoids(data, chosen_indexes)

    start = timer()
    kmedoids_instance.process()
    end = timer()

    clusters = kmedoids_instance.get_clusters()

    medoids = kmedoids_instance.get_medoids()

    seconds = end - start

    return clusters, medoids, seconds