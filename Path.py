from exceptions import IncompletePath, NoneDeterministicPath, CyclicPath
from graph import Graph
from node import Node


class Path(Graph):
    """
    Class to define a path from two nodes
    It is a Directed Graph that accepts one only
    one transition from each node and all nodes should be connected
    in the same order
    """

    def __init__(self, obj=None, recursive=False, weighted=False):
        Graph.__init__(self, weighted=weighted, directed=True, recursive=recursive)
        self._graph = {}
        if obj:  # If object is passed
            visited = []
            # Initialize an array of all states that have been traversed
            # Initialize the next variable
            # To the first State in the path
            # This variable remembers the last state visited
            next_state = list(obj.keys())[0][0]
            for transition in obj:
                # Check the formatting
                if isinstance(transition, tuple):
                    # If the current state is already visited
                    # Or is not the last state raise error
                    if transition[0] in visited:
                        raise NoneDeterministicPath
                    elif transition[0] != next_state:
                        raise IncompletePath
                    else:
                        # Build the graph
                        self._graph[transition] = obj[transition]
                        # push the previous state in the visited array
                        visited.append(transition[0])
                        # Remember the current state
                        next_state = transition[1]

    def insert(self, start, end, w=None):
        start = Node.params_to_node(start)
        end = Node.params_to_node(end)
        # Array to store all keys of the graph
        keys = list(self._graph.keys())
        if not self._recursive:
            if keys:  # If the keys array is not empty
                current = keys[-1][1]
            else:
                current = start
            # list all the visited states
            # those are the first
            # elements of the tuple
            visited = [i[0] for i in keys]
            if start != current:
                raise IncompletePath
            elif end in visited:
                raise CyclicPath
        else:
            if keys:  # If the keys array is not empty
                current = keys[0][0]
            else:
                current = end

            visited = [i[1] for i in keys]
            if end != current:
                raise IncompletePath
            elif start in visited:
                raise CyclicPath

        Graph.insert(self, start, end, w)

    def remove_last(self):
        """
         Removes the Last edge
        """
        keys = list(self._graph.keys())
        if keys:
            self._graph.pop(keys[-1])
