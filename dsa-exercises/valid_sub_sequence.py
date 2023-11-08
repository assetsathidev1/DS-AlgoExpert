"""
Input array: [5, 1, 22, 25, 6, -1, 8, 10]
Input Sequence: [1, 6, -1, 10]
Output: True
"""

# o(n) time | o(1) in space
def isValidSubsequence(array, sequence):
    si = 0
    l = len(sequence)
    for k in array:
        if k == sequence[si]:
            si += 1
        if si == l: 
            return True
    return False