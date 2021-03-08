"""
Board File
Includes Class for a chess board
Includes Class for a chess board square
"""
from typing import List, Dict
import settings as sett


class Board:
    """
    Board Class
    Holds all the squares and formats them

    squares = {row: sq_obj sorted in files}
    squares = {1: a1, b1, c1.... 2: a2, b2, c3...}
    """

    def __init__(self):
        self.squares = self.init_square_dic()

    def add_square(self, sq_obj: 'Square' ) -> None:

        self.squares[sq_obj.row].append(sq_obj)
        self.squares[sq_obj.row] = sorted(self.squares[sq_obj.row],
                                          key=lambda f: f.file)

    def init_square_dic(self):
        """
        To create the empty squares dictionary to organize
        all the square of the board
        """
        squares = {}
        for row in sett.rows:
            squares[row] = []
        return squares

    def place_piece(self, piece: 'Piece object') -> None:
        piece_row = piece.row
        piece_file = piece.file
        # Square of interest
        soi = self.squares[piece_row][sett.files.index(piece_file)]

        if soi.holding is not None:
            print("Piece: {} is trying to move onto square: {} but piece: {}" +
                  "is already on it".format(piece.type_, soi.code,
                                            soi.holding.type_))
            raise Exception
        soi.holding = piece

    def remove_piece(self, piece: 'Piece object') -> bool:
        """
        Remove piece from wherever it is on the board, make the square
        it is non holding = None

        Return True if piece is removed, False if something went wrong
        """
        for row in self.squares.values():
            for sq in row:
                if sq.holding is piece:
                    sq.holding = None
                    return True
        return False

    def __str__(self):
        board_str = ''
        line_str = ''
        for file in self.squares.values():
            for sq in file:
                if sq.holding:
                    line_str += sq.holding.type_[0] + '   '
                else:
                    line_str += str(sq)
            board_str = line_str + '\n' + board_str
            line_str = ''
        return board_str


class Square:
    """
    Class representing a single square


    Representation invariants:
    ==========================
    colour == 0 or colour == 1
    0 is black
    1 is white
    ==========================
    file in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row in ['1', '2', '3', '4', '5', '6', '7', '8']
    ==========================
    a
    """
    file: str
    row: str
    attacked: [bool, bool]  # white, black
    colour: int
    code: str
    holding: 'Piece object'

    def __init__(self, colour: int, file: str, row: str):
        self.file = file
        self.colour = colour
        self.row = row
        self.attacked = [False, False]
        self.code = file + row
        self.holding = None

    def __str__(self):
        formatting = '{}{}, '.format(self.file, self.row)
        return formatting


def create_board() -> 'Board':
    board = Board()
    colour_flag = 0
    for Row in range(8):
        for File in range(8):
            colour_flag += 1
            square = Square(sett.sq_colours[colour_flag % 2], sett.files[File],
                            sett.rows[Row])
            board.add_square(square)
        colour_flag += 1
    return board


if __name__ == '__main__':
    b = create_board()
    print(b)

