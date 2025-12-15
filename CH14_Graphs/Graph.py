class Graph:
    def __init__(self, num_vertices):
        """
        Initializes a graph with num_vertices vertices.
        Creates an adjacency matrix representation.
        """
        # Create a new data member called graph, it should be an empty list
        self.graph = []
        
        # Fill the graph with n lists, where n is the number of vertices in the graph
        # Each of these lists should contain n False values
        for i in range(num_vertices):
            self.graph.append([False] * num_vertices)

    def add_edge(self, u, v):
        """
        Adds an edge between vertices u and v.
        Since the graph is undirected, sets both graph[u][v] and graph[v][u] to True.
        """
        # It adds an edge to the graph by setting the corresponding cells to True
        # There are two cells in the matrix for each pair of vertices (undirected graph)
        self.graph[u][v] = True
        self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
