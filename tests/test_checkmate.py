from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Bishop, Rook, Queen, King, Knight


class TestKingIsInCheck:

    @staticmethod
    def test_white_king_not_in_check():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy_pawn = Pawn(Player.BLACK)
        enemy_pawn_square = Square.at(3, 3)
        board.set_piece(enemy_pawn_square, enemy_pawn)

        enemy_rook = Rook(Player.BLACK)
        enemy_rook_square = Square.at(3, 4)
        board.set_piece(enemy_rook_square, enemy_rook)

        enemy_bishop = Bishop(Player.BLACK)
        enemy_bishop_square = Square.at(1, 3)
        board.set_piece(enemy_bishop_square, enemy_bishop)

        enemy_knight = Knight(Player.BLACK)
        enemy_knight_square = Square.at(7, 7)
        board.set_piece(enemy_knight_square, enemy_knight)

        enemy_queen = Queen(Player.BLACK)
        enemy_queen_square = Square.at(3, 0)
        board.set_piece(enemy_queen_square, enemy_queen)

        enemy_king = King(Player.BLACK)
        enemy_king_square = Square.at(6, 6)
        board.set_piece(enemy_king_square, enemy_king)

        # Act
        check = king.is_in_check(board)

        # Assert
        assert check is False

    @staticmethod
    def test_white_king_checked_by_black_pawn():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(3, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        # check if current square is in check by a pawn
        check = king.is_in_check(board)

        # Assert
        assert check is True

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
        # check if current square is in check?
        check = king.is_in_check(board)

        # Assert
        assert check is True

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

        # check if current square is in check?
        check = king.is_in_check(board)

        # Assert
        assert check is True

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
        # check if current square is in check?
        check = king.is_in_check(board)

        # Assert
        assert check is True


    @staticmethod
    def test_white_king_checked_by_black_queen_lateral():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Queen(Player.BLACK)
        enemy_square = Square.at(2, 1)
        board.set_piece(enemy_square, enemy)

        # Act
        check = king.is_in_check(board)

        # Assert
        assert check is True

    @staticmethod
    def test_white_king_checked_by_black_queen_diagonal():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 3)
        board.set_piece(king_square, king)

        enemy = Queen(Player.BLACK)
        enemy_square = Square.at(1, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        check = king.is_in_check(board)

        # Assert
        assert check is True


class TestKingCannotMoveIntoCheck:

    @staticmethod
    def test_king_cannot_move_to_check_by_pawn():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(1, 3)
        board.set_piece(king_square, king)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(3, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(0, 2) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(0, 4) in moves
        assert Square.at(0, 3) in moves
        assert len(moves) == 7

#
#
    @staticmethod
    def test_king_cannot_move_to_check_by_rook():
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
    def test_king_cannot_move_to_check_by_bishop():
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

        # Assert
        assert len(moves) == 7
        assert Square.at(1, 2) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) not in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 3) in moves


    @staticmethod
    def test_king_cannot_move_to_check_by_knight():
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
    def test_king_cannot_move_to_check_by_queen():
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

        # Assert
        assert len(moves) == 3
        assert Square.at(1, 2) in moves
        assert Square.at(2, 2) not in moves
        assert Square.at(3, 2) not in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 4) not in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(1, 3) not in moves
 
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

class TestPieceCannotMoveAndPutOwnKingIntoCheck:
    @staticmethod
    def test_white_pawn_cannot_move_to_check_white_king():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(0, 4)
        board.set_piece(king_square, king)

        friend = Pawn(Player.WHITE)
        friend_square = Square.at(1, 4)
        board.set_piece(friend_square, friend)

        enemy_rook = Rook(Player.BLACK)
        enemy_rook_square = Square.at(4, 4)
        board.set_piece(enemy_rook_square, enemy_rook)

        enemy_pawn = Pawn(Player.BLACK)
        enemy_pawn_square = Square.at(2,5)
        board.set_piece(enemy_pawn_square, enemy_pawn)

        # Act
        moves = friend.get_available_moves(board)
            
        # Assert
        assert Square.at(2, 4) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves
        assert len(moves) == 2

    @staticmethod
    def test_white_knight_cannot_move_to_check_white_king():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(0, 4)
        board.set_piece(king_square, king)

        friend = Knight(Player.WHITE)
        friend_square = Square.at(1, 5)
        board.set_piece(friend_square, friend)

        enemy = Bishop(Player.BLACK)
        enemy_square = Square.at(3, 7)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = friend.get_available_moves(board)
            
        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_rook_cannot_move_to_check_white_king():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(0, 4)
        board.set_piece(king_square, king)

        friend = Rook(Player.WHITE)
        friend_square = Square.at(2, 4)
        board.set_piece(friend_square, friend)

        enemy = Rook(Player.BLACK)
        enemy_square = Square.at(4, 4)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = friend.get_available_moves(board)

        # Assert
        assert len(moves) == 3
        assert Square.at(3, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 5) not in moves
        assert Square.at(2, 3) not in moves
        assert Square.at(1, 4) in moves

    @staticmethod
    def test_white_bishop_cannot_move_to_check_white_king():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(0, 4)
        board.set_piece(king_square, king)

        friend = Bishop(Player.WHITE)
        friend_square = Square.at(2, 4)
        board.set_piece(friend_square, friend)

        enemy = Rook(Player.BLACK)
        enemy_square = Square.at(4, 4)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = friend.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_queen_cannot_move_to_check_white_king_1():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(0, 4)
        board.set_piece(king_square, king)

        friend = Queen(Player.WHITE)
        friend_square = Square.at(2, 4)
        board.set_piece(friend_square, friend)

        enemy = Rook(Player.BLACK)
        enemy_square = Square.at(4, 4)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = friend.get_available_moves(board)

        # Assert
        assert len(moves) == 3
        assert Square.at(3, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 5) not in moves
        assert Square.at(2, 3) not in moves
        assert Square.at(1, 4) in moves

    @staticmethod
    def test_white_queen_cannot_move_to_check_white_king_2():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(0, 4)
        board.set_piece(king_square, king)

        friend = Queen(Player.WHITE)
        friend_square = Square.at(1, 5)
        board.set_piece(friend_square, friend)

        enemy = Bishop(Player.BLACK)
        enemy_square = Square.at(3, 7)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = friend.get_available_moves(board)

        # Assert
        assert len(moves) == 2
        assert Square.at(2, 5) not in moves
        assert Square.at(2, 6) in moves
        assert Square.at(3, 7) in moves
        assert Square.at(1, 6) not in moves
        assert Square.at(0, 6) not in moves
        assert Square.at(0, 5) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(2, 4) not in moves


class TestCheckMate:
    @staticmethod
    def test_black_king_in_checkmate_1():
        # Arrange
        board = Board.empty()
        black_king = King(Player.BLACK)
        black_king_square = Square.at(7, 6)
        board.set_piece(black_king_square, black_king)

        black_rook = Rook(Player.BLACK)
        black_rook_square = Square.at(7, 7)
        board.set_piece(black_rook_square, black_rook)

        black_knight = Knight(Player.BLACK)
        black_knight_square = Square.at(7, 5)
        board.set_piece(black_knight_square, black_knight)

        black_pawn_1 = Pawn(Player.BLACK)
        black_pawn_1_square = Square.at(6, 5)
        board.set_piece(black_pawn_1_square, black_pawn_1)

        black_pawn_2 = Pawn(Player.BLACK)
        black_pawn_2_square = Square.at(6, 6)
        board.set_piece(black_pawn_2_square, black_pawn_2)

        black_pawn_3 = Pawn(Player.BLACK)
        black_pawn_3_square = Square.at(6, 7)
        board.set_piece(black_pawn_3_square, black_pawn_3)

        white_knight = Knight(Player.WHITE)
        white_knight_square = Square.at(6, 4)
        board.set_piece(white_knight_square, white_knight)

        white_king = King(Player.WHITE)
        white_king_square = Square.at(1, 4)
        board.set_piece(white_king_square, white_king)

        # Act
        check = black_king.is_in_check(board)
        moves_black_king = black_king.get_available_moves(board)
        moves_black_knight = black_king.get_available_moves(board)
        moves_black_rook = black_rook.get_available_moves(board)
        moves_black_pawn_1 = black_pawn_1.get_available_moves(board)
        moves_black_pawn_2 = black_pawn_2.get_available_moves(board)
        moves_black_pawn_3 = black_pawn_3.get_available_moves(board)

        # Assert
        assert check == True
        assert len(moves_black_king) == 0
        assert len(moves_black_knight) == 0
        assert len(moves_black_rook) == 0
        assert len(moves_black_pawn_1) == 0
        assert len(moves_black_pawn_2) == 0
        assert len(moves_black_pawn_3) == 0

    @staticmethod
    def test_black_king_in_checkmate_2():
        # Arrange
        board = Board.empty()
        black_king = King(Player.BLACK)
        black_king_square = Square.at(7, 6)
        board.set_piece(black_king_square, black_king)

        black_rook = Rook(Player.BLACK)
        black_rook_square = Square.at(7, 7)
        board.set_piece(black_rook_square, black_rook)

        black_bishop = Bishop(Player.BLACK)
        black_bishop_square = Square.at(7, 5)
        board.set_piece(black_bishop_square, black_bishop)

        black_pawn_1 = Pawn(Player.BLACK)
        black_pawn_1_square = Square.at(5, 5)
        board.set_piece(black_pawn_1_square, black_pawn_1)

        black_pawn_2 = Pawn(Player.BLACK)
        black_pawn_2_square = Square.at(6, 6)
        board.set_piece(black_pawn_2_square, black_pawn_2)

        black_pawn_3 = Pawn(Player.BLACK)
        black_pawn_3_square = Square.at(6, 7)
        board.set_piece(black_pawn_3_square, black_pawn_3)

        white_bishop = Bishop(Player.WHITE)
        white_bishop_square = Square.at(1, 0)
        board.set_piece(white_bishop_square, white_bishop)

        white_king = King(Player.WHITE)
        white_king_square = Square.at(1, 4)
        board.set_piece(white_king_square, white_king)

        # Act
        check = black_king.is_in_check(board)
        moves_black_king = black_king.get_available_moves(board)
        moves_black_bishop = black_bishop.get_available_moves(board)
        moves_black_rook = black_rook.get_available_moves(board)
        moves_black_pawn_1 = black_pawn_1.get_available_moves(board)
        moves_black_pawn_2 = black_pawn_2.get_available_moves(board)
        moves_black_pawn_3 = black_pawn_3.get_available_moves(board)

        # Assert
        assert check
        assert len(moves_black_king) == 0
        assert len(moves_black_bishop) == 0
        assert len(moves_black_rook) == 0
        assert len(moves_black_pawn_1) == 0
        assert len(moves_black_pawn_2) == 0
        assert len(moves_black_pawn_3) == 0

    @staticmethod
    def test_black_king_in_checkmate_3():
        # Arrange
        board = Board.empty()
        black_king = King(Player.BLACK)
        black_king_square = Square.at(7, 6)
        board.set_piece(black_king_square, black_king)

        black_knight = Knight(Player.BLACK)
        black_knight_square = Square.at(4, 2)
        board.set_piece(black_knight_square, black_knight)

        black_bishop = Bishop(Player.BLACK)
        black_bishop_square = Square.at(2, 0)
        board.set_piece(black_bishop_square, black_bishop)

        black_pawn_1 = Pawn(Player.BLACK)
        black_pawn_1_square = Square.at(6, 5)
        board.set_piece(black_pawn_1_square, black_pawn_1)

        black_pawn_2 = Pawn(Player.BLACK)
        black_pawn_2_square = Square.at(6, 6)
        board.set_piece(black_pawn_2_square, black_pawn_2)

        black_pawn_3 = Pawn(Player.BLACK)
        black_pawn_3_square = Square.at(6, 7)
        board.set_piece(black_pawn_3_square, black_pawn_3)

        white_rook = Rook(Player.WHITE)
        white_rook_square = Square.at(7, 3)
        board.set_piece(white_rook_square, white_rook)

        white_king = King(Player.WHITE)
        white_king_square = Square.at(1, 4)
        board.set_piece(white_king_square, white_king)

        # Act
        check = black_king.is_in_check(board)
        moves_black_king = black_king.get_available_moves(board)
        moves_black_bishop = black_bishop.get_available_moves(board)
        moves_black_knight = black_knight.get_available_moves(board)
        moves_black_pawn_1 = black_pawn_1.get_available_moves(board)
        moves_black_pawn_2 = black_pawn_2.get_available_moves(board)
        moves_black_pawn_3 = black_pawn_3.get_available_moves(board)

        # Assert
        assert check
        assert len(moves_black_king) == 0
        assert len(moves_black_bishop) == 0
        assert len(moves_black_knight) == 0
        assert len(moves_black_pawn_1) == 0
        assert len(moves_black_pawn_2) == 0
        assert len(moves_black_pawn_3) == 0
