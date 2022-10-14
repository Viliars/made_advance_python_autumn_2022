class TicTacError(Exception):
    pass


class IncorrectInput(TicTacError):
    pass


class IncorrectValue(TicTacError):
    pass


class CellOccupied(TicTacError):
    pass
