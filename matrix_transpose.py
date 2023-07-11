"""
input: [
  [1, 2, 3]
]
output: [
    [1],    
    [2],
    [3]
]
"""

# o(r * c) in time | o(r * c) in space
def transposeMatrix(matrix):
    # Write your code here.
    r = len(matrix)
    c = len(matrix[0])
    new_matrix = []
    for i in range(c):
        new_matrix.append([])
        for j in range(r):
            new_matrix[i].append(0)
    for i in range(r):
        for j in range(c):
            ele = matrix[i][j]
            new_matrix[j][i] = ele
    return new_matrix
