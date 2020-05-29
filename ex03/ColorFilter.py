import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from ImageProcessor import ImageProcessor


class ColorFilter():

    def invert(self, array):
        return (1 - array[:, :, 0:3])

    def to_blue(self, array):
        blu = np.zeros(array.shape)
        blu[:, :, 2] = array[:, :, 2]
        if array.shape[2] == 4:
            blu[:, :, 3] = array[:, :, 3]
        return blu

    def to_green(self, array):
        green = array[:, :, [0, 1, 0, 0]]
        green[:, :, 0] = (0 * array[:, :, 0])
        green[:, :, 2] = (0 * array[:, :, 2])
        if array.shape[2] == 4:
            green[:, :, 3] = array[:, :, 3]
            return green[:, :, 0:4]
        else:
            return green[:, :, 0:3]

    def to_red(self, array):
        red = array - self.to_blue(array) - self.to_green(array)
        return red[:, :, 0:3]

    def plus_proche(self, colors, n):
        lst = np.linspace(0, 1, num=4)
        for i, color in enumerate(colors):
            for palier in lst:
                if -1/(n*2) <= palier - color <= 1/(n*2):
                    colors[i] = palier
        return colors

    def celluloid(self, array, n=4):
        copy = array * 1
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                copy[i][j] = self.plus_proche(copy[i][j], n)
        return copy


# main de test
img_p = ImageProcessor()
arr = img_p.load("test2.png")
cf = ColorFilter()

arr2 = cf.invert(arr)
img_p.display(arr2)
arr2 = cf.to_blue(arr)
img_p.display(arr2)
arr2 = cf.to_green(arr)
img_p.display(arr2)
arr2 = cf.to_red(arr)
img_p.display(arr2)
arr3 = cf.celluloid(arr)
img_p.display(arr3)
