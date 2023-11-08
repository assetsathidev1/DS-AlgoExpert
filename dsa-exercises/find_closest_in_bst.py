"""
input: 
tree: {
  "nodes": [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": "13", "right": "22", "value": 15},
    {"id": "22", "left": null, "right": null, "value": 22},
    {"id": "13", "left": null, "right": "14", "value": 13},
    {"id": "14", "left": null, "right": null, "value": 14},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": null, "right": null, "value": 5},
    {"id": "2", "left": "1", "right": null, "value": 2},
    {"id": "1", "left": null, "right": null, "value": 1}
  ],
  "root": "10"
}
target: 12
output: 13
"""


"""
diff = None
close_val = None
    
def findClosestValueInBst(tree, target):
    if diff is None:
        close_val = tree.value
        diff = abs(target - close_val)
    if target < tree.value:
        if tree.left:
            return findClosestValueInBst(tree.left, target)
        else:
            return close_val
    else:
        if tree.right:
            return findClosestValueInBst(tree.right, target)
        else:
            return close_val
"""


# o(logn) in time | o(1) in space
def findClosestValueInBst(tree, target):
    diff = None
    close_val = None
    if diff is None:
        close_val = tree.value
        diff = abs(target - close_val)
    current_node = tree
    while current_node is not None:
        if abs(target - current_node.value) < diff:
            diff = abs(target - current_node.value)
            close_val = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return close_val
            
    

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
