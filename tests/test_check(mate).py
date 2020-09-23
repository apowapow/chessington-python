from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Bishop, Rook, Queen, King, Knight


class TestKingIsChecked:

    @staticmethod
    def test_white_king_checked_by_black_pawn():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(1, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = king.get_available_moves(board)
        # check if current square is in check?
        # checked_by = king.get_checked_by(board)

        # Assert
        assert Square.at(1, 2) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 3) in moves
        assert len(moves) == 8

    @staticmethod
    def test_white_king_checked_by_black_rook():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Rook(Player.BLACK)
        enemy_square = Square.at(2, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = king.get_available_moves(board)
        # check if current square is in check?
        # checked_by = king.get_checked_by(board)

        # Assert
        assert Square.at(1, 2) not in moves
        assert Square.at(2, 2) in moves
        assert Square.at(3, 2) not in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 3) in moves
        assert len(moves) == 5

    @staticmethod
    def test_white_king_checked_by_black_bishop():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Bishop(Player.BLACK)
        enemy_square = Square.at(1, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = king.get_available_moves(board)
        # check if current square is in check?
        # checked_by = king.get_checked_by(board)

        # Assert
        assert Square.at(1, 2) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) not in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 3) in moves
        assert len(moves) == 7

    @staticmethod
    def test_white_king_checked_by_black_knight():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Knight(Player.BLACK)
        enemy_square = Square.at(1, 1)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = king.get_available_moves(board)
        # check if current square is in check?
        # checked_by = king.get_checked_by(board)

        # Assert
        assert Square.at(1, 2) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(3, 2) not in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 3) in moves
        assert len(moves) == 7

    @staticmethod
    def test_white_king_checked_by_black_queen():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Queen(Player.BLACK)
        enemy_square = Square.at(1, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = king.get_available_moves(board)
        # check if current square is in check?
        # checked_by = king.get_checked_by(board)

        # Assert
        assert Square.at(1, 2) in moves
        assert Square.at(2, 2) not in moves
        assert Square.at(3, 2) not in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) not in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(1, 3) not in moves
        assert len(moves) == 3


class TestKingCannotMoveIntoCheck:
#
#     @staticmethod
#     def test_king_cannot_move_to_check_by_pawn():
#
#
#     @staticmethod
#     def test_king_cannot_move_to_check_by_rook():
#         pass
#
#     @staticmethod
#     def test_king_cannot_move_to_check_by_bishop():
#         pass
#
#     @staticmethod
#     def test_king_cannot_move_to_check_by_knight():
#         pass
#
#     @staticmethod
#     def test_king_cannot_move_to_check_by_queen():
#         pass
#
    @staticmethod
    def test_king_cannot_move_to_check_by_king():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = King(Player.BLACK)
        enemy_square = Square.at(2, 5)
        board.set_piece(enemy_square, enemy)

        # Act
        moves_white = king.get_available_moves(board)
        moves_black = enemy.get_available_moves(board)
        # check if current square is in check?
        # checked_by = king.get_checked_by(board)

        # Assert
        assert Square.at(1, 2) in moves_white
        assert Square.at(2, 2) in moves_white
        assert Square.at(3, 2) in moves_white
        assert Square.at(3, 3) in moves_white
        assert Square.at(3, 4) not in moves_white
        assert Square.at(2, 4) not in moves_white
        assert Square.at(1, 4) not in moves_white
        assert Square.at(1, 3) in moves_white
        assert len(moves_white) == 5

        assert Square.at(3, 5) in moves_black
        assert Square.at(3, 6) in moves_black
        assert Square.at(2, 6) in moves_black
        assert Square.at(1, 6) in moves_black
        assert Square.at(3, 4) not in moves_black
        assert Square.at(2, 4) not in moves_black
        assert Square.at(1, 4) not in moves_black
        assert Square.at(1, 5) in moves_black
        assert len(moves_black) == 5
# class TestPieceCannotMoveIfCreateCheck:
#
#     # @staticmethod
#     #
#
# class TestCheckMate: