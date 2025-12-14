def ref_impl_ins(tree, val):
    """
    Reference implementation of insert for Red-Black Tree with full balancing.
    This is the complete implementation including fix_insert.
    """
    from RBNode import RBNode
    
    # Step 1: Create the new_node
    new_node = RBNode(val)
    new_node.parent = None
    new_node.left = tree.nil
    new_node.right = tree.nil
    new_node.red = True
    
    # Step 2: Find the parent
    parent = None
    current = tree.root
    
    while current != tree.nil:
        parent = current
        if val < current.val:
            current = current.left
        elif val > current.val:
            current = current.right
        else:
            # Duplicate, return
            return
    
    # Step 3: Insert the new_node
    new_node.parent = parent
    
    if parent is None:
        tree.root = new_node
    else:
        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
    
    # Step 4: Fix the red-black tree properties
    ref_fix_insert(tree, new_node)


def ref_fix_insert(tree, current):
    """
    Reference implementation of fix_insert for Red-Black Tree.
    """
    # While current is not the root and has a red parent
    while current != tree.root and current.parent.red:
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
                    ref_rotate_right(tree, current)
                    # Set parent to be the current node's parent
                    parent = current.parent
                
                # Recolor the parent to black
                parent.red = False
                # Recolor the grandparent to red
                grandparent.red = True
                # Rotate left around the grandparent
                ref_rotate_left(tree, grandparent)
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
                    ref_rotate_left(tree, current)
                    # Set parent to be the current node's parent
                    parent = current.parent
                
                # Recolor the parent to black
                parent.red = False
                # Recolor the grandparent to red
                grandparent.red = True
                # Rotate right around the grandparent
                ref_rotate_right(tree, grandparent)
    
    # Recolor the root to black
    tree.root.red = False


def ref_rotate_left(tree, pivot_parent):
    """
    Reference implementation of rotate_left.
    """
    if pivot_parent == tree.nil or pivot_parent.right == tree.nil:
        return
    
    pivot = pivot_parent.right
    pivot_parent.right = pivot.left
    
    if pivot.left != tree.nil:
        pivot.left.parent = pivot_parent
    
    pivot.parent = pivot_parent.parent
    
    if pivot_parent.parent is None:
        tree.root = pivot
    elif pivot_parent == pivot_parent.parent.left:
        pivot_parent.parent.left = pivot
    else:
        pivot_parent.parent.right = pivot
    
    pivot.left = pivot_parent
    pivot_parent.parent = pivot


def ref_rotate_right(tree, pivot_parent):
    """
    Reference implementation of rotate_right.
    """
    if pivot_parent == tree.nil or pivot_parent.left == tree.nil:
        return
    
    pivot = pivot_parent.left
    pivot_parent.left = pivot.right
    
    if pivot.right != tree.nil:
        pivot.right.parent = pivot_parent
    
    pivot.parent = pivot_parent.parent
    
    if pivot_parent.parent is None:
        tree.root = pivot
    elif pivot_parent == pivot_parent.parent.left:
        pivot_parent.parent.left = pivot
    else:
        pivot_parent.parent.right = pivot
    
    pivot.right = pivot_parent
    pivot_parent.parent = pivot


# Alias for backward compatibility
def ref_implementation(tree, val):
    ref_impl_ins(tree, val)


def ref_inorder(node, result):
    """
    Performs an inorder traversal of the RBTree and collects values in result list.
    Returns the result list with values in sorted order (left, root, right).
    Handles nil nodes correctly (nil nodes have val = None).
    """
    # Check if node is not nil (nil nodes have val = None)
    if node is not None and node.val is not None:
        # Traverse left subtree (only if left is not nil)
        if node.left is not None and node.left.val is not None:
            ref_inorder(node.left, result)
        # Visit current node
        result.append(node.val)
        # Traverse right subtree (only if right is not nil)
        if node.right is not None and node.right.val is not None:
            ref_inorder(node.right, result)
    return result

