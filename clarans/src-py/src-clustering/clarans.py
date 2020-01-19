from pyclustering.cluster.clarans import clarans
from timeit import default_timer as timer

def compute_clarans(data, k, max_neighbour, num_local):
    
    clarans_instance = clarans(data, k, num_local, max_neighbour)

    start = timer()
    clarans_instance.process()
    end = timer()

    clusters = clarans_instance.get_clusters()

    medoids = clarans_instance.get_medoids()

    seconds = end - start

    return clusters, medoids, seconds