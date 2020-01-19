from pyclustering.cluster.kmedians import kmedians
from timeit import default_timer as timer
import numpy as np


def compute_kmedians(data, k):
    indexes = [i for i in range(len(data))]
    chosen_indexes = np.random.choice(indexes, k)

    kmedians_instance = kmedians(data, chosen_indexes)

    start = timer()
    kmedians_instance.process()
    end = timer()

    clusters = kmedians_instance.get_clusters()

    seconds = end - start

    return clusters, [], seconds