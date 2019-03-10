import os
from Exceptions import BadMoveException

class Board:

    def __init__(self, matrix=None):
        if matrix is None:
            self.board = [['_','_','_'] for i in range(3)]
            self.transposed_board = [['_','_','_'] for i in range(3)]
        else:
            self.board = board
            self.transposed_board = self.transpose(self.board)

    def transpose(self, matrix):
        return [[matrix[j][i] for j in range(3)] for i in range(3)]

    def set_token(self, pos, turn):
        row, col = pos
        check_range = row >= 0 and row < 3 and col >=0 and col < 3
        if  not check_range or self.board[row][col] != '_':
            return False

        if turn == 0:
            self.board[row][col] = 'x'
            self.transposed_board[col][row] = 'x'
        else:
            self.board[row][col] = 'o'
            self.transposed_board[col][row] = 'o'

        return True

    def check_winner(self, turn):
        state = []
        state.append(self.check_row(turn))
        state.append(self.check_col(turn))
        state.append(self.check_diagonals(turn))
        return any(state)

    def check_row(self, turn, board=None):
        searched_token = 'x' if turn == 0 else 'o'

        if board is None:
            board = self.board

        for row in board:
            if all(map(lambda x: x==searched_token, row)):
                return True
                
        return False

    def check_col(self, turn):
        return self.check_row(turn, self.transposed_board)

    def check_diagonals(self, turn):
        searched_token = 'x' if turn == 0 else 'o'
        d1 = [searched_token == self.board[i][i] for i in range(3)]
        d2 = [searched_token == self.board[i][j] for i in range(2, -1, -1) for j in range(3)]

        return all(d1) or all(d2)

    def print_board(self, error):
        os.system('clear')
        print("    0   1   2")
        for i in range(3):
            row = self.board[i]
            print("{} |_{}_|_{}_|_{}_|".format(i, row[0], row[1], row[2]))
        print(error)