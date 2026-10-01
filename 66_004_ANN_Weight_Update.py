"""
======================================================================
 Program     : 004_ANN_Weight_Update.py
 Topic       : Artificial Neural Network - Weight Update
 Description : Demonstrates weight update using gradient descent logic.
 Language    : Python
======================================================================
"""

# Input
input_value = 2

# Initial weight
weight = 0.5

# Bias
bias = 0.1

# Target output
target = 1

# Learning rate
learning_rate = 0.1


# Calculate prediction
prediction = (input_value * weight) + bias

print("Input Value       :", input_value)
print("Old Weight        :", weight)
print("Bias              :", bias)
print("Target Output     :", target)
print("Learning Rate     :", learning_rate)
print("Prediction        :", prediction)


# Calculate error
error = target - prediction

print("Error             :", error)


# Calculate gradient
gradient = error * input_value

print("Gradient          :", gradient)


# Update weight
new_weight = weight + (learning_rate * gradient)

print("Updated Weight    :", new_weight)