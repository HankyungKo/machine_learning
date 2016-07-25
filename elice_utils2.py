import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
import random

def generate_random_permutation():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16))

def generate_base64_image(img_buffer):
    b64str = base64.b64encode(img_buffer.getvalue())
    permutation = generate_random_permutation()
    img_str = "<image %s>" % permutation
    img_str += str(b64str)[2:-1]
    img_str += "</%s>" % permutation
    return img_str

def draw_toy_example(df, pca, pca_array):
    plt.figure(figsize=(4.5, 4.5))

    X = np.array(df['x'].values)
    Y = np.array(df['y'].values)

    X = X - np.mean(X)
    Y = Y - np.mean(Y)

    line_X = np.arange(X.min() - 0.2, X.max() + 0.2, step=0.1)
    line_Y = (pca.components_[0, 1] / pca.components_[0, 0]) * line_X

    plt.ylim(min(min(line_X), min(line_Y)), max(max(line_X), max(line_Y)))
    plt.xlim(min(min(line_X), min(line_Y)), max(max(line_X), max(line_Y)))

    for x, y in zip(X, Y):
        plt.scatter(x, y)
    plt.plot(line_X, line_Y)

    pca_x = np.array(pca_array)
    pca_x = pca_x ** 2
    a = pca_x / (pca.components_[0, 1] ** 2 + pca.components_[0, 0] ** 2)
    a = np.sqrt(a)

    red_x = []
    red_y = []
    for i in range(0, len(a)):
        red_x.append(pca.components_[0, 0] * a[i] * np.sign(pca_array[i]))
        red_y.append(pca.components_[0, 1] * a[i] * np.sign(pca_array[i]))

    plt.scatter(red_x, red_y, c='r')

    for i in range(0, len(a)):
        plt.plot([X[i], red_x[i]], [Y[i], red_y[i]], ls='dotted', c='black')

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)
