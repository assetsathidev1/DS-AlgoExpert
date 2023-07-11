"""
input1: [-1, 5, 10, 20, 28, 3]
input2: [26, 134, 135, 15, 17]
output: [28, 26]
trick: 
sort both and use two pointers, one for each array
find the difference between the two pointers and keep track of the smallest difference
if the difference is 0, return the two numbers
move the smallest of the two pointers values till you reach 0 diff or end of array
"""

# o(nlogn + mlogm) in time | o(1) in space
def smallestDifference(arrayOne, arrayTwo):
    smallest_so_far = 9999999
    result = []
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    while (i<len(arrayOne) and j<len(arrayTwo)):
        ad = abs(arrayOne[i] - arrayTwo[j])
        if ad < smallest_so_far:
            smallest_so_far = ad
            result = [arrayOne[i], arrayTwo[j]]
            if ad == 0:
                return result
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    return result
    

# o(n*m) in time | o(1) in space -> bruteforce
def smallestDifference(arrayOne, arrayTwo):
    smallest_so_far = 9999999
    result = [] 
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            ad = abs(arrayOne[i] - arrayTwo[j])
            if ad < smallest_so_far:
                smallest_so_far = ad
                result = [arrayOne[i], arrayTwo[j]]
    return result