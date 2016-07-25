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

def wine_graph(pca_array, class_df, class_names = ['Cultivar 1', 'Cultivar 2', 'Cultivar 3']):
    plt.figure(figsize=(6, 4.5))

    class_array = np.array(class_df)
    for c, i, class_name in zip("rgb", [1, 2, 3], class_names):
        plt.scatter(pca_array[class_array == i, 0], pca_array[class_array == i, 1], c=c, label=class_name, linewidth='0', s=6)

    plt.legend(loc=4)

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)
