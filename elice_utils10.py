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
    plt.figure(figsize=(9, 9))
    plt.subplots_adjust(left=.02, right=.98, bottom=.001, top=.96, wspace=.05, hspace=.01)


def draw_graph(X, y, svc_linear, svc_poly2, svc_poly3, svc_rbf, h = 0.2):
    draw_init()

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    titles = ['SVC with linear kernel',
              'SVC with polynomial degree 2 kernel',
              'SVC with polynomial degree 3 kernel',
              'SVC with RBF kernel']

    colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
    colors = np.hstack([colors] * 20)

    for i, clf in enumerate((svc_linear, svc_poly2, svc_poly3, svc_rbf)):
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

        plt.scatter(X[:, 0], X[:, 1], color=colors[y.tolist()].tolist())
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i])

    print(show_graph())

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
