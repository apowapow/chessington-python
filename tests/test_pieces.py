from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Bishop, Rook, Queen, King, Knight

class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(6, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_at_top_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(7, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_at_bottom_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(4, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(2, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_white_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(4, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(2, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves

    @staticmethod
    def test_bishop_move_unobstructed():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) in moves  # top-right
        assert Square.at(2, 5) in moves  # bottom-right
        assert Square.at(4, 3) in moves  # top-left
        assert Square.at(2, 3) in moves  # bottom-left

        assert Square.at(6, 7) in moves  # top-right
        assert Square.at(0, 7) in moves  # bottom-right
        assert Square.at(7, 0) in moves  # top-left
        assert Square.at(0, 1) in moves  # bottom-left

    @staticmethod
    def test_bishop_move_unobstructed_out_of_bounds():

        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(8, 9) not in moves  # top-right
        assert Square.at(-2, 9) not in moves  # bottom-right
        assert Square.at(9, -2) not in moves  # top-left
        assert Square.at(-2, -1) not in moves  # bottom-left

    @staticmethod
    def test_bishop_move_obstructed_same_colour_piece():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(5, 6)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) not in moves
        assert Square.at(6, 7) not in moves

    @staticmethod
    def test_bishop_move_obstructed_opposite_colour_piece():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        enemy = Pawn(Player.WHITE)
        enemy_square = Square.at(1, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(0, 1) not in moves

    @staticmethod
    def test_rook_move_unobstructed():

        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves  # up
        assert Square.at(3, 5) in moves  # right
        assert Square.at(2, 4) in moves  # down
        assert Square.at(3, 3) in moves  # left

        assert Square.at(7, 4) in moves  # up
        assert Square.at(3, 7) in moves  # right
        assert Square.at(0, 4) in moves  # down
        assert Square.at(3, 0) in moves  # left

    @staticmethod
    def test_rook_move_unobstructed_out_of_bounds():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(8, 4) not in moves  # up
        assert Square.at(3, 8) not in moves  # right
        assert Square.at(-1, 4) not in moves  # down
        assert Square.at(3, -1) not in moves  # left

    @staticmethod
    def test_rook_move_obstructed_same_colour_piece():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(6, 4)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(7, 4) not in moves

    @staticmethod
    def test_rook_move_obstructed_opposite_colour_piece():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        enemy = Pawn(Player.WHITE)
        enemy_square = Square.at(6, 4)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(7, 4) not in moves

    @staticmethod
    def test_queen_move_unobstructed():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # diagonal, immediate
        assert Square.at(4, 5) in moves  # top-right
        assert Square.at(2, 5) in moves  # bottom-right
        assert Square.at(4, 3) in moves  # top-left
        assert Square.at(2, 3) in moves  # bottom-left

        # diagonal, edge
        assert Square.at(6, 7) in moves  # top-right
        assert Square.at(0, 7) in moves  # bottom-right
        assert Square.at(7, 0) in moves  # top-left
        assert Square.at(0, 1) in moves  # bottom-left

        # lateral, immediate
        assert Square.at(4, 4) in moves  # up
        assert Square.at(3, 5) in moves  # right
        assert Square.at(2, 4) in moves  # down
        assert Square.at(3, 3) in moves  # left

        # lateral, edge
        assert Square.at(7, 4) in moves  # up
        assert Square.at(3, 7) in moves  # right
        assert Square.at(0, 4) in moves  # down
        assert Square.at(3, 0) in moves  # left


    @staticmethod
    def test_queen_move_unobstructed_out_of_bounds():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(6, 8) not in moves  # top-right
        assert Square.at(0, 8) not in moves  # bottom-right
        assert Square.at(7, -1) not in moves  # top-left
        assert Square.at(-1, 1) not in moves  # bottom-left

        assert Square.at(8, 4) not in moves  # up
        assert Square.at(3, 8) not in moves  # right
        assert Square.at(-1, 4) not in moves  # down
        assert Square.at(3, -1) not in moves  # left

    @staticmethod
    def test_queen_move_obstructed_same_colour_piece():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        friendly_diagonal = Pawn(Player.BLACK)
        friendly_diagonal_square = Square.at(5, 6)
        board.set_piece(friendly_diagonal_square, friendly_diagonal)

        friendly_lateral = Pawn(Player.BLACK)
        friendly_lateral_square = Square.at(6, 4)
        board.set_piece(friendly_lateral_square, friendly_lateral)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Diagonal
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) not in moves
        assert Square.at(6, 7) not in moves

        # Lateral
        assert Square.at(4, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(7, 4) not in moves

    @staticmethod
    def test_queen_move_obstructed_opposite_colour_piece():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        enemy_diagonal = Pawn(Player.WHITE)
        enemy_diagonal_square = Square.at(5, 6)
        board.set_piece(enemy_diagonal_square, enemy_diagonal)

        enemy_lateral = Pawn(Player.WHITE)
        enemy_lateral_square = Square.at(6, 4)
        board.set_piece(enemy_lateral_square, enemy_lateral)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Diagonal
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) not in moves

        # Lateral
        assert Square.at(4, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(7, 4) not in moves

    @staticmethod
    def test_king_move_unobstructed():
        return True  # todo

    @staticmethod
    def test_king_move_unobstructed_out_of_bounds():
        return True  # todo

    @staticmethod
    def test_king_move_obstructed_same_colour_piece():
        return True  # todo

    @staticmethod
    def test_king_move_obstructed_opposite_colour_piece():
        return True  # todo

    @staticmethod
    def test_knight_move_unobstructed():
        return True  # todo

    @staticmethod
    def test_knight_move_unobstructed_out_of_bounds():
        return True  # todo

    @staticmethod
    def test_knight_move_obstructed_same_colour_piece():
        return True  # todo

    @staticmethod
    def test_knight_move_obstructed_opposite_colour_piece():
        return True  # todo
