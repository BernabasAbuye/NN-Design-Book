# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 23:49:09 2025

@author: Bernabas
"""


def hardlims(net_n : float) -> int:
    """
    A single neuron perceptron creates a straight lline ( a flat plane in higher
                                                         dimention)
    that divide the input space into two categories.

    Parameters
    ----------
    net_n : float
        net_n = Wp + b 
        the net_n gives the dot product of the matrix weight (W) and the input
        scalar p plus the bias.

    Returns
    -------
    int
        the trasnfer function return an output a based on its relation to 0
        (the decision boundary).
        if it is >0 then output 1 else -1

    """
    return 1 if net_n > 0 else -1


# the equation for determining the decision boundary is Wp + b = 0

# Given two input vector
import numpy as np

p_apple = np.array([1, 1, -1]) #apple shape, texture, wieght
p_orange = np.array([1, -1, -1]) #orange shape, texture, wieght

"""
    Identifying the weight 
    
    we want an output of 1 for apple and -1 for orange it means
    
    Wp + b = 0
    
    for apple:
        W * p_apple + b >= 0
        W * p_orange + b < 0
        
    The only difference for the two materials is texture(the middle elmt)
    
    p_apple = texture value +1 and p_orange = texture -1 value
    
    ideal boundary will be:
        texture > 0 wil be apple else orange
        
    thus the other weight will be zero
    
    W = [0 1 0] we only give attention to the texture
    
"""

W = np.array([0, 1, 0])

net_apple = np.dot(W, p_apple) + 0 
net_orange = np.dot(W, p_orange) + 0

def apple_orange(a :float) -> str:
    return "Apple" if a > 0 else "Orange"

print(f'Input {p_apple} Result {apple_orange(hardlims(net_apple))}')

print(f'Input {p_orange} Result {apple_orange(hardlims(net_orange))}')
    