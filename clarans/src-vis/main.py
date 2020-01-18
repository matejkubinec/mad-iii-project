import matplotlib.pyplot as plt
from sklearn import metrics
from dunn_index import dunn_index
import json
from utils import labelize_clusters
import os



def load_filenames():
    res_dir = "../results/"
    files = os.listdir(res_dir)
    filenames = map(lambda f: res_dir + f,files)
    return list(filenames)

def visualise_davies_bouldin_score(results):
    indexes = [i for i in range(len(results))]
    names = []
    scores = []

    for r in results:
        names.append(r["name"])

        items, labels = labelize_clusters(r["clusters"])

        score = metrics.davies_bouldin_score(items, labels)
        scores.append(score)

    _, ax = plt.subplots()

    fig.set_size_inches(5, 20)

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, scores)

    plt.savefig("images/davies_bouldin_score.png", dpi=500)

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

    plt.savefig("images/dunn_index.png")

def visualise_silhouette_coefficient(results):
    indexes = [i for i in range(len(results))]
    names = []
    scores = []

    for r in results:
        names.append(r["name"])

        items, labels = labelize_clusters(r["clusters"])

        score = metrics.silhouette_score(items, labels)
        scores.append(score)

    _, ax = plt.subplots()

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, scores)

    plt.savefig("images/silhouette_coefficient.png")

def visualise_adjusted_rand_index(results):
    indexes = [i for i in range(len(results))]
    names = []
    scores = []

    for r in results:
        names.append(r["name"])

        items, labels = labelize_clusters(r["clusters"])

        score = metrics.calinski_harabasz_score(items, labels)
        scores.append(score)

    _, ax = plt.subplots()

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, scores)

    plt.savefig("images/calinski_harabasz_score.png")


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
    filenames = load_filenames()

    results = list(map(load_result, filenames))

    for r in results:
        if 'name' not in r.keys():
            r['name'] = "KUB0462 - Clarans"
            r['seconds'] = 0
    
    visualize_dunn_index(results)
    visualise_silhouette_coefficient(results)
    visualise_adjusted_rand_index(results)
    visualise_davies_bouldin_score(results)