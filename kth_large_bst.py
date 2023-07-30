"""
find kth largest value in BST
input: tree, k
trick: in order traversal and return kth element from the end
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_arr(tree, arr):
    if tree.left:
        in_order_arr(tree.left, arr)
    arr.append(tree.value)
    if tree.right:
        in_order_arr(tree.right, arr)
    return arr

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    return in_order_arr(tree,[])[-k]
