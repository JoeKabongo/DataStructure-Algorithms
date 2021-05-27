from Graph import Graph
from collections import deque


def route_between_node(graph: Graph, S, E):
    """ Is there a path between S and E"""

    # get adjency list
    adj = graph.get_adjency_list()

    # queue
    queue = deque()
    queue.append(S)

    # keep track of visited nodes
    visited = set()
    visited.add(S)

    while len(queue) > 0:
        node = queue.popleft()
        if node == E:
            return True

        neighbors = adj.get(node, [])
        for edge in neighbors:
            destination = edge.destination
            if destination not in visited:  # only consider not if not visted before
                visited.add(destination)
                queue.append(destination)

    return False
