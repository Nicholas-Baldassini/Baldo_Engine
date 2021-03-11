"""
File to extract and process the sprites for pygame to use to display to screen
"""

import pygame
import settings as sett
icon_scaling = 16

path = r'/Users/baldo/Desktop/BaldCorpium/pygame_pics/'

wking_icon = pygame.image.load(path + r'white_king.png')
wqueen_icon = pygame.image.load(path + r'white_queen.png')
wbishop_icon = pygame.image.load(path + r'white_bishop.jpg')
wknight_icon = pygame.image.load(path + r'white_horse.jpg')
wrook_icon = pygame.image.load(path + r'white_rook.png')
wpawn_icon = pygame.image.load(path + r'white_pawn.jpg')
white_icons = {'wking_icon': wking_icon, 'wqueen_icon': wqueen_icon,
               'wbishop_icon': wbishop_icon, 'wknight_icon': wknight_icon,
               'wrook_icon': wrook_icon, 'wpawn_icon': wpawn_icon}

bking_icon = pygame.image.load(path + r'black_king.jpg')
bqueen_icon = pygame.image.load(path + r'black_queen.png')
bbishop_icon = pygame.image.load(path + r'black_bishop.png')
bknight_icon = pygame.image.load(path + r'black_horse.png')
brook_icon = pygame.image.load(path + r'black_rook.jpg')
bpawn_icon = pygame.image.load(path + r'black_pawn.png')

black_icons = {'bking_icon': bking_icon, 'bqueen_icon': bqueen_icon,
               'bbishop_icon': bbishop_icon, 'bknight_icon': bknight_icon,
               'brook_icon': brook_icon, 'bpawn_icon': bpawn_icon}


for icon in white_icons:
    white_icons[icon] = pygame.transform.scale(white_icons[icon],
                                              (sett.sq_size - icon_scaling,
                                               sett.sq_size - icon_scaling))

for icon in black_icons:
    black_icons[icon] = pygame.transform.scale(black_icons[icon],
                                               (sett.sq_size - icon_scaling,
                                                sett.sq_size - icon_scaling))

combined_icons = {'white': white_icons, 'black': black_icons}
