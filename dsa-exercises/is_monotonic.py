"""
input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
output: true
input: [1, 2, 3, 2, 5, 6, 7, 9, 8]
output: false
"""

# o(n) in time | o(1) in space
def isMonotonic(array):
    # Write your code here.
    if len(array) == 0 or len(array) == 1:
        return True
    increase = None
    for i in range(len(array)-1):
        d = array[i] - array[i+1]
        if d != 0:
            increase = True if d < 0 else False
    if increase == None:
        return True
    for i in range(len(array)-1):
        d = array[i] - array[i+1]
        if increase is True and d > 0:
            return False
        elif increase is False and d < 0:
            return False
    return True



# o(n) in time | o(1) in space 
def isMonotonic(array):  # much cleaner solution
    # Write your code here.
    inc = True
    dec = True
    for i in range(len(array)-1):
        inc = inc and array[i] <= array[i+1]
        dec = dec and array[i] >= array[i+1]
    return inc or dec
