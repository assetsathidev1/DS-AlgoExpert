"""
Validate if given BST is valid or not
"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_val=-999999, max_val=999999):
    # Write your code here.    
    if tree is None:
        return True
    if tree.value < min_val:
        return False
    if tree.value >= max_val:
        return False
    l_valid = validateBst(tree.left, min_val, tree.value)
    return l_valid and validateBst(tree.right, tree.value, max_val)
    