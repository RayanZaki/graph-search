from Path import Path
from graph import Graph
from node import Node


def get_path(node, graph, p=Path(recursive=True)):
    """
    Recursive Function to climb up the Parents of the
    Goal node and return the The Goal Path
    Parameters
    ----------
    node
    graph
    p

    Returns
    -------

    """
    p.weighted = graph.weighted
    print(p.weighted)
    if node.parent is None:
        return p
    p.insert(node.parent, node, graph.get(node.parent, node))
    return get_path(node.parent, graph, p)


def breadth_first(node: Node, goal: Node, g: Graph):
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

    # Initialize the goal path
    goal_path = Path(weighted=g.weighted)

    # initialize the visited array
    visited = [node]
    # initialize the search FIFO queue
    queue = [node]

    p = None
    # initialize the parent to None
    while queue:  # is not empty
        s = queue.pop(0)
        # print(s)
        # print("parent: ", s.parent)
        # print("p: ", p)

        # if p != s.parent:
        # p = s.parent
        # try:
        # print("inseted: ", p, s)
        # goal_path.insert(p, s)
        # except IncompletePath:
        #     pass
        # else:
        #     print("remove last")
        #     goal_path.remove_last()

        for i in g.adjacent(s):
            i.parent = s
            if i == goal:
                # try:
                #     goal_path.insert(s, i)
                # except IncompletePath:
                #     pass
                return get_path(i, g)
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return Path()
