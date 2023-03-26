class IncompletePath(Exception):
    pass


class NoneDeterministicPath(Exception):
    pass


class CyclicPath(Exception):
    pass


class ExistingTransition(Exception):
    pass


class InvalidTransition(Exception):
    pass
