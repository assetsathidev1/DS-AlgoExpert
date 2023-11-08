"""
input: [3, 5, -4, 8, 11, 1, -1, 6]
targetSum: 10
output: [-1, 11]
"""

# o(n) time | o(n) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    d = {k:targetSum - k for k in array}
    for k in d:
        v = d[k]
        if v in d and v != k:
            return [k, v]
    return []
