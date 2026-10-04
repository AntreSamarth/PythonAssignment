"""
======================================================================
 Program     : 003_Flattening.py
 Topic       : Flattening
 Description : Converts a 2D matrix into a 1D vector manually.
 Language    : Python
======================================================================
"""

# Input Matrix

matrix = [
    [6, 4],
    [8, 6]
]


# Flatten Matrix

flatten_output = []

for row in matrix:

    for value in row:

        flatten_output.append(value)


# Display Input

print("Input Matrix:")

for row in matrix:
    print(row)


# Display Flattened Output

print("\nFlattened Output:")
print(flatten_output)