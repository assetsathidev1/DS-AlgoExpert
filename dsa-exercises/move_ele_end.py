"""
input array: [2, 1, 2, 2, 2, 3, 4, 2]
toMove: 2
output: [4, 1, 3, 2, 2, 2, 2, 2]
trick: two pointer start and end 
move the end pointer till you find a non toMove value
swap the start and end values
move the start pointer till you find a toMove value
"""


# o(n) in time | o(1) in space
def moveElementToEnd(array, toMove):
    l = 0
    r = len(array) - 1
    while l < r:
        while array[r] == toMove and l<r:
            r-=1
        if array[l] == toMove:
            array[l] = array[r]
            array[r] = toMove
        l+=1
    return array
