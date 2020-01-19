import json
from clarans import compute_clarans
from kmedoids import compute_kmedoids
from kmeans import compute_kmeans
from kmedians import compute_kmedians
from spectral_clustering import compute_spectral_clustering
from hierarchical_clustering import compute_agglomerative_clustering
from utils import load_data, save_results


def iris():
    dataset = "iris"
    file_path = '../../data/iris.txt'
    data = load_data(file_path)
    k = 3

    # Clarans
    max_neighbour = 3
    num_local = 10

    filename = 'pyclustering-results'
    name = 'PyClustering - Clarans'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_clarans(
        data, k, max_neighbour, num_local)
    save_results("iris", clusters, medoids, seconds, data, name, filename)

    filename = 'kmedoids-results'
    name = 'KMedoids'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_kmedoids(data, k)
    save_results("iris", clusters, medoids, seconds, data, name, filename)

    filename = 'kmeans-results'
    name = 'KMeans'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_kmeans(data, k)
    save_results("iris", clusters, medoids, seconds, data, name, filename)

    filename = 'agglomerative-clustering-results'
    name = 'Hierarchical Clustering - Agglomerative'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_agglomerative_clustering(data, k)
    save_results("iris", clusters, medoids, seconds, data, name, filename)

    filename = 'spectral-clustering-results'
    name = 'Spectral Clustering'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_spectral_clustering(data, k)
    save_results("iris", clusters, medoids, seconds, data, name, filename)


def wine():
    dataset = "wine"
    file_path = '../../data/wine.txt'
    data = load_data(file_path)
    k = 2

    # Clarans
    max_neighbour = 4
    num_local = 10

    filename = 'pyclustering-results'
    name = 'PyClustering - Clarans'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_clarans(
        data, k, max_neighbour, num_local)
    save_results(dataset, clusters, medoids, seconds, data, name, filename)

    filename = 'kmedoids-results'
    name = 'KMedoids'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_kmedoids(data, k)
    save_results(dataset, clusters, medoids, seconds, data, name, filename)

    filename = 'kmeans-results'
    name = 'KMeans'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_kmeans(data, k)
    save_results(dataset, clusters, medoids, seconds, data, name, filename)

    filename = 'agglomerative-clustering-results'
    name = 'Hierarchical Clustering - Agglomerative'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_agglomerative_clustering(data, k)
    save_results(dataset, clusters, medoids, seconds, data, name, filename)

    filename = 'spectral-clustering-results'
    name = 'Spectral Clustering'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_spectral_clustering(data, k)
    save_results(dataset, clusters, medoids, seconds, data, name, filename)


def yeast():
    dataset = "yeast"
    file_path = '../../data/yeast.txt'
    data = load_data(file_path)
    k = 10

    # Clarans
    max_neighbour = 5
    num_local = 10

    filename = 'pyclustering-results'
    name = 'PyClustering - Clarans'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_clarans(
        data, k, max_neighbour, num_local)
    save_results("yeast", clusters, medoids, seconds, data, name, filename)

    filename = 'kmedoids-results'
    name = 'KMedoids'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_kmedoids(data, k)
    save_results("yeast", clusters, medoids, seconds, data, name, filename)

    filename = 'kmeans-results'
    name = 'KMeans'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_kmeans(data, k)
    save_results("yeast", clusters, medoids, seconds, data, name, filename)

    filename = 'agglomerative-clustering-results'
    name = 'Hierarchical Clustering - Agglomerative'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_agglomerative_clustering(data, k)
    save_results("yeast", clusters, medoids, seconds, data, name, filename)

    filename = 'spectral-clustering-results'
    name = 'Spectral Clustering'
    print(f"{dataset}: '{name}'")
    clusters, medoids, seconds = compute_spectral_clustering(data, k)
    save_results("yeast", clusters, medoids, seconds, data, name, filename)


if __name__ == "__main__":
    iris()
    wine()
    yeast()
