"""
input: 3 nodes in a BST
output: boolean indicating if the 3 nodes are in the same branch of the BST

- node 2 is the middle node
- node 1 or node 3 has to be ancestor of node 2
- node 1 or node 3 has to be descendant of node 2
Trick: started by searching descendants of node 2, to find node 1 or node 3
if either found, using the other searching for node 2
if all found, break and return True

Might be a better way to do this, but this is what I came up with
reasonable time and space complexity, so not optimising further
"""



# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# o(h) in time | o(1) in space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    currentNode = nodeTwo
    node1_is_child = False
    while currentNode != None:
        if nodeOne.value < currentNode.value:
           currentNode = currentNode.left 
        elif nodeOne.value > currentNode.value:
            currentNode = currentNode.right
        else:
            node1_is_child = True
            break

    node3_is_child = False
    currentNode = nodeTwo
    # print("nodeTwo after first check:", nodeTwo.value)
    while currentNode != None:
        if nodeThree.value < currentNode.value:
           currentNode = currentNode.left 
        elif nodeThree.value > currentNode.value:
            currentNode = currentNode.right
        else:
            node3_is_child = True
            break
    
    # print("node3_is_child:", node3_is_child, "node1_is_child:", node1_is_child)
    if not node3_is_child and not node1_is_child:
        return False
    
    if node1_is_child: # check if n3 is ancestor of n2
        currentNode = nodeThree
        node2_is_child = False
        while currentNode != None:
            if nodeTwo.value < currentNode.value:
               currentNode = currentNode.left 
            elif nodeTwo.value > currentNode.value:
                currentNode = currentNode.right
            else:
                node2_is_child = True
                break
        if node2_is_child:
            return True
        else:
            return False

    if node3_is_child: # check if n1 is ancestor of n2
        currentNode = nodeOne
        node2_is_child = False
        while currentNode != None:
            if nodeTwo.value < currentNode.value:
               currentNode = currentNode.left 
            elif nodeTwo.value > currentNode.value:
                currentNode = currentNode.right
            else:
                node2_is_child = True
                break
        if node2_is_child:
            return True
        else:
            return False
    
    return False
