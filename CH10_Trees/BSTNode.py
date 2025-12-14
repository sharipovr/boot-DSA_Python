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

    def preorder(self, visited):
        """
        Preorder traversal: Visit ROOT → LEFT → RIGHT
        
        Think of it as: "Say hello to the parent, then explore its children"
        
        Example tree:
            4
           / \
          2   7
         /   /
        1   6
        
        Result: [4, 2, 1, 7, 6]
        """
        # STEP 1: Visit current node FIRST (if it has a value)
        # This is the "pre" part - we visit BEFORE children
        if self.val is not None:
            visited.append(self.val)
        
        # STEP 2: Recursively explore LEFT subtree
        # We pass the same 'visited' list so all nodes add to it
        if self.left is not None:
            self.left.preorder(visited)  # Call ourselves on left child
        
        # STEP 3: Recursively explore RIGHT subtree
        # After left is done, we explore the right side
        if self.right is not None:
            self.right.preorder(visited)  # Call ourselves on right child
        
        # STEP 4: Return the list (now contains all visited nodes)
        return visited

    def postorder(self, visited):
        """
        Postorder traversal: Visit LEFT → RIGHT → ROOT
        
        Think of it as: "Explore all children first, then visit the parent"
        
        Example tree:
            4
           / \
          2   7
         /   /
        1   6
        
        Result: [1, 2, 6, 7, 4]
        """
        # STEP 1: Recursively explore LEFT subtree first
        if self.left is not None:
            self.left.postorder(visited)  # Call ourselves on left child
        
        # STEP 2: Recursively explore RIGHT subtree second
        if self.right is not None:
            self.right.postorder(visited)  # Call ourselves on right child
        
        # STEP 3: Visit current node LAST (if it has a value)
        # This is the "post" part - we visit AFTER children
        if self.val is not None:
            visited.append(self.val)
        
        # STEP 4: Return the list (now contains all visited nodes)
        return visited

    def inorder(self, visited):
        """
        Inorder traversal: Visit LEFT → ROOT → RIGHT
        
        Think of it as: "Explore left children, visit parent, then explore right children"
        
        For a Binary Search Tree, this produces values in SORTED ORDER!
        
        Example tree:
            4
           / \
          2   7
         /   /
        1   6
        
        Result: [1, 2, 4, 6, 7] (sorted order!)
        """
        # STEP 1: Recursively explore LEFT subtree first
        if self.left is not None:
            self.left.inorder(visited)  # Call ourselves on left child
        
        # STEP 2: Visit current node (if it has a value)
        # This is the "in" part - we visit IN BETWEEN children
        if self.val is not None:
            visited.append(self.val)
        
        # STEP 3: Recursively explore RIGHT subtree last
        if self.right is not None:
            self.right.inorder(visited)  # Call ourselves on right child
        
        # STEP 4: Return the list (now contains all visited nodes in sorted order)
        return visited

    def exists(self, val):
        """
        Checks if a value exists in the BST.
        Returns True if found, False otherwise.
        
        Uses the BST property: left < root < right
        to efficiently search by going left or right.
        """
        # If current node is empty, value doesn't exist here
        if self.val is None:
            return False
        
        # Found it! Value matches current node
        if self.val == val:
            return True
        
        # Value is less than current node, search left subtree
        if val < self.val:
            if self.left is not None:
                return self.left.exists(val)
            return False
        
        # Value is greater than current node, search right subtree
        if val > self.val:
            if self.right is not None:
                return self.right.exists(val)
            return False

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