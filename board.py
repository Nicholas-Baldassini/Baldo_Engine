"""
Board File
Includes Class for a chess board
Includes Class for a chess board square

The board class is the backbone of the whole program, the board object holds all
64 squares of the chess board and performs operations and data retrieval on the
board

The square class holds data about a specific square, data being colour,
occupying piece, code and more

The board and square class are meant to be public interfaces
"""
from typing import List, Dict, Optional
import settings as sett
import pieces # Only used for type annotations


class Board:
    """
    Board public Class
    Holds all the square objects and formats them, performs various operations

    squares = [[8], [7], [6]...]
    squares = [[a8, b8, c8...], [a7, b7, c7...]...]

    Representation Invariants
    ========================
    len(squares) == 8
    len(squares[i]) == 8
    """
    squares: List[List['Square']]  # Private
    flipped: bool
    # Pieces are already stored in squares but coloured_pieces is used to not
    # have to loop through the list every time coloured_pieces is needed
    coloured_pieces: Dict[str, List['pieces.Piece']]

    def __init__(self):
        self.squares = self.init_square_list() # Create empty board
        self.flipped = False  # False is white on bottom, default layout
        self.coloured_pieces = {'white': [], 'black': []}

    def add_square(self, sq_obj: 'Square') -> None:
        """
        Called during creation of a board object, adds a square into its
        designated position in the squares list based on its code
        """
        rr = sett.rows[::-1]  # Reversed rows, used for indexing

        self.squares[rr.index(sq_obj.row)].append(sq_obj)
        self.squares[rr.index(sq_obj.row)] = sorted(
            self.squares[rr.index(sq_obj.row)], key=lambda f: f.file)

    @staticmethod
    def init_square_list() -> List[List['Square']]:
        """
        Used to create the empty squares list to organize all the squares
        of the board
        >>> b_ = Board()
        >>> b_.init_square_list()
        [[], [], [], [], [], [], [], []]
        """
        squares = []
        for i in range(8):
            squares.append([])
        return squares

    def get_board(self) -> List[List['Square']]:
        """
        Returns a copy of the virtual board, the list of lists holding all the
        squares
        """
        return self.squares

    def init_coloured_pieces(self) -> None:
        """
        Create the initial colour pieces dictionary holding all pieces currently
        on board, called only when all the pieces are placed at start of game
        """
        for row in self.squares:
            for square in row:
                if square.holding and isinstance(square.holding, pieces.Piece):
                    if square.holding.team == sett.teams[0]: # 'white'
                        self.coloured_pieces['white'].append(square.holding)
                    elif square.holding.team == sett.teams[1]:
                        self.coloured_pieces['black'].append(square.holding)
                    else:
                        print("The team of a piece is not 'white or black")
                        raise Exception

    def update_colour_pieces_on_board(self, colour: str) -> None:
        """
        Update list containing all pieces of a certain colour
        Only called when a piece is captured
        """
        for row in self.squares:
            for square in row:
                if square.holding and isinstance(square.holding, pieces.Piece):
                    if square.holding.team == colour:
                        # Only remove pieces that was on board previously
                        if square.holding not in self.coloured_pieces.get(colour):
                            self.coloured_pieces[colour].remove(square.holding)
                            # break

    # # Todo Set this one time to save time, set as attribute
    # def get_type_of_pieces(self, piece_type: str, colour: str):
    #     """
    #     Return a list of all the pieces of piece_type of colour
    #     """
    #     the_chosen_ones = []
    #     coloured = self.get_colour_pieces_on_board(colour)
    #     for peece in coloured:
    #         if peece.type_ == piece_type:
    #             the_chosen_ones.append(peece)
    #     return the_chosen_ones

    def flip_board(self) -> None:
        """
        Internally flip the board, white is on top, black on bottom

        Initially the board is read from top to bottom starting with black on
        top, refer to class docstring
        """
        for row in range(len(self.squares)):
            self.squares[row] = self.squares[row][::-1]
        self.squares = self.squares[::-1]
        self.flipped = not self.flipped  # Toggle flipped status

    def get_square(self, file: str, row: str) -> 'Square':
        """
        Retrieve a specific square given file and row of the square
        Return square object

        # Note: Handles flipped board
        """
        if not isinstance(file, str) or not isinstance(row, str):
            print("File or Row is not str")
            raise Exception

        if self.flipped:
            rr = sett.rows
            rf = sett.files[::-1]
        else:
            rr = sett.rows[::-1]  # Must reverse list because square list is
            rf = sett.files
        row = rr.index(row)
        sq = self.squares[row][rf.index(file)]
        return sq

    # def get_piece(self, file, row) -> Optional['pieces.Piece']:
    #     """
    #     Returns piece object existing on a square, if no piece is on square
    #     return None
    #     """
    #     sq = self.get_square(file, row)
    #     if sq.holding:
    #         return sq.holding
    #     else:
    #         return None

    def place_piece(self, piece: 'pieces.Piece') -> None:
        """
        Given a piece, place it on the square that the piece's code it
        Every piece has its given code and is placed onto a square given its
        code

        Set the piece on its appropriate location

        # Note: Handles flipped board
        """

        if self.flipped:
            rr = sett.rows
            rf = sett.files[::-1]
        else:
            rr = sett.rows[::-1]
            rf = sett.files
        piece_row = piece.row
        piece_file = piece.file
        # rr = sett.rows[::-1]
        # rf = sett.files

        # Square of interest
        soi = self.squares[rr.index(piece_row)][rf.index(piece_file)]

        if soi.holding and isinstance(soi.holding, pieces.Piece):
            if soi.holding is not piece:
                print(soi.holding.code + 'is already on this square')
                raise Exception
        soi.holding = piece

    def remove_piece(self, piece: 'Piece object') -> bool:
        """
        Wherever a piece is, remove it from that square in the virtual board
        Called before moving a piece, the piece must be removed from its square,
        its code is updated then the piece is placed on a new square

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
    Class representing a single square, all square objects are stored in board
    object

    The square class is meant to hold data specific per square like what piece
    is on it, the colour, code and more also to perform operations and
    manipulation of data on the square

    Representation invariants:
    ==========================
    ==========================
    file in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row in ['1', '2', '3', '4', '5', '6', '7', '8']
    ==========================
    a
    """
    file: str
    row: str
    attacked: List[bool]  # white, black
    cur_colour: str
    code: str
    holding: Optional['pieces.Piece']
    default_colour: str  # black or white by default

    def __init__(self, colour: str, file: str, row: str):
        self.file = file
        self.cur_colour = colour
        self.row = row

        # ToDo update attribute to include how many attackers and which
        self.attacked = [False, False] # Not implemented yet
        self.code = file + row
        self.holding = None
        self.default_colour = colour

    def change_colour(self, colour):
        """
        Change colour of square
        Used to convey a status of the square i.e mouse is on it
        Mostly used for graphics
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
    """
    Create a board with all the squares added into it, all squares are empty
    of course
    """
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

