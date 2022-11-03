from board import Board
from coord import Coord
from game import Game
from piece import Piece
from pygame_screen import PygameScreen

# for i in range(1,8):
#     piece = Piece(i)
#     for coords in piece.shapes_coords:
#         for x in range(4):
#             for y in range(4):
#                 if (x,y) in coords:
#                     print("#", end="  ")
#                 else:
#                     print("-", end="  ")
#             print("")
#         print("")
#     print("++++++++++++++++++++++++++++++")
from screenable import Screenable

game = Game(PygameScreen(20, 15))
board = Board(PygameScreen(20, 15))
game.start()

