from node import Node


class LinkedList:

    def add_to_head(self, node):
        if self.head is None:
            self.tail = node

        node.set_next(self.head)
        self.head = node        
    
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
