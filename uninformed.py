from Path import Path
from graph import Graph
from node import Node


def get_path(node, graph, p=None):
    """
    Recursive Function to climb up the Parents of the
    Goal node and return the Goal Path
    """
    # Make the Path follow the graph
    #  weighted => Path weighted
    if p is None:
        p = Path(recursive=True)

    p.weighted = graph.weighted

    if node.parent is None:  # ie Reached the root
        return p  # Return the path
    print(node.parent, node)
    p.insert(node.parent, node, graph.get(node.parent, node))
    return get_path(node.parent, graph, p)


def breadth_first(node: any, goal: any, g: Graph):
    """
    Parameters
    ----------
    node: The Starting State, It can be of any type
    goal: The Gaol State, It also can be of any type
    g: The Graph that relates both states
    """
    # Adjusting Parameters to be of type Node
    node = Node.params_to_node(node)
    goal = Node.params_to_node(goal)

    if node == goal:
        return Path()
    # initialize the visited array
    visited = [node]
    # initialize the search FIFO queue
    queue = [node]

    while queue:  # is not empty
        s = queue.pop(0)
        for i in g.adjacent(s):
            i.parent = s    # set the parent node attribute on each child
            if i == goal:
                return get_path(i, g)
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return Path()


def depth_first(node: any, goal: any, g: Graph):
    """
    Apply depth first search on Graph g starting from node
    up to goal
    """

    # Adjusting Parameters to be of type Node
    node = Node.params_to_node(node)
    goal = Node.params_to_node(goal)

    if node == goal:
        return Path()
    # initialize the visited array
    visited = [node]
    # initialize the search LIFO queue
    queue = [node]

    while queue:  # is not empty
        s = queue.pop()
        for i in g.adjacent(s):
            i.parent = s
            if i == goal:
                return get_path(i, g)
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return Path()
