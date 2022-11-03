import time

from board import Board
from coord import Coord
from piece_bag import PieceBag
from screenable import Screenable


class Game:
    def __init__(self, screen: Screenable):
        self.board = Board(screen)
        self.bag = PieceBag()
        self.loop = True
        self.piece = self.bag.next()
        self.next_piece = self.bag.next()

    def start(self):
        while self.loop:
            print(self.bag.next().shapes_coords)
            shape = self.bag.next()
            coords = shape.shapes_coords[shape.shapes_index]
            self.board.paint_coords(coords=coords, initCoord=Coord(0, -2), color="#FF0000")
            self.board.send()
            time.sleep(1)

    def draw_skeleton(self):
        self.board.paint_square(Coord(0, 0), Coord(9, 19), "#")
        self.board.paint_square(Coord(11, 6), Coord(14, 9), "#")

    def draw_next_piece(self):
        pass

    def stop(self):
        self.loop = False

