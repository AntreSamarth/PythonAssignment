"""
======================================================================
 Program     : 001_Manual_Convolution.py
 Topic       : Manual Convolution
 Description : Performs convolution on a grayscale image manually.
 Language    : Python
======================================================================
"""

# Input Image Matrix

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]


# Kernel Matrix

kernel = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]


# Create Feature Map

feature_map = []

for i in range(len(image) - len(kernel) + 1):

    row = []

    for j in range(len(image[0]) - len(kernel[0]) + 1):

        result = 0

        for x in range(len(kernel)):

            for y in range(len(kernel[0])):

                result = result + image[i + x][j + y] * kernel[x][y]

        row.append(result)

    feature_map.append(row)


# Display Feature Map

print("Input Image Matrix:")

for row in image:
    print(row)

print("\nKernel Matrix:")

for row in kernel:
    print(row)

print("\nFeature Map:")

for row in feature_map:
    print(row)