"""
======================================================================
 Program     : 003_Loss_Functions.py
 Topic       : Artificial Neural Network - Loss Functions
 Description : Calculates Mean Squared Error and Binary Cross Entropy
               manually using Python.
 Language    : Python
======================================================================
"""

import math

# Actual values
actual = [1, 0, 1, 1, 0]

# Predicted values
predicted = [0.9, 0.2, 0.8, 0.7, 0.1]


# Mean Squared Error
mse_sum = 0

for i in range(len(actual)):
    error = actual[i] - predicted[i]
    mse_sum = mse_sum + (error * error)

mse = mse_sum / len(actual)


# Binary Cross Entropy
bce_sum = 0

for i in range(len(actual)):
    y = actual[i]
    p = predicted[i]

    bce_sum = bce_sum + (
        y * math.log(p) +
        (1 - y) * math.log(1 - p)
    )

bce = -bce_sum / len(actual)


# Display values
print("Actual Values    :", actual)
print("Predicted Values :", predicted)

print("Mean Squared Error      :", mse)
print("Binary Cross Entropy    :", bce)


# Explanation
print("\nLoss Function Usage:")
print("MSE  -> Commonly used for Regression")
print("BCE  -> Commonly used for Binary Classification")