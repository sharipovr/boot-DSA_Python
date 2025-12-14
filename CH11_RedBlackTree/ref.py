def ref_implementation(tree, val):
    """
    Reference implementation of insert for Red-Black Tree.
    Since we're just doing basic insert (no rebalancing yet), 
    this matches the same logic as the student implementation.
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

