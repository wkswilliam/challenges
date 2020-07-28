#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:08:31 2020

@author: william
"""
import numpy as np
import math

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# where X is the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

'''
def sigmoid_derivative(x):
    return sigmoid(x)/(1 - sigmoid(x))
'''

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

w1 = np.array([synaptic_weights[0]])
w2 = np.array([synaptic_weights[1]])
w3 = np.array([synaptic_weights[2]])

# learning rate
alpha = 2

for iteration in range(20000):
    
    input_layer = training_inputs
    
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    
    error = training_outputs - outputs
    
    adjustments = alpha*error * sigmoid_derivative(outputs)
    
    synaptic_weights += np.dot(input_layer.T, adjustments)
    w1 = np.append(w1, synaptic_weights[0])
    w2 = np.append(w2, synaptic_weights[1])
    w3 = np.append(w3, synaptic_weights[2])
    
print(synaptic_weights)
print(outputs)