"""
======================================================================
 Program     : 001_Single_Artificial_Neuron.py
 Topic       : Artificial Neural Network - Single Neuron
 Description : Demonstrates the working of a single artificial neuron.
 Language    : Python
======================================================================
"""

import math

# Input values
x1 = 2
x2 = 3

# Weights
w1 = 0.4
w2 = 0.6

# Bias
bias = 0.5

# Calculate weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias

print("Input x1        :", x1)
print("Input x2        :", x2)
print("Weight w1       :", w1)
print("Weight w2       :", w2)
print("Bias            :", bias)
print("Weighted Sum    :", weighted_sum)

# Sigmoid activation function
output = 1 / (1 + math.exp(-weighted_sum))

print("Neuron Output   :", output)

# Explain output
if output >= 0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")