import numpy
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
import random

def visualize(X, Y, results):

    def generate_random_permutation():
        return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16))

    def generate_base64_image(img_buffer):
        b64str = base64.b64encode(img_buffer.getvalue())
        permutation = generate_random_permutation()
        img_str = "<image %s>" % permutation
        img_str += str(b64str)[2:-1]
        img_str += "</%s>" % permutation
        return img_str

    slope = results.params[1]
    intercept = results.params[0]

    plt.scatter(X, Y)
    reg_line_x = numpy.array([min(X), max(X)])
    reg_line_y = reg_line_x * slope + intercept
    plt.plot(reg_line_x, reg_line_y, color='r')
    plt.show()

    format = "png"
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format=format)
    img_buffer.seek(0)

    return generate_base64_image(img_buffer)
