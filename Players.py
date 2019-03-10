from abc import ABC, abstractmethod
from Exceptions import BadMoveException

class Player(ABC):

    def __init__(self, name, turn):
        self.name = name
        self.turn = turn
        super().__init__()

    @abstractmethod
    def move(self, board):
        pass

    @abstractmethod
    def think(self):
        pass

    def __str__(self):
        return self.name
        

class HumanPlayer(Player):

    def __init__(self, name, turn):
        super().__init__(name, turn)

    def move(self, board):
        pos = self.think()
        if not board.set_token(pos, self.turn):
            row, col = pos
            raise BadMoveException('row: {} col: {} is a bad move'.format(row, col))
        return board.check_winner(self.turn)

    def think(self):
        pos = input("{} is your turn: ".format(self.name))
        return list(map(int, pos.split()))

class MachinePlayer(Player):

    def __init__(self, name, turn):
        super().__init__(name, turn)

    def move(self, board):
        pos = self.think()
        if not board.set_token(pos, self.turn):
            row, col = pos
            raise BadMoveException('row: {} col: {} is a bad move'.format(row, col))
        return board.check_winner(self.turn)

    def think(self):
        pos = input("{} is your turn: ".format(self.name))
        return list(map(int, pos.split()))
        
        