"""
Reconstruct BST from pre-order traversal
"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# o(nlogn) time | o(n) space
def insert_in_bst(tree, value):
    if value < tree.value:
        if tree.left is None:
            tree.left = BST(value)
        else:
            insert_in_bst(tree.left, value)
    elif value >= tree.value:
        if tree.right is None:
            tree.right = BST(value)
        else:
            insert_in_bst(tree.right, value)

def reconstructBst(preOrderTraversalValues):
    tree = BST(preOrderTraversalValues[0])
    for i in preOrderTraversalValues[1:]:
        insert_in_bst(tree, i)
    return tree
    # return None
