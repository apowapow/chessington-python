"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player
<<<<<<< Updated upstream
=======
        self.moved = False

    def maybe_add_square(self, squarelist, square, board, empty, takeable) -> bool:
        if BOARD_MIN <= square.row <= BOARD_MAX and BOARD_MIN <= square.col <= BOARD_MAX:
            if not self._is_illegal_move(board, square):
                piece = board.get_piece(square)
                if piece is None:
                    if empty:
                        squarelist.append(square)
                    return False  # empty square is not obstruction

                else:
                    if piece.player != self.player:
                        if takeable:
                            if not isinstance(piece, King):
                                squarelist.append(square)
                    return True  # any colour is obstruction
            else:
                return False  # an illegal move should not stop get lat or dia from looking in that direction
        else:
            return True  # walls of board are also obstructions

    def _is_illegal_move(self, board, square) -> bool:
        # check if self moves to square will the king be in check
        # current_piece = board.get_piece(self)
        original_pos = board.find_piece(self)
        piece_at_square = board.get_piece(square)

        #board_temp = copy.deepcopy(board)
        king_piece = board.get_king(self.player)
        #self.move_to(board, square)
        board.set_piece(original_pos, square)
        board.set_piece(original_pos, None)
        if king_piece is None:
            return False
        is_check = king_piece.is_in_check(board)
        # self.move_to(board, original_pos)
        board.set_piece(square, original_pos)
        board.set_piece(square, piece_at_square)
        try:
            board.find_piece(self)
        except:
            pass
        board.set_piece(square, piece_at_square)
        try:
            board.find_piece(self)
        except:
            pass
        return is_check

    def is_in_check(self, board, square=None) -> bool:
        pos = board.find_piece(self) if square is None else square

        if not self._checked_by_pawn(board, pos):
            if not self._checked_by_knight(board, pos):
                if not self._checked_by_lateral(board, pos):
                    if not self._checked_by_diagonal(board, pos):
                        return False
        return True

    def get_diagonal(self, squarelist, square, board, is_king=False):
        direction = [(True, True), (False, True), (False, False), (True, False)]

        for d in direction:
            next_col = square.col + 1 if d[1] else square.col - 1
            next_row_init = square.row + 1 if d[0] else square.row - 1
            next_row_end = BOARD_MAX + 1 if d[0] else BOARD_MIN - 1
            step = 1 if d[0] else -1

            for next_row in range(next_row_init, next_row_end, step):
                obstruction = self.maybe_add_square(
                    squarelist=squarelist,
                    square=Square.at(next_row, next_col),
                    board=board,
                    empty=True,
                    takeable=True)

                if obstruction or is_king:
                    break

                next_col = next_col + 1 if d[1] else next_col - 1

    def get_lateral(self, squarelist, square, board, is_king=False):
        config = [
            (square.row + 1, BOARD_MAX + 1, 1, True),
            (square.row - 1, BOARD_MIN - 1, -1, True),
            (square.col + 1, BOARD_MAX + 1, 1, False),
            (square.col - 1, BOARD_MIN - 1, -1, False)
        ]

        for c in config:
            for n in range(c[0], c[1], c[2]):
                obstruction = self.maybe_add_square(
                    squarelist=squarelist,
                    square=Square.at(n, square.col) if c[3] else Square.at(square.row, n),
                    board=board,
                    empty=True,
                    takeable=True)

                if obstruction or is_king:
                    break

    def _checked_by_pawn(self, board, pos) -> bool:
        white = self.player == Player.WHITE
        pawn_left = board.get_piece(Square.at(pos.row + 1 if white else pos.row - 1, pos.col - 1))
        pawn_right = board.get_piece(Square.at(pos.row + 1 if white else pos.row - 1, pos.col + 1))

        return (isinstance(pawn_left, Pawn) and pawn_left.player is not self.player) or \
               (isinstance(pawn_right, Pawn) and pawn_right.player is not self.player)

    def _checked_by_knight(self, board, pos) -> bool:
        config = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ]

        for row_offset, col_offset in config:
            curr_knight = board.get_piece(Square.at(pos.row + row_offset, pos.col + col_offset))

            if isinstance(curr_knight, Knight) and curr_knight.player is not self.player:
                return True

        return False

    def _checked_by_lateral(self, board, pos) -> bool:
        config = [
            (pos.row + 1, BOARD_MAX + 1, 1, True),
            (pos.row - 1, BOARD_MIN - 1, -1, True),
            (pos.col + 1, BOARD_MAX + 1, 1, False),
            (pos.col - 1, BOARD_MIN - 1, -1, False)
        ]

        for c in config:
            for n in range(c[0], c[1], c[2]):
                curr_piece = board.get_piece(Square.at(n, pos.col) if c[3] else Square.at(pos.row, n))

                if curr_piece is not None:
                    if (isinstance(curr_piece, Rook) or isinstance(curr_piece, Queen)) and \
                            curr_piece.player is not self.player:
                        return True
                    break
        return False

    def _checked_by_diagonal(self, board, pos) -> bool:
        direction = [(True, True), (False, True), (False, False), (True, False)]

        for d in direction:
            next_col = pos.col + 1 if d[1] else pos.col - 1
            next_row_init = pos.row + 1 if d[0] else pos.row - 1
            next_row_end = BOARD_MAX + 1 if d[0] else BOARD_MIN - 1
            step = 1 if d[0] else -1

            for next_row in range(next_row_init, next_row_end, step):
                if next_col < 0 or next_col > 7:
                    break
                curr_piece = board.get_piece(Square.at(next_row, next_col))

                if curr_piece is not None:
                    if (isinstance(curr_piece, Bishop) or isinstance(curr_piece, Queen)) and \
                            curr_piece.player is not self.player:
                        return True
                    break

                next_col = next_col + 1 if d[1] else next_col - 1
        return False
>>>>>>> Stashed changes

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


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        return []


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