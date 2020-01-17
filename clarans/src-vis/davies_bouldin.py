from utils import euclidean_distance, get_average_distance, get_centroid

# https://en.wikipedia.org/wiki/Davies%E2%80%93Bouldin_index
def davies_bouldin(medoids, clusters):
    n = len(clusters)
    db = 0
    
    for i in range(n):
        for j in range(n):

            if i == j:
                continue

            cl_i = clusters[i]
            cl_j = clusters[j]

            c_i = get_centroid(cl_i)
            c_j = get_centroid(cl_j)

            d_i = get_average_distance(cl_i, c_i)
            d_j = get_average_distance(cl_j, c_j)

            d = euclidean_distance(c_i, c_j)

            # TODO: davies_boulding


    pass