import matplotlib.pyplot as plt
from sklearn import metrics
from dunn_index import dunn_index
import json
from utils import labelize_clusters
import os


def load_result(filename):
    json_str = ''

    with open(filename, 'r') as f:
        lines = f.readlines()
        json_str = ''.join(lines)

    return json.loads(json_str)


def load_filenames(dataset):
    res_dir = f"../../results/{dataset}/"
    files = os.listdir(res_dir)
    filenames = map(lambda f: res_dir + f, files)
    return list(filenames)


def get_size(results):
    col_width = 3
    return col_width * len(results), 5


def visualise_seconds(subfolder, dataset, results):
    indexes = [i for i in range(len(results))]
    names = []
    scores = []
    colors = []
    image_path = f"../../images/{subfolder}/{dataset}"

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    for r in results:
        name = r["name"]
        names.append(name)

        if name.startswith("KUB0462"):
            colors.append('r')
        else:
            colors.append('b')

        seconds = r["seconds"]
        scores.append(seconds)

    fig, ax = plt.subplots()
    width, height = get_size(results)
    fig.set_size_inches(width, height)

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, scores, color=colors)

    plt.title("Seconds")
    plt.savefig(image_path + "/seconds.png")


def visualise_davies_bouldin_score(subfolder, dataset, results):
    indexes = [i for i in range(len(results))]
    names = []
    scores = []
    colors = []
    image_path = f"../../images/{subfolder}/{dataset}"

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    for r in results:
        names.append(r["name"])

        if r['name'].startswith("KUB0462"):
            colors.append('r')
        else:
            colors.append('b')

        items, labels = labelize_clusters(r["clusters"])

        score = metrics.davies_bouldin_score(items, labels)
        scores.append(score)

    fig, ax = plt.subplots()
    width, height = get_size(results)
    fig.set_size_inches(width, height)

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, scores, color=colors)

    plt.title("Davies-Bouldin Score")
    plt.savefig(image_path + "/davies_bouldin_score.png")


def visualize_dunn_index(subfolder, dataset, results):
    indexes = []
    dunn_indexes = []
    names = []
    colors = []
    image_path = f"../../images/{subfolder}/{dataset}"

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    for i, res in enumerate(results):
        clusters = res['clusters']
        name = res['name']

        if res['name'].startswith("KUB0462"):
            colors.append('r')
        else:
            colors.append('b')

        names.append(name)
        indexes.append(i)
        dunn_indexes.append(dunn_index(clusters))

    fig, ax = plt.subplots()
    width, height = get_size(results)
    fig.set_size_inches(width, height)

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, dunn_indexes, color=colors)

    plt.title("Dunn Score")
    plt.savefig(image_path + "/dunn_index.png")


def visualise_silhouette_coefficient(subfolder, dataset, results):
    indexes = [i for i in range(len(results))]
    names = []
    scores = []
    colors = []
    image_path = f"../../images/{subfolder}/{dataset}"

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    for r in results:
        names.append(r["name"])

        if r['name'].startswith("KUB0462"):
            colors.append('r')
        else:
            colors.append('b')

        items, labels = labelize_clusters(r["clusters"])

        score = metrics.silhouette_score(items, labels)
        scores.append(score)

    fig, ax = plt.subplots()
    width, height = get_size(results)
    fig.set_size_inches(width, height)

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, scores, color=colors)

    plt.title("Silhouette Coefficient Score")
    plt.savefig(image_path + "/fsilhouette_coefficient.png")


def visualise_adjusted_rand_index(subfolder, dataset, results):
    indexes = [i for i in range(len(results))]
    names = []
    scores = []
    colors = []
    image_path = f"../../images/{subfolder}/{dataset}"

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    for r in results:
        names.append(r["name"])

        if r['name'].startswith("KUB0462"):
            colors.append('r')
        else:
            colors.append('b')

        items, labels = labelize_clusters(r["clusters"])

        score = metrics.calinski_harabasz_score(items, labels)
        scores.append(score)

    fig, ax = plt.subplots()
    width, height = get_size(results)
    fig.set_size_inches(width, height)

    ax.set_xticks(indexes)
    ax.set_xticklabels(names)
    ax.bar(indexes, scores, color=colors)

    plt.title("Adjusted Rand Index Score")
    plt.savefig(image_path + "/calinski_harabasz_score.png")


if __name__ == "__main__":
    datasets = ["iris", "wine", "yeast"]

    for dataset in datasets:
        filenames = load_filenames(dataset)
        filenames = filter(lambda f: "pyclustering" not in f, filenames)
        subfolder = "all"
        results = list(map(load_result, filenames))

        visualize_dunn_index(subfolder, dataset, results)
        visualise_silhouette_coefficient(subfolder, dataset, results)
        visualise_adjusted_rand_index(subfolder, dataset, results)
        visualise_davies_bouldin_score(subfolder, dataset, results)
        visualise_seconds(subfolder, dataset, results)

    for dataset in datasets:
        filenames = load_filenames(dataset)
        filenames = filter(lambda f: "clarans" in f or "pyclustering" in f, filenames)
        subfolder = "pyclustering"
        results = list(map(load_result, filenames))

        visualize_dunn_index(subfolder, dataset, results)
        visualise_silhouette_coefficient(subfolder, dataset, results)
        visualise_adjusted_rand_index(subfolder, dataset, results)
        visualise_davies_bouldin_score(subfolder, dataset, results)
        visualise_seconds(subfolder, dataset, results)
