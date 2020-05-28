import numpy as np


class NumPyCreator:

    def from_list(self, list):
        return (np.array(list))

    def from_tuple(self, tpl):
        return (np.array(tpl))

    def from_iterable(self, itr):
        return(np.array(itr))

    def from_shape(self, shape, value=0):
        return(np.full(shape, value))

    def random(self, shape):
        return(np.full(shape, np.random.rand()))

    def identity(self, i):
        return(np.identity(i))
