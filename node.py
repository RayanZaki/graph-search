class Node:
    def __init__(self, data: object, parent=None):
        self._data = data
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if not isinstance(parent, Node):
            raise TypeError('Parent Must be a Node instance')
        else:
            self._parent = parent

    @classmethod
    def params_to_node(cls, node):
        """
        Parameters
        ----------
        node: object to be converted to node

        Returns
        -------
        A new Node with object as data
        """

        if not isinstance(node, Node):
            node = Node(node)
        return node

    def __str__(self):
        return self._data.__str__()

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._data == other._data
        elif isinstance(other, type(self._data)):
            return self._data == other
        elif isinstance(other, type(None)):
            return self._data is None
        else:
            raise TypeError('Not the same Type')

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return ord(self._data.__str__()[0])
