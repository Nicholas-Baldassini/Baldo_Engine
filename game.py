"""
Do the actual game computation in here, then give the outputs to pygame
Main control center of the game + engine
"""
import board
import pieces as p
import settings as sett

master_board = board.create_board()
turn_number = 1
# if odd, white's turn, if even, black's turn


def start_game():
    # White pieces
    wr1 = p.Rook(sett.files[0], sett.rows[0],
                 sett.piece_types[0], sett.teams[0])
    wkn1 = p.Knight(sett.files[1], sett.rows[0],
                    sett.piece_types[1], sett.teams[0])
    wb1 = p.Bishop(sett.files[2], sett.rows[0],
                   sett.piece_types[2], sett.teams[0])
    wq = p.Queen(sett.files[3], sett.rows[0],
                 sett.piece_types[3], sett.teams[0])
    wk = p.King(sett.files[4], sett.rows[0],
                sett.piece_types[4], sett.teams[0])
    wb2 = p.Bishop(sett.files[5], sett.rows[0],
                   sett.piece_types[2], sett.teams[0])
    wkn2 = p.Knight(sett.files[6], sett.rows[0],
                    sett.piece_types[1], sett.teams[0])
    wr2 = p.Rook(sett.files[7], sett.rows[0],
                 sett.piece_types[0], sett.teams[0])

    master_board.place_piece(wr1)
    master_board.place_piece(wkn1)
    master_board.place_piece(wb1)
    master_board.place_piece(wq)
    master_board.place_piece(wk)
    master_board.place_piece(wb2)
    master_board.place_piece(wkn2)
    master_board.place_piece(wr2)

    for i in range(8):
        pawn = p.Pawn(sett.files[i],
                      sett.rows[1], sett.piece_types[5], sett.teams[0])
        master_board.place_piece(pawn)

    # Black pieces
    br1 = p.Rook(sett.files[0], sett.rows[7],
                 sett.piece_types[0], sett.teams[1])
    bkn1 = p.Knight(sett.files[1], sett.rows[7],
                    sett.piece_types[1], sett.teams[1])
    bb1 = p.Bishop(sett.files[2], sett.rows[7],
                   sett.piece_types[2], sett.teams[1])
    bq = p.Queen(sett.files[3], sett.rows[7],
                 sett.piece_types[3], sett.teams[1])
    bk = p.King(sett.files[4], sett.rows[7],
                sett.piece_types[4], sett.teams[1])
    bb2 = p.Bishop(sett.files[5], sett.rows[7],
                   sett.piece_types[2], sett.teams[1])
    bkn2 = p.Knight(sett.files[6], sett.rows[7],
                   sett.piece_types[1], sett.teams[1])
    br2 = p.Rook(sett.files[7], sett.rows[7],
                 sett.piece_types[0], sett.teams[1])

    master_board.place_piece(br1)
    master_board.place_piece(bkn1)
    master_board.place_piece(bb1)
    master_board.place_piece(bq)
    master_board.place_piece(bk)
    master_board.place_piece(bb2)
    master_board.place_piece(bkn2)
    master_board.place_piece(br2)

    for i in range(8):
        pawn = p.Pawn(sett.files[i],
                      sett.rows[6], sett.piece_types[5], sett.teams[1])
        master_board.place_piece(pawn)

    master_board.init_coloured_pieces()
    for peece in master_board.coloured_pieces['white']:
        peece.create_vision(master_board)
    for peece in master_board.coloured_pieces['black']:
        peece.create_vision(master_board)



def can_piece_move(piece: 'Piece object', to_row: str, to_file: str) -> bool:
    """
    Given a piece and a destination, return True if piece can move there
    Check vision of a piece then if anything is blocking it
    Maybe put it in piece class
    """
    pass


def En_passant():
    pass

def castle():
    pass


def move_piece(piece: 'Piece object', to_row: str, to_file: str) -> None:
    """
    Called after calculations done to figure out where piece is to be moved

    Changes file and row position of the piece object
    Changes the actual position on the board object as well
    """
    # if not can_piece_move(piece, to_row, to_file):
    #     print('Piece can not move here')
    #     raise Exception

    global turn_number

    if piece is None:
        return None
    # Remove current piece from wherever it is on board
    worked = master_board.remove_piece(piece)
    if not worked:
        print("Piece: {} on {} was not found ".format(piece.type_, piece.code) +
              "in board.squares")
        raise Exception

    # Change piece object attributes
    piece.move_piece_object(to_row, to_file, master_board)
    piece.create_vision(master_board)

    # Move piece to new spot on board
    master_board.place_piece(piece)

    turn_number += 1


if __name__ == '__main__':
    start_game()
    # print(master_board)
    master_board.flip_board()
    # print(master_board)
    # print(master_board.get__colour_pieces_on_board('white'))
else:
    start_game()
