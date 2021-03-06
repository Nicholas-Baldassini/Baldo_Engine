import game
import settings as sett
from typing import List, Optional
import board
import pieces
"""
Chess strings are retrieved from https://old.chesstempo.com/ database and 
processed according to their formatting
"""

move_string = '1. b3 e5 2. Bb2 Nc6 3. e3 Nf6 4. Bb5 Bd6 5. Ne2 O-O 6. Ng3 Re8 7. O-O e4 8. f4 a6 9. Be2 Bc5 10. Bxf6 Qxf6 11. Nc3 Bxe3+ 12. Kh1 Bd4 13. Ngxe4 Qh6 14. Bc4 d6 15. Qf3 Be6 16. Rae1 Bb6 17. f5 Bxc4 18. bxc4 Ne5 19. Qe2 c6 20. g4 Bc7 21. Qg2 Qh4 22. Re3 Qd8 23. g5 d5 24. cxd5 Kf8 25. Rh3 cxd5 26. Rxh7 dxe4 27. f6 Ng6 28. Qh3 gxf6 29. gxf6 '
if not move_string:
    move_string = input('Move string: ')

fake_order = move_string.strip().split(' ')
move_order = []
for move in fake_order:
    if move[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        move_order.append(move)


is_white = True


def process_move_code(code: str, board_: 'board.Board', colour: str) -> \
                                                           (str,
                                                            str,
                                                            str,
                                                            bool,
                                                            None):
    """
    Responsible for processing the code given, examples
    --------------------------------------------------

    Output tuple:
    ( colour of piece,
    type of piece to move,
    The code square the piece is to be moved to,
    piece on destination is to be captured,
    promotion information

    # ToDo Castle's information)


    B - bishop
    N - knight
    R - rook
    K - king
    Q - queen
    'None' - pawn

    x - non-pawn captures
    'File' - pawn captures

    # Todo Ambiguous moves

    'code + piece type' - pawn promotion
    e8=Q - pawn promotion to queen on

    0-0 - king side castle
    0-0-0 - queen side castle

    + - check

    # - checkmate

    Examples:
    =========
    Qe5 queen moves to square e5

    d4 - move pawn to d4

    0-0 - castle king side

    a8=K+ - promote pawn on a8 with check

    hxg8=Q - pawn from h file captures piece on g8 and promote to queen

    0-0 castle with check
    """
    castles = ['0-0', '0-0-0']
    check_and_mate = ['+', '#']
    if code in castles:
        pass
    if code[-1] in check_and_mate:
        pass

    if '=' in code: # Promotion
        pass



def make_move(move: str):
    """
    Responsible for finding which piece is to move and to move it
    """
    if move[0] not in sett.piece_move_notation:
        type = sett.piece_types[-1]
    else:
        type = sett.piece_types[sett.piece_move_notation.index(move[0])]

    team = sett.teams[(game.turn_number - 1) % 2]
    team_pieces = game.master_board.get_colour_pieces_on_board(
        team)

    # The piece that is to be moved or atleast suppose to move
    the_chosen_one = None
    the_chosen_one = game.master_board.get_type_of_pieces(type, team)
    if the_chosen_one is None:
        print('No piece is found that can move')
        raise Exception

    file = move[-2]
    row = move[-1]

    game.move_piece(the_chosen_one[0], row, file)




# print(move_order)
