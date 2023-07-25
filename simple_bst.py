
class TreeNode:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value) 
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    
    def __str__(self) -> str:
        return f"v: {self.value}"
    
    def inorder_traversal(self):
        """ 
        go to left most leaf node and then print and then go right
        prints in ascending order
        """
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.value)
        if self.right is not None:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        """ 
        print value, go to left most leaf node and then go right
        """
        print(self.value)
        if self.left is not None:
            self.left.preorder_traversal()
        if self.right is not None:
            self.right.preorder_traversal()
    
    def postorder_traversal(self):
        """ 
        go to left most leaf node and then go right and then print
        """
        if self.left is not None:
            self.left.postorder_traversal()
        if self.right is not None:
            self.right.postorder_traversal()
        print(self.value)

    def is_exists(self, value):
        # avg case time complexity logn; worst case n
        # print(self.value)
        if value == self.value:
            return True
        if value < self.value:
            if self.left:
                return self.left.is_exists(value)
            else:
                return False
        else:
            if self.right:
                return self.right.is_exists(value)
            else:
                return False

tree = TreeNode(11)
tree.insert(5)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(19)
tree.insert(20)
tree.insert(21)
tree.insert(27)
tree.insert(3)
tree.insert(4)
tree.insert(1)
tree.insert(17)
tree.insert(16)

# print(tree.right.left.left)
# tree.inorder_traversal()
# tree.preorder_traversal()
# tree.postorder_traversal()
print(tree.is_exists(16))