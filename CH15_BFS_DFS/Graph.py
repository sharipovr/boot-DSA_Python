class Graph:
    def breadth_first_search(self, v):
        """
        Performs breadth-first search starting from vertex v.
        Returns all vertices in the order they were visited.
        
        Args:
            v: The starting vertex (string)
        
        Returns:
            List of vertices in the order they were discovered
        """
        # Initialize tracking structures
        # Create a list to track visited vertices
        visited = []
        
        # Create a list to use as a queue for vertices waiting to be explored
        queue = []
        
        # Begin the search: Add the starting vertex to the queue
        queue.append(v)
        
        # Process the queue until empty
        while queue:
            # Remove the first vertex from the queue and add it to the visited list
            current = queue.pop(0)
            visited.append(current)
            
            # Get a sorted list of this vertex's neighbors (for stable ordering)
            neighbors = sorted(self.graph.get(current, set()))
            
            # For each neighbor, if it is neither visited nor queued, add it to the queue
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
        
        # When complete, return the visited list containing vertices in the order they were discovered
        return visited

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
