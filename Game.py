from Board import Board
from Exceptions import BadMoveException
from Players import Player, HumanPlayer, MachinePlayer

class Game:
    def __init__(self):

        self.board = Board()
        self.players = [HumanPlayer("Player 1", 0), MachinePlayer("Player 2", 1)]
        self.turn = 0

    def start(self):
        winner = False
        error_message = ""
        while not winner:
            self.board.print_board(error_message)
            try:
                winner = self.players[self.turn].move(self.board)
                error_message = ""
            except BadMoveException as bme:
                error_message = str(bme)
                continue

            self.turn = (self.turn+1)%2

        if winner:
            self.board.print_board(error_message)
            winner_turn = (self.turn+1)%2 + 1
            print("{} wins".format(self.players[winner_turn]))

if __name__=="__main__":
    g = Game()
    g.start()


        

