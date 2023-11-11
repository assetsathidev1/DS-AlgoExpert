"""
Given a graph traverse it in bfs manner
input graph:
        A
      /   \
     B     C
    / \   / \
   D   E F   G
  / \     \
 H   I     J

output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

tt: 25mins; 10-15 mins took coz i was trying to solve through reursion.
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        if len(array) == 0:
            queue = [self]
        while queue:
            node = queue.pop(0)
            array.append(node.name)
            for child in node.children:
                queue.append(child)
        return array

