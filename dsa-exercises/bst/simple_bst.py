
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
    
    def remove(self, value, parent_node=None):
        """
        function to remove an element from a bst
        """
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    # two children case
                    current_node.value = current_node.right.find_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        print("edgest case!!")
                        break
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    def find_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    # def find_max_height(self):
    #     if self.left is None and self.right is None:
    #         return 0
    #     elif self.left is None:
    #         return 1 + self.right.find_max_height()
    #     elif self.right is None:
    #         return 1 + self.left.find_max_height()
    #     else:
    #         return 1 + max(self.left.find_max_height(), self.right.find_max_height())
    
    def find_max_height(self):
        if self.left is None and self.right is None:
            return 0
        ld = 0
        rd = 0
        if self.left:
            ld = 1 + self.left.find_max_height()
        if self.right:
            rd = 1 + self.right.find_max_height()
        return ld if ld > rd else rd


tree = TreeNode(11)
tree.insert(5)
tree.insert(19)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(17)
tree.insert(16)
tree.insert(20)
tree.insert(21)
tree.insert(27)
print(tree.right.right.right.right)
print(tree.find_max_height())


# print(tree.find_min_value())
# print(tree.left.left.left)
# tree.inorder_traversal()
# tree.preorder_traversal()
# tree.postorder_traversal()
# print(tree.is_exists(16))
# print("------ rem ----")
# tree.remove(1)
# tree.inorder_traversal()

# tree.remove(5)
# tree.inorder_traversal()

# tree.remove(11)
# tree.inorder_traversal()

# tree.remove(99)
# tree.inorder_traversal()