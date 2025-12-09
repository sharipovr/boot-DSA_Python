class BSTNode:
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