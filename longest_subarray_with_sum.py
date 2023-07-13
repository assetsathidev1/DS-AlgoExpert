"""
input array: [1, 2, 3, 4, 3, 3, 1, 2, 1]
targetSum: 10
output: [4, 8]
trick: start with both pointers at 0, 
keep adding right pointer values till you exceed or equal targetSum
if you exceed, keep subtracting left pointer values till you are less than or equal targetSum
if you are equal, check if the current result is smaller than the previous result
"""

# o(n) in space | o(1) in time
def longestSubarrayWithSum(array, targetSum):
    # Write your code here.
    l = 0
    r = len(array)-1
    s = sum(array) 
    result = []
    if s == targetSum:
        return [l,r]
    l = 0
    r = 0
    cs = 0
    while r < len(array):
        cs += array[r]
        while l < r and cs > targetSum:
            cs -= array[l]
            l += 1

        if cs == targetSum:
            if len(result)==0 or result[1] - result[0] < r - l:
                result = [l, r]
        r += 1
    return result
