from exceptions import ExistingTransition, InvalidTransition
from node import Node


class Graph:
    """
    Class to represent a graph
    the format of the graph is as follows:
    graph = {
        {A, B}: w1,
        {A, C}: w2
    }
    A, B, C: are nodes
    w1, w2: are weights
    {A, B}: is an undirected transition
    """

    def __init__(self, obj=None, weighted=True, directed=False, recursive=False):
        """
        By default, the graph is not directed
        If obj passed, directed parameter will override the formulation
        """

        self._recursive = recursive
        self._graph = {}
        self._DIRECTED = directed
        self._WEIGHTED = weighted

        if obj:
            for transition in obj:
                if isinstance(transition, tuple):
                    self._graph[transition] = obj[transition]
                    self._DIRECTED = True
                elif isinstance(transition, frozenset):
                    self._graph[transition] = obj[transition]
                    self._DIRECTED = False
                else:
                    raise Exception("Invalid object for constructing graph instance")
            if not directed:
                self.to_non_directed()

    @property
    def graph(self):
        return self._graph

    @property
    def weighted(self):
        return self._WEIGHTED
    
    @weighted.setter
    def weighted(self, w):
        if not isinstance(w, (bool)):
            raise TypeError("Type must be numeric")
        else:
            self._WEIGHTED = w

    def get(self, parent, node):
        if not self._WEIGHTED:
            return
        if self._DIRECTED:
            return self._graph.get((parent, node))
        else:
            return self._graph.get(frozenset({parent, node}))

    def insert(self, a: Node, b: Node, w=None):
        """
        Insert a transition:
            for a directed graph, the order of a and b matters
        """

        # By default, the weight is 0
        a = Node.params_to_node(a)
        b = Node.params_to_node(b)

        if a == b:
            raise InvalidTransition

        if self._DIRECTED:
            if self._graph.get((a, b)):
                raise ExistingTransition
            if self._WEIGHTED:
                self._graph[(a, b)] = 0 if w is None else w
            else:
                self._graph[(a, b)] = None
        else:
            if self._graph.get(frozenset({a, b})):
                raise ExistingTransition
            self._graph[frozenset({a, b})] = 0 if w is None else w

    def remove(self, a: Node, b: Node):
        """
            Remove a transition:
                for directed graph. the order matters
        """
        if not self._DIRECTED:
            self._graph.pop(frozenset({a, b}))
        else:
            self._graph.pop((a, b))

    def to_non_directed(self):
        """
        Transform a directed graph to a non-directed graph
        """

        if not self._DIRECTED:
            return
        else:
            self._DIRECTED = False
            temp = self._graph
            self._graph = {}
            for transition in temp:
                if isinstance(transition, tuple):
                    self._graph[frozenset(transition)] = temp[transition]
            return self._graph

    def adjacent(self, node: Node):
        if not self._DIRECTED:
            for transition in self._graph:
                if node in transition:
                    tr = tuple(transition)
                    yield tr[0] if tr[0] != node else tr[1]
        else:
            for transition in self._graph:
                if node == transition[0]:
                    yield transition[1]

    def __str__(self):
        if self._recursive:
            keys = list(self._graph)
            keys.reverse()
        else:
            keys = self._graph
        string = "{ "
        if not self._DIRECTED:
            if self._WEIGHTED:
                for transition in keys:
                    tr = list(transition)
                    string += "\n\t{ " + tr[0].__str__() + ", " + tr[1].__str__() + " }: " + self._graph[
                        transition].__str__() + ","
            else:
                for transition in keys:
                    transition = list(transition)
                    string += "\n\t{ " + transition[0].__str__() + ", " + transition[1].__str__() + " },"

        else:
            if self._WEIGHTED:
                for transition in keys:
                    string += "\n\t( " + transition[0].__str__() + ", " + transition[1].__str__() + " ): " + \
                              self._graph[transition].__str__() + ","
            else:
                for transition in keys:
                    string += "\n\t( " + transition[0].__str__() + ", " + transition[1].__str__() + " ),"

        string = string[:-1]
        string += "\n}"
        return string
