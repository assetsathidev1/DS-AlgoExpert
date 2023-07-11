"""
input: [12, 3, 1, 2, -6, 5, -8, 6]
targetSum: 0
output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
trick: 
sort the array first, 
then use two pointers left(immediatly after current) and right most ele of array
sum these 3 and move pointers accordingly
"""

# o(n) in space | o(n^2) in time
def threeNumberSum(array, targetSum):
    array.sort()
    i = 0
    result = []
    for i in range(len(array)):
        l = i + 1
        r = len(array)-1
        while l < r:
            s = array[i] + array[l] + array[r]
            if s == targetSum:
                result.append([array[i], array[l], array[r]])
                r -= 1
                l += 1
            elif s > targetSum:
                r -= 1
            elif s < targetSum:
                l += 1
    return result
