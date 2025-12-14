class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Step 1: Create the new_node
        new_node = RBNode(val)
        new_node.parent = None  # Will be set later
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # New nodes are red by default
        
        # Step 2: Find the parent of the new_node
        parent = None
        current = self.root
        
        while current != self.nil:
            parent = current
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                # Duplicate value, return early
                return
        
        # Step 3: Insert the new_node by setting the parent's child
        new_node.parent = parent
        
        # If parent is None, we are dealing with a new root
        if parent is None:
            self.root = new_node
        else:
            # Compare values and set parent's left or right child
            if val < parent.val:
                parent.left = new_node
            else:
                parent.right = new_node
        
        # Step 4: Fix the red-black tree properties
        self.fix_insert(new_node)

    def fix_insert(self, current):
        """
        Fixes the red-black tree properties after insertion.
        Maintains the red-black tree invariants through recoloring and rotations.
        """
        # While current is not the root and has a red parent
        while current != self.root and current.parent.red:
            # Identify parent, grandparent, and uncle
            parent = current.parent
            grandparent = parent.parent
            
            # If parent is a right child of the grandparent
            if parent == grandparent.right:
                uncle = grandparent.left
                
                # Case 1: If uncle is red
                if uncle.red:
                    # Recolor uncle and parent to black
                    uncle.red = False
                    parent.red = False
                    # Recolor grandparent to red
                    grandparent.red = True
                    # Move up the tree by making current node the grandparent
                    current = grandparent
                # Case 2: If uncle is black
                else:
                    # If current node is the left child of the parent
                    if current == parent.left:
                        # Move up the tree by making current node the parent
                        current = parent
                        # Rotate right around the current node
                        self.rotate_right(current)
                        # Set parent to be the current node's parent
                        parent = current.parent
                    
                    # Recolor the parent to black
                    parent.red = False
                    # Recolor the grandparent to red
                    grandparent.red = True
                    # Rotate left around the grandparent
                    self.rotate_left(grandparent)
            # If parent is a left child of the grandparent
            else:
                uncle = grandparent.right
                
                # Case 1: If uncle is red
                if uncle.red:
                    # Recolor uncle and parent to black
                    uncle.red = False
                    parent.red = False
                    # Recolor grandparent to red
                    grandparent.red = True
                    # Move up the tree by making current node the grandparent
                    current = grandparent
                # Case 2: If uncle is black
                else:
                    # If current node is the right child of the parent
                    if current == parent.right:
                        # Move up the tree by making current node the parent
                        current = parent
                        # Rotate left around the current node
                        self.rotate_left(current)
                        # Set parent to be the current node's parent
                        parent = current.parent
                    
                    # Recolor the parent to black
                    parent.red = False
                    # Recolor the grandparent to red
                    grandparent.red = True
                    # Rotate right around the grandparent
                    self.rotate_right(grandparent)
        
        # Recolor the root to black
        self.root.red = False

    def rotate_left(self, pivot_parent):
        """
        Rotates the tree left around pivot_parent.
        pivot_parent's right child (pivot) moves up to replace pivot_parent.
        """
        # If pivot_parent is nil or pivot_parent's right child is nil, return
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        
        # Let pivot be pivot_parent's right child
        pivot = pivot_parent.right
        
        # Set pivot_parent's right child to be pivot's left child
        pivot_parent.right = pivot.left
        
        # If pivot's left child isn't a nil leaf node, set pivot's left child's parent to pivot_parent
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
        
        # Set pivot's parent to pivot_parent's parent
        pivot.parent = pivot_parent.parent
        
        # If pivot_parent is the root, set the root to pivot
        if pivot_parent.parent is None:
            self.root = pivot
        # Otherwise, if pivot_parent is its parent's left child, set parent's left child to pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        # Otherwise, if pivot_parent is its parent's right child, set parent's right child to pivot
        else:
            pivot_parent.parent.right = pivot
        
        # Set pivot's left child to be pivot_parent
        pivot.left = pivot_parent
        
        # Set pivot_parent's parent to be pivot
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        """
        Rotates the tree right around pivot_parent.
        pivot_parent's left child (pivot) moves up to replace pivot_parent.
        """
        # If pivot_parent is nil or pivot_parent's left child is nil, return
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        
        # Let pivot be pivot_parent's left child
        pivot = pivot_parent.left
        
        # Set pivot_parent's left child to be pivot's right child
        pivot_parent.left = pivot.right
        
        # If pivot's right child isn't a nil leaf node, set pivot's right child's parent to pivot_parent
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent
        
        # Set pivot's parent to pivot_parent's parent
        pivot.parent = pivot_parent.parent
        
        # If pivot_parent is the root, set the root to pivot
        if pivot_parent.parent is None:
            self.root = pivot
        # Otherwise, if pivot_parent is its parent's left child, set parent's left child to pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        # Otherwise, if pivot_parent is its parent's right child, set parent's right child to pivot
        else:
            pivot_parent.parent.right = pivot
        
        # Set pivot's right child to be pivot_parent
        pivot.right = pivot_parent
        
        # Set pivot_parent's parent to be pivot
        pivot_parent.parent = pivot
