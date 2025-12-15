class Graph:
    def __init__(self, num_vertices=None):
        """
        Initializes a graph using an adjacency list representation.
        Creates an empty dictionary where vertices map to sets of connected vertices.
        Note: num_vertices parameter is kept for compatibility but not used with adjacency lists.
        """
        # It should create an empty dictionary called graph as a data member
        self.graph = {}

    def add_edge(self, u, v):
        """
        Adds an edge between vertices u and v.
        Uses adjacency list representation where vertices map to sets of connected vertices.
        """
        # Handle the case where a set for a vertex doesn't exist yet
        if u not in self.graph:
            self.graph[u] = set()
        if v not in self.graph:
            self.graph[v] = set()
        
        # Be sure to map both vertices to each other, it's a bidirectional edge
        self.graph[u].add(v)
        self.graph[v].add(u)

    def add_node(self, node):
        """
        Adds a node (vertex) to the graph with no connections.
        If the node already exists, it will not overwrite existing connections.
        """
        if node not in self.graph:
            self.graph[node] = set()

    def adjacent_nodes(self, node):
        """
        Returns a set of all nodes adjacent to the given node.
        
        Args:
            node: The node (vertex) to get adjacent nodes for
        
        Returns:
            A set of all adjacent nodes, or empty set if node doesn't exist
        """
        # Return the set of adjacent nodes for the given node
        # If the node doesn't exist in the graph, return an empty set
        return self.graph.get(node, set())

    def unconnected_vertices(self):
        """
        Returns a list of vertices that have no connections.
        A vertex with no edges will have an empty set as its value.
        
        Returns:
            A list of vertices (integers) with no connections
        """
        # Find vertices where the set of adjacent nodes is empty
        unconnected = []
        for vertex, adjacent_set in self.graph.items():
            if len(adjacent_set) == 0:
                unconnected.append(vertex)
        return unconnected

    # don't touch below this line

    def edge_exists(self, u, v):
        # Check if vertex u exists in the graph
        if u not in self.graph:
            return False
        # Check if vertex v is in the set of vertices connected to u
        return v in self.graph[u]
