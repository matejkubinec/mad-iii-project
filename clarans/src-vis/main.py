import matplotlib.pyplot as plt
from sklearn import metrics
from dunn_index import dunn_index
import json

def visualize_dunn_index(results):
    indexes = []
    dunn_indexes = []
    names = []

    for i, res in enumerate(results):
        clusters = res['clusters']
        name = res['name']

        names.append(name)
        indexes.append(i)
        dunn_indexes.append(dunn_index(clusters))

    _, ax = plt.subplots()

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, dunn_indexes)

    plt.savefig("dunn_index.png")

def silhouette_score(medoids, clusters):
    pass

def load_result(filename):
    json_str = ''

    with open(filename, 'r') as f:
        lines = f.readlines()
        json_str = ''.join(lines)

    return json.loads(json_str)

def visualise(medoids, clusters):
    _, ax = plt.subplots()

    for cl in clusters:
        X = [v[0] for v in cl]
        Y = [v[1] for v in cl]
        S = [25 if v in medoids else 10 for v in cl]
        ax.scatter(X, Y, s=S)

    plt.savefig("visualised.png")

if __name__ == "__main__":
    names = [
        "PyClustering - Clarans",
        "KUB0462 - Clarans"
    ]

    filenames = [
        '../results/pyclustering-results.json',
        '../results/clarans-csharp-results.json',
    ]

    results = list(map(load_result, filenames))

    for r, n in zip(results, names):
        r['name'] = n

    # filename = filenames[0]
    #  = load_result(filename)
    # visualise(medoids, clusters)
    
    visualize_dunn_index(results)