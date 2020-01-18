import json
from clarans import compute_clarans
from kmedoids import compute_kmedoids
from kmeans import compute_kmeans
from kmedians import compute_kmedians
from spectral_clustering import compute_spectral_clustering
from hierarchical_clustering import compute_agglomerative_clustering

def load_data(file_path):
    data = []
    lines = []

    with open(file_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        values = []

        for value in line.split(" "):

            if value == '':
                continue

            values.append(float(value))

        data.append(values)

    return data


def save_results(clusters, medoids, seconds, data, name, filename):
    clusters_data = []
    for cl in clusters:
        cl_data = []

        for item in cl:
            cl_data.append(data[item])

        clusters_data.append(cl_data)

    medoids_data = []
    for medoid in medoids:
        medoids_data.append(data[medoid])

    data = {
        'clusters': clusters_data,
        'medoids': medoids_data,
        'seconds': seconds,
        'name': name
    }

    json_str = json.dumps(data)

    with open(f'../results/{filename}.json', 'w') as f:
        f.write(json_str)


if __name__ == "__main__":
    datasets = [
        '../data/iris.txt',
        '../data/wine.txt',
        '../data/breast.txt',
        '../data/yeast.txt'
    ]
    file_path = datasets[0]
    data = load_data(file_path)
    
    k = 5

    # Clarans
    max_neighbour = 5
    num_local = 5

    filename = 'pyclustering-results'
    name = 'PyClustering - Clarans'
    clusters, medoids, seconds = compute_clarans(data, k, max_neighbour, num_local)
    save_results(clusters, medoids, seconds, data, name, filename)

    filename = 'kmedoids-results'
    name = 'KMedoids'
    clusters, medoids, seconds = compute_kmedoids(data, k)
    save_results(clusters, medoids, seconds, data, name, filename)
    
    filename = 'kmeans-results'
    name = 'KMeans'
    clusters, medoids, seconds = compute_kmeans(data, k)
    save_results(clusters, medoids, seconds, data, name, filename)

    # filename = 'kmedians-results'
    # name = 'KMedians'
    # clusters, medoids, seconds = compute_kmedians(data, k)
    # save_results(clusters, medoids, seconds, data, name, filename)

    filename = 'agglomerative-clustering-results'
    name = 'Hierarchical Clustering - Agglomerative'
    clusters, medoids, seconds = compute_agglomerative_clustering(data, k)
    save_results(clusters, medoids, seconds, data, name, filename)

    filename = 'spectral-clustering-results'
    name = 'Spectral Clustering'
    clusters, medoids, seconds = compute_spectral_clustering(data, k)
    save_results(clusters, medoids, seconds, data, name, filename)
