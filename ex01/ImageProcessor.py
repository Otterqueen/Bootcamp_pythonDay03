import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


class ImageProcessor():

    def load(self, path):
        """opens the .png file specified by the path argument and returns an \
array with the RGB values of the image pixels. It must display a message\
specifying the dimensions of the image (e.g. 340 x 500)."""
        datas = mpimg.imread(path)
        print("Loading image of dimensions ",
              datas.shape[1], " x ", datas.shape[0])
        return datas

    def display(self, array):
        """takes a NumPy array as an argument and displays\
the corresponding RGB image."""
        plt.imshow(array)
        plt.show()


# main de test
img_p = ImageProcessor()
arr = img_p.load("test.PNG")
img_p.display(arr)
