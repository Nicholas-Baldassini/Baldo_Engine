"""
Board File
Includes Class for a chess board
Includes Class for a chess board square
"""
from typing import List, Dict
import settings as sett
import pieces


class Board:
    """
    Board Class
    Holds all the squares and formats them

    squares = [[8], [7], [6]...]
    squares = [[a8, b8, c8...], [a7, b7, c7...]...]

    Representation Invariants
    ========================
    len(squares) == 8
    len(squares[i]) == 8
    """
    squares: [['Square']]  # Private
    flipped: bool

    def __init__(self):
        self.squares = self.init_square_list()
        self.flipped = False  # False is white on bottom

    def add_square(self, sq_obj: 'Square') -> None:
        rr = sett.rows[::-1]  # Reversed rows, used for indexing

        self.squares[rr.index(sq_obj.row)].append(sq_obj)
        self.squares[rr.index(sq_obj.row)] = sorted(
            self.squares[rr.index(sq_obj.row)],
            key=lambda f: f.file)

    def init_square_list(self) -> List[List]:
        """
        To create the empty squares dictionary to organize
        all the square of the board
        >>> b = Board()
        >>> b.init_square_list()
        [[], [], [], [], [], [], [], []]
        """
        squares = []
        for i in range(8):
            squares.append([])
        return squares

    def get_board(self) -> List[List['Square']]:
        """
        Returns a copy of the virtual board, the list of lists
        """
        return self.squares

    # Todo Set this one time to save time, set as attribute
    def get_colour_pieces_on_board(self, colour: str):
        """
        Returns a list of all the pieces on the board of colour
        """
        the_alive_ones = []
        for row in self.squares:
            for square in row:
                if isinstance(square.holding, pieces.Piece):
                    if square.holding.team == colour:
                        the_alive_ones.append(square.holding)
        return the_alive_ones

    # Todo Set this one time to save time, set as attribute
    def get_type_of_pieces(self, piece_type: str, colour: str):
        """
        Return a list of all the pieces of piece_type of colour
        """
        the_chosen_ones = []
        coloured = self.get_colour_pieces_on_board(colour)
        for peece in coloured:
            if peece.type_ == piece_type:
                the_chosen_ones.append(peece)
        return the_chosen_ones

    def flip_board(self) -> None:
        """
        Internally flip the board, white is on top, black on bottom
        """
        for row in range(len(self.squares)):
            self.squares[row] = self.squares[row][::-1]
        self.squares = self.squares[::-1]
        self.flipped = not self.flipped  # Toggle flipped status

    def get_square(self, file: str, row: str) -> 'Square':
        """
        Retrieve a specific square given code
        Return square object
        """
        if not isinstance(file, str) or not isinstance(row, str):
            print("File or Row is not a str")
            raise Exception
        if self.flipped:
            rr = sett.rows
            rf = sett.files[::-1]
        else:
            rr = sett.rows[::-1]  # Must reverse list because square list is
                                  # read top, row 8 to bottom, ro 1
            rf = sett.files
        row = rr.index(row)
        sq = self.squares[row][rf.index(file)]
        return sq

    def get_piece(self, file, row):
        """
        Returns piece object if piece object exists in the code
        """
        sq = self.get_square(file, row)
        if sq.holding:
            return sq.holding


    def place_piece(self, piece: 'Piece object') -> None:
        piece_row = piece.row
        piece_file = piece.file
        rr = sett.rows[::-1]
        # Square of interest
        soi = self.squares[rr.index(piece_row)][sett.files.index(piece_file)]

        if soi.holding is not None or isinstance(soi.holding, pieces.Piece):
            if soi.holding is not piece:
                print(soi.holding.code + 'is already on this square')
                raise Exception
        soi.holding = piece

    def remove_piece(self, piece: 'Piece object') -> bool:
        """
        Remove piece from wherever it is on the board, make the square
        it is non holding = None

        Return True if piece is removed, False if something went wrong
        """

        for row in self.squares:
            for sq in row:
                if sq.holding and sq.holding is piece:
                    sq.holding = None
                    return True
        return False

    def __str__(self):
        board_str = '['

        for row in self.squares:
            board_str += '['
            for sq in row:
                if isinstance(sq.holding, pieces.Piece):
                    board_str += sq.holding.code + ', '
                else:
                    board_str += sq.code + ',   '
            board_str += '], \n'
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
    cur_colour: str
    code: str
    holding: 'pieces.Piece'
    default_colour: str # black or white by default

    def __init__(self, colour: str, file: str, row: str):
        self.file = file
        self.cur_colour = colour
        self.row = row
        self.attacked = [False, False]
        self.code = file + row
        self.holding = None
        self.default_colour = colour

    def change_colour(self, colour):
        """
        Change colour of square
        Used to highlight a square
        """
        self.cur_colour = colour

    def get_default_colour(self):
        """
        Return Default colour of the square
        """
        return self.default_colour

    def __str__(self):
        formatting = '{}{}, '.format(self.file, self.row)
        return formatting


def create_board() -> 'Board':
    board = Board()
    colour_flag = 0
    for Row in range(8):
        for File in range(8):
            colour_flag += 1
            square = Square(sett.teams[colour_flag % 2], sett.files[File],
                            sett.rows[Row])
            board.add_square(square)
        colour_flag += 1
    return board


if __name__ == '__main__':
    b = create_board()
    print(b)

