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


def save_results(dataset, clusters, medoids, seconds, data, name, filename):
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

    with open(f'../../results/{dataset}/{filename}.json', 'w') as f:
        f.write(json_str)