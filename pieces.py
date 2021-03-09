import board


class Piece:
    """
    Public Interface Class representing a single piece object
    """
    file: str
    row: str
    type_: str
    code: str
    captured: bool
    team: str
    vision: [board.Square]

    def __init__(self, file: str, row: str, type_: str, team: str):
        self.file = file
        self.row = row
        self.type_ = type_
        self.code = team[0] + type_[0] + file + row
        self.captured = False
        self.team = team
        self.vision = []

    def legal_moves(self):
        raise NotImplementedError

    def move_rules(self):
        raise NotImplementedError

    def create_vision(self):
        """
        Create list of squares that this piece could move too, no obstructions
        """
        raise NotImplementedError

    def get_vision(self):
        """
        Return vision of piece
        """
        return self.vision

    def move_piece(self, to_row: str, to_file: str):
        """
        Changes file and row position in object
        DOES NOT MOVE PIECE IN BOARD OBJECT JUST OBJECT VARIABLES
        """
        self.row = to_row
        self.file = to_file

    def capture(self):
        """
        Flag captured, once captured piece is out of game
        """
        self.captured = True


class Pawn(Piece):

    def legal_moves(self):
        pass

    def move_rules(self):
        pass
    pass


class Rook(Piece):
    def legal_moves(self):
        pass

    def move_rules(self):

        pass


class Knight(Piece):
    def legal_moves(self):
        pass

    def move_rules(self):
        pass
    pass


class Bishop(Piece):
    def legal_moves(self):
        pass

    def move_rules(self):
        pass
    pass


class King(Piece):
    def legal_moves(self):
        pass

    def move_rules(self):
        pass
    pass


class Queen(Piece):
    def legal_moves(self):
        pass

    def move_rules(self):
        pass
    pass
