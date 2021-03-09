import pygame
import settings as sett
import game
import pieces
import graphics_process as gp
import moveStringProcessing as MP


def master_game():
    screen = pygame.display.set_mode(sett.size)
    running = True
    pygame.display.set_caption("BaldCorpium")

    global pygame_board
    pygame_board = {}
    skip = 0
    draw_squares(screen)

    while running:
        skip += 1
        # Screen object that do not need to be processed every iteration
        if (skip % sett.FPS // 10) == 0:
            # screen.fill(sett.gray)
            draw_squares(screen)
            draw_additionals(screen)
            # hovered_square()
            skip = 0

        draw_pieces(screen)
        detect_mouse_additional(screen)
        move_piece()


        pygame.display.update()
        pygame.time.delay(sett.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



def move_piece():
    flip = False
    pos = pygame.mouse.get_pos()
    posx = pos[0]
    posy = pos[1]
    fu = sett.move_piece_button
    move = ''

    # Check for button flip event
    # Add any other additional buttons or interactions we want

    if fu['x'] <= posx <= fu['x'] + fu['width'] and \
            fu['y'] <= posy <= fu['y'] + fu['height']:
        if pygame.mouse.get_pressed(3)[0]:
            move = input('Where do you want to move: ')
    if move:
        MP.make_move(move)



def draw_squares(screen: 'pygame screen') -> None:
    """
    Draws just the squares onto the pygame screen
    """
    file_spacing = 0
    row_spacing = 0
    for row in game.master_board.get_board():
        for sq in row:
            pygame.draw.rect(screen, sett.sq_colours[sq.cur_colour],
                                   (file_spacing,
                                    row_spacing,
                                    sett.sq_size,
                                    sett.sq_size))

            pygame_board[sq] = {'x': file_spacing, 'y': row_spacing,
                                'width': file_spacing + sett.sq_size,
                                'height': row_spacing + sett.sq_size}
            file_spacing += sett.sq_size
        row_spacing += sett.sq_size
        file_spacing = 0


def draw_pieces(screen: 'pygame screen') -> None:
    file_spacing = 0
    row_spacing = 0
    for row in game.master_board.get_board():
        for sq in row:
            if isinstance(sq.holding, pieces.Piece):
                t = sq.holding.team
                ty = sq.holding.type_
                icon = gp.combined_icons.get(t)
                icon = icon.get(str(t)[0] + ty + '_icon')

                screen.blit(icon, (file_spacing + gp.icon_scaling // 2,
                                   row_spacing + gp.icon_scaling // 2))

            file_spacing += sett.sq_size
        file_spacing = 0
        row_spacing += sett.sq_size


def draw_additionals(screen) -> None:
    """
    Draw additional objects to screen, flip, undo...
    """
    fb = sett.flip_button_ui
    mp = sett.move_piece_button
    pygame.draw.rect(screen, fb.get('colour'), (fb.get('x'), fb.get('y'),
                                                fb.get('width'),
                                                fb.get('height')))

    pygame.draw.rect(screen, mp.get('colour'), (mp.get('x'), mp.get('y'),
                                                mp.get('width'),
                                                mp.get('height')))




# def hovered_square() -> 'Square object':
#     pos = pygame.mouse.get_pos()
#     posx = pos[0]
#     posy = pos[1]
#
#     soi = None
#     for sq in pygame_board:
#         if pygame_board[sq]['x'] <= posx <= pygame_board[sq]['width'] and \
#                 pygame_board[sq]['y'] <= posy <= pygame_board[sq]['height']:
#             sq.change_colour('hovered')
#             soi = sq
#         else:
#             if sq.cur_colour is not sq.default_colour:
#                 sq.change_colour(sq.default_colour)
#     return soi


def detect_mouse_additional(screen) -> None:
    """
    Check for mouse moving over a piece and if let go, move the piece
    """
    flip = False
    pos = pygame.mouse.get_pos()
    posx = pos[0]
    posy = pos[1]
    fu = sett.flip_button_ui

    # Check for button flip event
    # Add any other additional buttons or interactions we want

    if fu['x'] <= posx <= fu['x'] + fu['width'] and \
            fu['y'] <= posy <= fu['y'] + fu['height']:
        if pygame.mouse.get_pressed(3)[0]:
            pygame.time.delay(100)
            flip = True

    if flip:
        game.master_board.flip_board()
        flip = False


if __name__ == "__main__":
    master_game()
