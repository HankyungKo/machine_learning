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

def display_digits(digits, index):
    plt.clf()
    plt.figure(1, figsize=(2, 2))
    plt.imshow(digits.images[index], cmap=plt.cm.gray_r, interpolation='nearest')

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)

def benchmark_plot(X, Y):
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.plot(X, Y, color='b', linestyle='dashed')
    ax.scatter(X, Y)
    ax.set_title("Benchmark: #Components from 1 to 64")
    ax.set_xlabel("#Principal Components")
    ax.set_ylabel("Homogeneity Score")

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
