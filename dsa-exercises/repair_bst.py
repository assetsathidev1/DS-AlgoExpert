"""
{
  "nodes": [
    {"id": "10", "left": "7", "right": "20", "value": 10},
    {"id": "7", "left": "3", "right": "12", "value": 7},
    {"id": "3", "left": "2", "right": null, "value": 3},
    {"id": "2", "left": null, "right": null, "value": 2},
    {"id": "12", "left": null, "right": null, "value": 12},
    {"id": "20", "left": "8", "right": "22", "value": 20},
    {"id": "8", "left": null, "right": "14", "value": 8},
    {"id": "22", "left": null, "right": null, "value": 22},
    {"id": "14", "left": null, "right": null, "value": 14}
  ],
  "root": "10"
}

{
  "nodes": [
    {"id": "2", "left": null, "right": "1", "value": 2},
    {"id": "1", "left": null, "right": null, "value": 1}
  ],
  "root": "2"
}

trick is to: go in order, and find if prev node is gt than current. 
since we know there are only 2 that are off place, keep track of them in 2 variables. 
whenever we find the pattern off, we update node1 to be prev (if we did not find n1 already) and node2 to be current.

Another approach is: 
go in order, sort the sequence (o-nlogn) and then find the 2 nodes that are off place.
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""partially correct"""
def get_in_order(tree, arr=[]):
    if tree.left:
        get_in_order(tree.left, arr)
    arr.append(tree.value)
    if tree.right:
        get_in_order(tree.right, arr)

def validateBst(tree, min_val=-999999, max_val=999999, arr=[]):
    if tree is None:
        return
    if tree.value < min_val:
        arr.append(tree)
    if tree.value >= max_val:
        arr.append(tree)
    l_valid = validateBst(tree.left, min_val, tree.value, arr)
    r_valid = validateBst(tree.right, tree.value, max_val, arr)


def repairBst(tree):
    swap_v = []
    validateBst(tree, -999999, 999999, swap_v)
    print("swap_v:", [s.value for s in swap_v])

    if len(swap_v) == 1:
        # print("swap_v:", swap_v[0].value)
        # only true in 2 node case, just swap node value
        if tree.left and tree.left.value == swap_v[0].value:
            temp = swap_v[0].value
            tree.left.value = tree.value
            tree.value = temp
            
        if tree.right and tree.right.value == swap_v[0].value:
            temp = swap_v[0].value
            tree.right.value = tree.value
            tree.value = temp

    elif len(swap_v)>=2:
        # case when tree is larger, search for either value
        temp = swap_v[1].value
        swap_v[1].value = swap_v[0].value
        swap_v[0].value = temp
    return tree



"""Simpler correct solution"""
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# o(n) in time and o(h) in space (call stack)
def repairBst(tree):
    node_one = None
    node_two = None
    prev = None

    def in_order(node):
        nonlocal node_one, node_two, prev
        if node is None:
            return
        in_order(node.left)

        if prev is not None and prev.value > node.value:
            if node_one is None:
                node_one = prev
            node_two = node
        
        prev = node
        in_order(node.right)
    
    in_order(tree)
    # print("n1:", node_one.value, "n2:", node_two.value)


    node_one.value, node_two.value = node_two.value, node_one.value
    
    return tree
