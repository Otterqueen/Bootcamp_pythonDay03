import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker():
    def crop(self, array, dimensions, position=(0, 0)):
        """crops the image as a rectangle with the given dimensions whose top\
left corner is given by the position argument.You have to consider it an error\
if dimensions is larger than the current image size."""
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            print("Error: the dimensions is larger than shape.")
            return None
        else:
            crop_x = position[1] + dimensions[1]
            crop_y = position[0] + dimensions[0]
            if crop_x > array.shape[1] or crop_y > array.shape[0]:
                print("Error: the dimensions is larger than shape.")
                return None
            return array[position[1]:crop_x, position[0]:crop_y]

    def thin(self, array, n, axis):
        """deletes every n-th pixel row along the specified axis\
    (0 vertical, 1 horizontal)"""
        axis = 1 - axis
        if axis == 1 or axis == 0:
            arr = np.delete(array, np.s_[n-1::n], axis)
            return arr
        else:
            print("Error: the axis is not egal to 0 or 1.")
            return None

    def juxtapose(self, array, n, axis):
        """juxtaposes n copies of the image along the specified axis\
    (0 vertical, 1horizontal)."""
        axis = 1 - axis
        if axis == 1 or axis == 0:
            arr = np.concatenate([array] * n, axis)
            return arr
        else:
            print("Error: the axis is not egal to 0 or 1.")
            return None

    def mosaic(self, array, dimensions):
        """makes a grid with multiple copies of the array. The dimensions\
argument specifies the dimensions of the grid (e.g. 2x3)"""
        return np.tile(array, dimensions + (1,))


# main de test
img_p = ImageProcessor()
arr = img_p.load("test.PNG")
sb = ScrapBooker()
arr2 = sb.crop(arr, (200, 200), (0, 0))
img_p.display(arr2)
arr3 = sb.thin(arr, 3, 0)
img_p.display(arr3)
arr4 = sb.thin(arr, 3, 1)
img_p.display(arr4)
arr5 = sb.juxtapose(arr, 3, 1)
img_p.display(arr5)
arr6 = sb.juxtapose(arr, 3, 0)
img_p.display(arr6)
arr7 = sb.mosaic(arr, (3, 2))
img_p.display(arr7)
