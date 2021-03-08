import pygame
import settings as sett
import game
import pieces
import graphics_process as gp


def master_game():
    screen = pygame.display.set_mode(sett.size)
    running = True
    pygame.display.set_caption("BaldCorpium")

    master_board = game.master_board

    while running:
        file_spacing = 0
        row_spacing = 0
        screen.fill(sett.gray)

        for row in master_board.squares.values():
            for sq in row:
                pygame.draw.rect(screen, sq.colour, (file_spacing,
                                                     row_spacing,
                                                     sett.sq_size,
                                                     sett.sq_size))
                file_spacing += sett.sq_size
            row_spacing += sett.sq_size
            file_spacing = 0

        draw_pieces(screen)
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def draw_pieces(screen: 'pygame screen'):

    file_spacing = 0
    row_spacing = 0
    for row in game.master_board.squares.values():
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



if __name__ == "__main__":
    master_game()
