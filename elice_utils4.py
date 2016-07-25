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

def plot_champions(champs_df, champ_pca_array):
    champ_names = champs_df.index.values

    x = champ_pca_array[:, 0]
    y = champ_pca_array[:, 1]
    difficulty = champs_df['difficulty'].values
    magic = champs_df['attack'].values

    plt.figure(figsize=(20, 10))

    plt.scatter(x, y,  c = magic, s = difficulty*1500, cmap = plt.get_cmap('Spectral'))

    for champ_name, x, y in zip(champ_names, x, y):
        plt.annotate(
            champ_name,
            xy = (x, y), xytext = (-20, 20),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)
