"""
Implement DFS on a Acyclic Graph
Time taken: 10 Mins (from first principles)
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # O(V+E) in time, O(V) in Space
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
