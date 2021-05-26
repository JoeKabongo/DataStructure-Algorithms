from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class WeightedGraph:
    """ Undirected graph"""

    def __init__(self):
        self.adj = {}

    def add_edge(self, source, destination, weight):
        """Add edge to graph"""
        if self.adj.get(source) is None:
            self.adj[source] = []
        self.adj[source].append(Edge(source, destination, weight))

    def breath_first_search(self, start):
        """ BFS with a start node"""
        queue = deque()
        visited = set()
        visited.add(start)
        queue.append(start)

        while len(queue) > 0:
            node = queue.popleft()
            neighbors = self.adj.get(node, [])
            print(node)
            for edge in neighbors:
                if edge.destination not in visited:
                    queue.append(edge.destination)
                    visited.add(edge.destination)

    def DFS(self, start):
        """ Depth first serach """
        def helper(node, visited: set):
            print(node)
            visited.add(node)
            neighbors = self.adj.get(node, [])
            for edge in neighbors:
                if edge.destination not in visited:
                    helper(edge.destination, visited)

        helper(start, set())


x = WeightedGraph()
x.add_edge(1, 2, 10)
x.add_edge(1, 5, 1)
x.add_edge(2, 5, 3)
x.add_edge(5, 1, 5)
x.add_edge(5, 10, 3)

x.DFS(1)
