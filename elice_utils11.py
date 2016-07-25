import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
import random
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster


def generate_random_permutation():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16))

def generate_base64_image(img_buffer):
    b64str = base64.b64encode(img_buffer.getvalue())
    permutation = generate_random_permutation()
    img_str = "<image %s>" % permutation
    img_str += str(b64str)[2:-1]
    img_str += "</%s>" % permutation
    return img_str

def plot_stocks(df, pca_array, cluster_labels, code_to_name, display_cluster_idx):
    display_datapoints_indices = [i for i in range(0, len(cluster_labels)) if cluster_labels[i] == display_cluster_idx]

    names = df.index.values[display_datapoints_indices]

    x = pca_array[:, 0][display_datapoints_indices]
    y = pca_array[:, 1][display_datapoints_indices]

    scaler = sklearn.preprocessing.MinMaxScaler()
    colors = scaler.fit_transform(np.array(cluster_labels).astype('float64'))[display_datapoints_indices]

    plt.figure(figsize=(20, 10))
    plt.scatter(x, y, c = colors, cmap = plt.get_cmap('Spectral'))

    for name, x, y in zip(names, x, y):
        plt.annotate(
            code_to_name[name],
            xy = (x, y), xytext = (-20, 20),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)
