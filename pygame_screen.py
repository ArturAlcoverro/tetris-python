from screenable import Screenable
import pygame


def _translate_matrix(matrix):
    for iy, y in enumerate(matrix):
        for ix, x in enumerate(y):
            if x == "#":
                matrix[iy][ix] = "#FFFFFF"
            elif x == "-":
                matrix[iy][ix] = "#888888"


class PygameScreen(Screenable):
    def __init__(self, hCells, wCells):
        super().__init__(hCells, wCells)
        self.height = 600
        self.width = 450
        self.cellHeight = 600 / hCells
        self.cellWidth = 450 / wCells

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.flip()

    def render(self, matrix):
        self.screen.fill((0, 0, 0))
        _translate_matrix(matrix)

        for y in range(self.hCells):
            for x in range(self.wCells):
                polygon = [
                    (x * self.cellWidth, y * self.cellHeight),
                    ((x + 1) * self.cellWidth, y * self.cellHeight),
                    ((x + 1) * self.cellWidth, (y + 1) * self.cellHeight),
                    (x * self.cellWidth, (y + 1) * self.cellHeight)
                ]
                pygame.draw.polygon(self.screen, matrix[y][x], polygon)

        pygame.display.flip()

