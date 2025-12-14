class BSTNode:
    def delete(self, val):
        # Check if the current node is empty
        if self.val is None:
            return None
        
        # If the value to delete is less than the current node's value
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
            return self
        
        # If the value to delete is greater than the current node's value
        if val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
            return self
        
        # If the value to delete equals the current node's value
        # Case 1: No right child, return left child
        if self.right is None:
            return self.left
        
        # Case 2: No left child, return right child
        if self.left is None:
            return self.right
        
        # Case 3: Both children exist - find successor (smallest in right subtree)
        # Find the smallest node in the right subtree
        successor = self.right
        while successor.left is not None:
            successor = successor.left
        
        # Replace current node's value with successor's value
        self.val = successor.val
        
        # Delete the successor node from the right subtree
        self.right = self.right.delete(successor.val)
        
        return self

    # don't touch below this line
    def get_min(self):
        if self.left is None:
            return self.val
        return self.left.get_min()

    def get_max(self):
        if self.right is None:
            return self.val
        return self.right.get_max()

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return
        
        if val < self.val and self.left is None:
            self.left = BSTNode(val)
        elif val < self.val:
            return self.left.insert(val)
        
        if val > self.val and self.right is None:
            self.right = BSTNode(val)
        elif val > self.val:
            return self.right.insert(val)