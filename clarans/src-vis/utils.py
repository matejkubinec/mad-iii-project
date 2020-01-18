import math

def maximal_intra_distance(cluster):
    min_c = min(cluster)
    max_c = max(cluster)
    return euclidean_distance(min_c, max_c)

def euclidean_distance(element_1, element_2):
    dist = 0

    for e1, e2 in zip(element_1, element_2):
        dist += (e1 - e2) ** 2

    return math.sqrt(dist)

def list_add(list1, list2):
    
    if len(list1) != len(list2):
        raise Exception("List must have the same length.")

    res = []

    for l1, l2 in zip(list1, list2):
        
        res.append(l1 + l2)

    return res

def get_centroid(cluster):
    k = len(cluster)
    centroid = None

    for c in cluster:
        
        if centroid is None:
            centroid = c
        else:
            centroid = list_add(centroid, c)

    return list(map(lambda c: c / k, centroid))

def get_average_distance(cluster, centroid):
    distances = []

    for c in cluster:
        dist = euclidean_distance(centroid, c)
        distances.append(dist)

    return sum(distances) / len(distances)

def labelize_clusters(clusters):
    items = []
    labels = []

    l = 0
    for c in clusters:
    
        for v in c:
            items.append(v)
            labels.append(l)
    
        l += 1

    return items, labels


if __name__ == "__main__":
    a1 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    a2 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    a1a2 = [4, 4, 4, 4, 4, 4, 4, 4, 4]
    c = [2, 2, 2, 2, 2, 2, 2, 2, 2]

    assert a1a2 == list_add(a1, a2)

    assert c == get_centroid([a1, a2])

    assert 3 == get_average_distance([a1, a2], c)