"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square


BOARD_MAX = 7
BOARD_MIN = 0


class Piece(ABC):

    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player
        self.moved = False

    def maybe_add_square(self, squarelist, square, board, empty, takeable):
        if BOARD_MIN <= square.row <= BOARD_MAX and BOARD_MIN <= square.col <= BOARD_MAX:
            piece = board.get_piece(square)

            if piece is None:
                if empty:
                    squarelist.append(square)
                    return False  # empty square is not obstruction

            else:
                if piece.player != self.player:
                    if takeable:
                        squarelist.append(square)
                return True  # any colour is obstruction
        else:
            return True  # walls of board are also obstructions

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self.moved = True


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        moves = []
        white = self.player == Player.WHITE
        pos = board.find_piece(self)

        # in front
        self.maybe_add_square(
            squarelist=moves,
            square=Square.at(pos.row + 1 if white else pos.row - 1, pos.col),
            board=board,
            empty=True,
            takeable=False)

        if len(moves) == 1 and (not self.moved):
            self.maybe_add_square(
                squarelist=moves,
                square=Square.at(pos.row + 2 if white else pos.row - 2, pos.col),
                board=board,
                empty=True,
                takeable=False)

        # diagonal
        self.maybe_add_square(
            squarelist=moves,
            square=Square.at(pos.row + 1 if white else pos.row - 1, pos.col - 1),
            board=board,
            empty=False,
            takeable=True)

        self.maybe_add_square(
            squarelist=moves,
            square=Square.at(pos.row + 1 if white else pos.row - 1, pos.col + 1),
            board=board,
            empty=False,
            takeable=True)

        return moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        moves = []
        direction = [(True, True), (False, True), (False, False), (True, False)]
        pos = board.find_piece(self)

        for d in direction:
            next_col = pos.col + 1 if d[1] else pos.col - 1
            next_row_init = pos.row + 1 if d[0] else pos.row - 1
            next_row_end = BOARD_MAX + 1 if d[0] else BOARD_MIN - 1
            step = 1 if d[0] else -1

            for next_row in range(next_row_init, next_row_end, step):
                obstruction = self.maybe_add_square(
                    squarelist=moves,
                    square=Square.at(next_row, next_col),
                    board=board,
                    empty=True,
                    takeable=True)

                if obstruction:
                    break

                next_col = next_col + 1 if d[1] else next_col - 1

        return moves


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []
