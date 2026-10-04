"""
======================================================================
 Program     : 002_ReLU_MaxPooling.py
 Topic       : ReLU and Max Pooling
 Description : Demonstrates ReLU activation and 2x2 Max Pooling.
 Language    : Python
======================================================================
"""

# Input Feature Map

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]


# Apply ReLU

relu_output = []

for row in feature_map:

    new_row = []

    for value in row:

        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu_output.append(new_row)


print("Input Feature Map:")

for row in feature_map:
    print(row)


print("\nReLU Output:")

for row in relu_output:
    print(row)


# Apply 2x2 Max Pooling

pool_size = 2

pooled_output = []

for i in range(len(relu_output) - pool_size + 1):

    row = []

    for j in range(len(relu_output[0]) - pool_size + 1):

        maximum = relu_output[i][j]

        for x in range(pool_size):

            for y in range(pool_size):

                if relu_output[i + x][j + y] > maximum:
                    maximum = relu_output[i + x][j + y]

        row.append(maximum)

    pooled_output.append(row)


print("\nMax Pooling Output:")

for row in pooled_output:
    print(row)