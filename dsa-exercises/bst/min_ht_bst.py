"""
input sorted array: [1, 2, 5, 7, 10, 13, 14, 15, 22]
output: bst with min ht
trick: use binary search to find the middle element and then 
recursively call the function on the left and right subarrays
"""


def generate_seq(arr, left_off, right_off, narr):
    if right_off < left_off:
        return

    m = left_off + int((right_off - left_off)/2)
    narr.append(arr[m])
    generate_seq(arr, left_off, m-1, narr)
    generate_seq(arr, m+1, right_off, narr)
    return narr

# o(n) in time | o(n) in space
def minHeightBst(array):
    narr = []
    left_off = 0
    right_off = len(array)-1
    narr = generate_seq(array, left_off, right_off, narr)
    bst = BST(narr[0])
    for i in range(1, len(narr)):
        bst.insert(narr[i])
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
