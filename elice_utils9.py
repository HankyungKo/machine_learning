import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
import random
import sklearn.preprocessing

def generate_random_permutation():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16))

def generate_base64_image(img_buffer):
    b64str = base64.b64encode(img_buffer.getvalue())
    permutation = generate_random_permutation()
    img_str = "<image %s>" % permutation
    img_str += str(b64str)[2:-1]
    img_str += "</%s>" % permutation
    return img_str

def draw_init():
    plt.figure(figsize=(2 + 3, 2.5 * 9 + 0.5))
    plt.subplots_adjust(left=.02, right=.98, bottom=.001, top=.99, wspace=.05, hspace=.1)


def draw_graph(X, dbscan_result, alg_name, plot_num, len_algs, indices):
    colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
    colors = np.hstack([colors] * 20)

    plt.subplot(len_algs, 2, indices[plot_num-1])
    if len_algs >= plot_num:
        plt.title(alg_name, size=18)
    plt.scatter(X[:, 0], X[:, 1], color=colors[dbscan_result.labels_.astype(np.int)].tolist(), s=10)

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.xticks(())
    plt.yticks(())


def show_graph():
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)


def plot_digit_class(pca_array, num_classes):
    x = pca_array[:, 0]
    y = pca_array[:, 1]

    scaler = sklearn.preprocessing.MinMaxScaler()
    num_color = scaler.fit_transform(np.array(num_classes).astype('float64'))

    plt.figure(figsize=(20, 10))
    plt.scatter(x, y,  c = num_color, s = 50, cmap = plt.get_cmap('Spectral'))

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)
