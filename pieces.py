import board
import settings as sett

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
    vision: ['board.Square']
    # rules: {''}

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

    def create_vision(self, board_: 'board.Board'):
        """
        Create list of squares that this piece could move too, no obstructions
        """
        raise NotImplementedError

    def get_vision(self):
        """
        Return vision of piece
        """
        return self.vision

    def move_piece_object(self, to_row: str, to_file: str,
                          board_: 'board.Board'):
        """
        Changes file and row position in object
        DOES NOT MOVE PIECE IN BOARD OBJECT JUST OBJECT VARIABLES
        """
        self.row = to_row
        self.file = to_file
        self.vision = self.create_vision(board_)

    def capture(self):
        """
        Flag captured, once captured piece is out of game
        """
        self.captured = True


class Pawn(Piece):
    first_move: bool  # True if first move has been made

    def __init__(self, file: str, row: str, type_: str, team: str):
        Piece.__init__(self, file, row, type_, team)
        self.first_move = False

    def make_first_move(self):
        """
        This pawn made their first move, change attribute boolean
        """
        self.first_move = True

    def create_vision(self, board_: 'board.Board') -> None:
        self.vision = []
        if self.first_move:
            if self.team == sett.teams[0]:  # White team
                one_row_above = str(sett.rows.index(self.row) + 1 + 1)
            else:  # Black team
                print(True, 1)
                one_row_above = str(sett.rows.index(self.row) + 1 - 1)

            if int(one_row_above) >= 8:
                self.promote()
            else:
                self.vision.append(board_.get_square(self.file,
                                                     one_row_above))
        else:  # Can move two squares on first move if desired
            if self.team == sett.teams[0]:
                one_row_above = str(sett.rows.index(self.row) + 1 + 1)
                two_row_above = str(int(one_row_above) + 1)
            else:
                one_row_above = str(sett.rows.index(self.row) + 1 - 1)
                two_row_above = str(int(one_row_above) - 1)

            self.vision.append(board_.get_square(self.file, one_row_above))
            self.vision.append(board_.get_square(self.file, two_row_above))


    def promote(self):
        pass

    def legal_moves(self):
        """
        Given vision, where can the piece actually move
        """
        pass


class Rook(Piece):
    def create_vision(self, board_: 'board.Board'):
        """
        Create vision for the rook piece
        """
        self.vision = []
        r = self.row
        f = self.file
        current_square = board_.get_square(f, r)

        # Lateral, all squares in its lateral direction minus its self
        for i in range(8):
            self.vision.append(board_.get_square(sett.files[i], r))
        # All vertical squares in file
        for i in range(8):
            self.vision.append(board_.get_square(f, sett.rows[i]))

        # Two copies of current square are added, once lateral once vertical
        self.vision.remove(current_square)
        self.vision.remove(current_square)


    def legal_moves(self):
        pass



class Knight(Piece):
    def create_vision(self, board_: 'board.Board'):
        self.vision = []
        r = sett.rows.index(self.row)
        f = sett.files.index(self.file)

        horse_codes = [[f + 1, r + 2],
                       [f - 1, r + 2],
                       [f + 1, r - 2],
                       [f - 1, r - 2],
                       [f + 2, r + 1],
                       [f + 2, r - 1],
                       [f - 2, r + 1],
                       [f - 2, r - 1]]

        for code in horse_codes:
            if 0 <= code[0] < 8 and 0 <= code[1] < 8:
                self.vision.append(board_.get_square(sett.files[code[0]],
                                                     sett.rows[code[1]]))

        # try:
        #     # Squares above
        #     self.vision.append(board_.get_square(sett.files[r + 1],
        #                                          sett.rows[r + 2]))
        # try:
        #     self.vision.append(board_.get_square(sett.files[r - 1],
        #                                          sett.rows[r + 2]))
        # try:
        #     # Squares below
        #     self.vision.append(board_.get_square(sett.files[r + 1],
        #                                          sett.rows[r - 2]))
        # try:
        #     self.vision.append(board_.get_square(sett.files[r - 1],
        #                                          sett.rows[r - 2]))
        # try:
        #     # Squares right
        #     self.vision.append(board_.get_square(sett.files[r + 2],
        #                                          sett.rows[r + 1]))
        # try:
        #     self.vision.append(board_.get_square(sett.files[r + 2],
        #                                          sett.rows[r - 2]))
        # try:
        #     # Squares left
        #     self.vision.append(board_.get_square(sett.files[r - 2],
        #                                          sett.rows[r + 1]))
        # try:
        #     self.vision.append(board_.get_square(sett.files[r - 2],
        #                                          sett.rows[r - 1]))






class Bishop(Piece):

    def create_vision(self, board_: 'board.Board'):
        self.vision = []
        r = sett.rows.index(self.row)
        f = sett.files.index(self.file)

        lateral_inc = f
        vertical_inc = r

        # Up and to the right diagonals
        while 0 <= lateral_inc < 8 and 0<= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc += 1
            vertical_inc += 1
        lateral_inc = f
        vertical_inc = r

        # Up and to the left diagonals
        while 0 <= lateral_inc < 8 and 0 <= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc -= 1
            vertical_inc += 1
        lateral_inc = f
        vertical_inc = r

        # Down and to the right
        while 0 <= lateral_inc < 8 and 0 <= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc += 1
            vertical_inc -= 1
        lateral_inc = f
        vertical_inc = r

        # Down and to the left
        while 0 <= lateral_inc < 8 and 0 <= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc -= 1
            vertical_inc -= 1
        lateral_inc = f
        vertical_inc = r


class King(Piece):

    def create_vision(self, board_: 'board.Board'):
        self.vision = []
        r = sett.rows.index(self.row)
        f = sett.files.index(self.file)

        # Add top square
        if r != 7:
            # Add top left
            if f != 0:
                self.vision.append(board_.get_square(sett.files[f - 1],
                                                     sett.rows[r + 1]))
            # Add top right
            if f != 7:
                self.vision.append(board_.get_square(sett.files[f + 1],
                                                     sett.rows[r + 1]))

            self.vision.append(board_.get_square(sett.files[f],
                                                 sett.rows[r + 1]))
        # Add bottom square
        if r != 0:
            # Add bottom left square
            if f != 0:
                self.vision.append(board_.get_square(sett.files[f - 1],
                                                    sett.rows[r - 1]))
            # Add bottom right square
            if f != 7:
                self.vision.append(board_.get_square(sett.files[f + 1],
                                                     sett.rows[r - 1]))
            self.vision.append(board_.get_square(sett.files[f],
                                                 sett.rows[r - 1]))

        # Add left square
        if f != 0:
            self.vision.append(board_.get_square(sett.files[f - 1],
                                                 sett.rows[r]))
        # Add right square
        if f != 7:
            self.vision.append(board_.get_square(sett.files[f + 1],
                                                 sett.rows[r]))


class Queen(Piece):

    def create_vision(self, board_: 'board.Board'):
        self.vision = []
        r = self.row
        f = self.file
        current_square = board_.get_square(f, r)

        # Lateral, all squares in its lateral direction minus its self
        for i in range(8):
            self.vision.append(board_.get_square(sett.files[i], r))
        # All vertical squares in file
        for i in range(8):
            self.vision.append(board_.get_square(f, sett.rows[i]))

        # Two copies of current square are added, once lateral once vertical
        self.vision.remove(current_square)
        self.vision.remove(current_square)

        # Lateral and vertical squares all added
        # -------------------------------------

        r = sett.rows.index(self.row)
        f = sett.files.index(self.file)

        lateral_inc = f
        vertical_inc = r

        # Up and to the right diagonals
        while 0 <= lateral_inc < 8 and 0<= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc += 1
            vertical_inc += 1
        lateral_inc = f
        vertical_inc = r

        # Up and to the left diagonals
        while 0 <= lateral_inc < 8 and 0 <= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc -= 1
            vertical_inc += 1
        lateral_inc = f
        vertical_inc = r

        # Down and to the right
        while 0 <= lateral_inc < 8 and 0 <= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc += 1
            vertical_inc -= 1
        lateral_inc = f
        vertical_inc = r

        # Down and to the left
        while 0 <= lateral_inc < 8 and 0 <= vertical_inc < 8:
            self.vision.append(board_.get_square(sett.files[lateral_inc],
                                                 sett.rows[vertical_inc]))
            lateral_inc -= 1
            vertical_inc -= 1
        lateral_inc = f
        vertical_inc = r


    def legal_moves(self):
        pass


