# -*- coding: utf-8 -*-

#import
import numpy as np
import pandas as pd

#data
input_data = np.array([
        [0,0],
        [1,0],
        [0,1],
        [1,1]])
expected_output = np.array([[0],[1],[1],[0]])
data_num = input_data.shape[0]
input_node = input_data.T.shape[0]
first_node = 3
second_node = 1

alpha = 0.1
epochs = 40000

def Sig(x):
    return 1 / (1 + np.exp(-x))

def d_Sig(x):
    return Sig(x)*(1-Sig(x))

first_weight = np.random.rand(input_node, first_node) - 0.5
second_weight= np.random.rand(first_node, second_node) - 0.5
for i in range(epochs):
    first_node_input = np.dot(input_data, first_weight)
    first_node_output = Sig(first_node_input)
    second_node_input = np.dot(first_node_output, second_weight)
    second_node_output = Sig(second_node_input)
    Error = (second_node_output - expected_output)**2
    
    d_Error = (second_node_output - expected_output)
    d_second_node_output = d_Error*d_Sig(second_node_input)
    d_second_weight = np.dot(first_node_output.T, d_second_node_output)
    d_second_node_input = np.dot(d_second_node_output, second_weight.T)
    d_first_node_output = d_second_node_input*d_Sig(first_node_input)
    d_first_weight = np.dot(input_data.T,d_first_node_output)
    
    first_weight -= alpha*(d_first_weight)
    second_weight -= alpha*(d_second_weight)

first_node_input = np.dot(input_data, first_weight)
first_node_output = Sig(first_node_input)
second_node_input = np.dot(first_node_output, second_weight)
second_node_output = Sig(second_node_input)

print("predict\n",second_node_output)
print("Answer\n",expected_output)

