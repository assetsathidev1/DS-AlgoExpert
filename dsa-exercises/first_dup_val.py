"""
input: array of integers b/w 1 and n (inclusive)
ex: [2, 1, 5, 2, 3, 3, 4]
output: 2 # 2 is the first duplicate value in the array

trick: use the array itself as a hash table
mutate the index-1 of the array to be negative,
while looping forward if you find the current value at index-1 to be negative, return the value 
"""

# o(n) in time | o(1) in space
def firstDuplicateValue(array):
    for k in array:
        idx_k = abs(k)
        if array[idx_k - 1] < 0:
            return idx_k
        array[idx_k-1] *= -1
    return -1

# o(n) in time | o(n) in space
def firstDuplicateValue(array):
    d = {}
    for k in array:
        if k in d:
            return k
        else:
            d[k] = 1
    return -1
