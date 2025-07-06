# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 04:38:15 2025

@author: Bernabas

@desc: designed only for ch-3 of nn design book by Hegan
"""

import numpy as np


class Hamming:
    """
    Hamming uses two layers with same number of neuron:
        FeedForward layer:
            - it takes the input prototype and correlate against the input
            vector
            Given p1 and p2 input the weight will be:
                W = arrya of p1 transpose and p2 transpose
                b = the bias will be equal to R (length of the input)
        Recurrent layer:
            - it takes the output of the feedforward layer which gives the
            similarity between the prototype and the input vector and use it
            as initializer a2(0) = a1

            Then it iterate and compete using the poslin transfer func to give
            until the output converges (stop changing)
    """

    def __init__(self, prototype_1: list, prototype_2: list):
        """


        Parameters
        ----------
        prototype_1 : list
            Vector of int for orange.
        prototype_2 : list
            Vector of int for apple.

        Returns
        -------
        None.

        """
        self.p1 = np.array(prototype_1)
        self.p2 = np.array(prototype_2)

        self.W = np.array([self.p1.T, self.p2.T])

        self.bias = np.array([[3, 3]])  # hard coding the

    def feed_forward_layer(self, input_vec: list) -> list:

        a = self.W.dot(input_vec) + self.bias
        return a

    def recurrent_layer(self, a: list, e: float) -> list:
        a2 = np.array(a).reshape(-1, 1)
        self.w2 = np.array([[1, -e], [-e, 1]])


        prev_a2 = np.zeros_like(a2)
        calculating = True
        while calculating:
            print('working')
            prev_a2 = a2.copy()
            a2 = np.dot(self.w2, a2)
            a2 = np.where(a2 > 0, a2, 0)
            calculating = not np.array_equal(a2, prev_a2)
        return a2.tolist()

test = Hamming([1, -1, -1], [1, 1, -1])

output = test.feed_forward_layer(np.array([-1, -1, -1]))
final = test.recurrent_layer(output, 0.5)