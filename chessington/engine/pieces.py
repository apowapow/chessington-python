"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square


BOARD_SIZE = 8


class Piece(ABC):

    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player
        self.moved = False

    def maybe_add_square(self, squarelist, square, board, takeable):
        if 0 <= square.row < BOARD_SIZE and 0 <= square.col < BOARD_SIZE:
            piece = board.get_piece(square)

            if piece is None:
                if not takeable:
                    squarelist.append(square)

            elif piece.player != self.player:
                if takeable:
                    squarelist.append(square)

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
            takeable=False)

        if len(moves) == 1 and (not self.moved):
            self.maybe_add_square(
                squarelist=moves,
                square=Square.at(pos.row + 2 if white else pos.row - 2, pos.col),
                board=board,
                takeable=False)

        # diagonal
        self.maybe_add_square(
            squarelist=moves,
            square=Square.at(pos.row + 1 if white else pos.row - 1, pos.col - 1),
            board=board,
            takeable=True)

        self.maybe_add_square(
            squarelist=moves,
            square=Square.at(pos.row + 1 if white else pos.row - 1, pos.col + 1),
            board=board,
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
        return []


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
