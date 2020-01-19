import os


def load_labels():
    base_path = os.path.dirname(os.path.realpath(__file__))
    data_path = f'{base_path}/data/birch_5_labels.txt'

    line = None
    with open(data_path, 'r') as f:
        line = f.readline()

    labels = line.split(' ')
    return labels
