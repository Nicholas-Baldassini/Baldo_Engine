# Settings of the game
# Add more settings of the game here, random, any move no rules...
# DO NOT CHANGE ANY OF THESE
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']
teams = ['white', 'black']
piece_types = ['rook', 'knight', 'bishop', 'queen', 'king', 'pawn']
square_states = ['white', 'black', 'hovered']
piece_move_notation = ['R', 'N', 'B', 'Q', 'K']
"""



"""
# pygame settings, UI COMPONENTS
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
hovered = (188, 86, 86)
dimension = 700
bottom_bar = 60
size = (dimension, dimension + bottom_bar)
sq_size = dimension // 8
sq_colours = {'white': white, 'black': black, 'gray': gray, 'hovered': hovered}



FPS = 100  # Milliseconds delay, 100 = 1 second
flip_button_ui = {'height': bottom_bar - 10, 'width': dimension // 6,
                  'x': 0, 'y': dimension, 'colour': gray}

move_piece_button = {'height': bottom_bar - 10, 'width': dimension // 6,
                     'x': 200, 'y': dimension, 'colour': gray}
