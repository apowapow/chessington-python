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

    def check_empty_square(self, square, board):
        return board.get_piece(square) is None

    def within_boundaries(self, square):
        return 0 <= square.row < BOARD_SIZE and 0 <= square.col < BOARD_SIZE

    def has_opposite_colour(self, square, board):
        piece = board.get_piece(square)
        return piece is not None and piece.player != self.player

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
        sq_one = Square.at(pos.row + 1 if white else pos.row - 1, pos.col)

        if self.within_boundaries(sq_one) and self.check_empty_square(sq_one, board):
            moves.append(sq_one)

            if not self.moved:
                sq_two = Square.at(pos.row + 2 if white else pos.row - 2, pos.col)

                if self.within_boundaries(sq_one) and self.check_empty_square(sq_two, board):
                    moves.append(sq_two)

        # diagonal
        sq_left = Square.at(pos.row + 1 if white else pos.row - 1, pos.col - 1)
        sq_right = Square.at(pos.row + 1 if white else pos.row - 1, pos.col + 1)

        if self.within_boundaries(sq_left) and self.has_opposite_colour(sq_left, board):
            moves.append(sq_left)

        if self.within_boundaries(sq_right) and self.has_opposite_colour(sq_right, board):
            moves.append(sq_right)

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
