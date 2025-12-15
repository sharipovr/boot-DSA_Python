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

    # don't touch below this line

    def edge_exists(self, u, v):
        # Check if vertex u exists in the graph
        if u not in self.graph:
            return False
        # Check if vertex v is in the set of vertices connected to u
        return v in self.graph[u]
