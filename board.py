from coord import Coord
from screenable import Screenable

HEIGHT = 20
WIDTH = 15


class Board:
    def __init__(self, screen: Screenable):
        self.matrix = []
        self.screen = screen
        self.fill_matrix("#FFFFFF")

    def send(self):
        self.screen.render(self.matrix)

    def paint_coord(self, coord: Coord, initCoord: Coord = Coord(0, 0), color="#000000"):
        y = initCoord.y + coord.y
        x = initCoord.x + coord.x
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return
        self.matrix[initCoord.y + coord.y][initCoord.x + coord.x] = color

    def paint_coords(self, coords: [Coord], initCoord: Coord = Coord(0, 0), color="#000000"):
        for coord in coords:
            self.paint_coord(coord=coord, initCoord=initCoord, color=color)

    def paint_square(self, coord1: Coord, coord2: Coord, color):
        for y in range(coord2.y - coord1.y + 1):
            for x in range(coord2.x - coord1.x + 1):
                self.matrix[coord1.y + y][coord1.x + x] = color

    def paint_board(self, matrix):
        self.matrix = matrix

    def fill_matrix(self, color):
        self.matrix = []
        for i in range(HEIGHT):
            self.matrix.append([])
            for j in range(WIDTH):
                self.matrix[i].append(color)

    def print_str(self):
        for arr in self.matrix:
            for cell in arr:
                print(f"|{cell}", end="")
            print("|")
