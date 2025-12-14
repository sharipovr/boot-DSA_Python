def ref_inorder(bst_node, result):
    """
    Performs an inorder traversal of the BST and collects values in result list.
    Returns the result list with values in sorted order (left, root, right).
    """
    if bst_node is not None and bst_node.val is not None:
        ref_inorder(bst_node.left, result)
        result.append(bst_node.val)
        ref_inorder(bst_node.right, result)
    return result

