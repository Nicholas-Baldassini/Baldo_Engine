# Do the actual game computation in here, then give the outputs to pygame
import board
import pieces as p
import settings as sett

master_board = board.create_board()


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


def move_piece(piece: 'Piece object', to_row: str, to_file: str) -> None:
    """
    Called after calculations done to figure out where piece is to be moved

    Changes file and row position of the piece object
    Changes the actual position on the board object as well
    """
    worked = master_board.remove_piece(piece)
    if not worked:
        print("Piece:{} on {} was not found " +
              "in board.squares".format(piece.type_, piece.code))
        raise Exception

    piece.move_piece(to_row, to_file)
    master_board.place_piece(piece)


start_game()
if __name__ == '__main__':
    start_game()
    print(master_board)
