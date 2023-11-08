"""
input: two arrays of integers
ex: 
arr1: [10, 15, 8, 12, 94, 81, 5, 2, 11]
arr2: [10, 8, 5, 15, 2, 12, 11, 94, 81]
output: true # boolean

trick: check for same len and first element, and then 
split the arrays into left and right subtrees and recusively call the function on them
"""


# o(n^2) in time | o(d) in space
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False
    larr1 = []
    rarr1 = []
    larr2 = []
    rarr2 = []

    for i in range(1, len(arrayOne)):
        if arrayOne[i] < arrayOne[0]:
            larr1.append(arrayOne[i])
        else:
            rarr1.append(arrayOne[i])
            
    for i in range(1, len(arrayTwo)):
        if arrayTwo[i] < arrayTwo[0]:
            larr2.append(arrayTwo[i])
        else:
            rarr2.append(arrayTwo[i])
    l_match = sameBsts(larr1, larr2)
    r_match = sameBsts(rarr1, rarr2)
    return l_match and r_match
