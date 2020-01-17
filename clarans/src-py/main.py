from pyclustering.cluster.clarans import clarans
from pyclustering.utils import timedcall
import json


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


def save_results(clusters, medoids, data):
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
        'medoids': medoids_data
    }

    json_str = json.dumps(data)

    with open('pyclustering-results.json', 'w') as f:
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
    max_neighbour = 5
    num_local = 5

    clarans_instance = clarans(data, k, num_local, max_neighbour)

    clarans_instance.process()

    # (ticks, result) = timedcall(clarans_instance.process)
    # print("Execution time : ", ticks, "\n")

    clusters = clarans_instance.get_clusters()

    medoids = clarans_instance.get_medoids()

    save_results(clusters, medoids, data)
