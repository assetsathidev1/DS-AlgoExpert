"""
Given a binary tree, find the branch sums of the tree.
a branch is defined as a path from the root node to a leaf node.
example:
        1
    2       3   
  4    5   6     7
8  9 10 11 12
output: [15, 16, 18, 10, 11]
timetaken: 20mins (first principles)
"""



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(N) in space and time
def traverseAndSum(node, prev_sum, arr):
    if not node:
        return arr
    if not node.left and not node.right:
        arr.append(prev_sum+node.value)
        return arr
    traverseAndSum(node.left, prev_sum+node.value, arr)
    traverseAndSum(node.right, prev_sum+node.value, arr)
    return arr

def traverse(node, arr):
    if not node:
        return arr
    arr.append(node.value)
    traverse(node.left, arr)
    traverse(node.right, arr)
    return arr

def branchSums(root):
    arr = []
    if root:
        prev_sum = 0
        # traverse(root, arr)
        arr = traverseAndSum(root, prev_sum, arr)
    # print(arr)
    return arr
