# https://en.wikipedia.org/wiki/Dunn_index
from utils import euclidean_distance, maximal_intra_distance, get_centroid

def dunn_index(clusters):
    n = len(clusters)

    min_inter_dist = None
    max_intra_dist = None

    for i in range(n):
        for j in range(n):
            
            if i == j:
                continue

            cl_i = clusters[i]
            cl_j = clusters[j]

            c_i = get_centroid(cl_i)
            c_j = get_centroid(cl_j)

            dist = euclidean_distance(c_i, c_j)

            if min_inter_dist is None:
                min_inter_dist = dist
            elif dist < min_inter_dist:
                min_inter_dist = dist

    for c in clusters:
        intra_dist = maximal_intra_distance(c)

        if max_intra_dist is None:
            max_intra_dist = intra_dist
        elif intra_dist > max_intra_dist:
            max_intra_dist = intra_dist

    return min_inter_dist / max_intra_dist
