
class Screenable:
    @staticmethod
    def __hex_to_rgb(hex: str):
        value = hex.strip("#")
        print(tuple(int(value[i:i + 2], 16) for i in (0, 2, 4)))

    def __init__(self, hCells, wCells):
        self.hCells = hCells
        self.wCells = wCells

    def render(self, matrix):
        pass
