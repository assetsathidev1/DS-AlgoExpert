"""
input: [1, 2, 3, 5, 6, 8, 9]
output: [1, 4, 9, 25, 36, 64, 81]

input: [-10, -5, 0, 5, 10]
output: [0, 25, 25, 100, 100]
"""

# o(nlogn) time | o(n) space
def sortedSquaredArray(array):
    # Write your code here.
    narray = []
    for k in array:
        narray.append(k*k)
    narray.sort()
    return narray


# o(n) time  | o(n) space - took hints
def sortedSquaredArray(array):
    # Write your code here.
    narray = [0 for _ in array]
    l = 0
    r = len(array) - 1
    
    for idx in reversed(range(len(array))):
        l2 = array[l] * array[l]
        r2 = array[r] * array[r]
        if l2 > r2:
            narray[idx] = l2
            l += 1
        else:
            narray[idx] = r2
            r -= 1
    return narray
    
