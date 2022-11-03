from coord import Coord

I_PIECE = 1
L_PIECE = 2
J_PIECE = 3
S_PIECE = 4
Z_PIECE = 5
T_PIECE = 6
O_PIECE = 7


class Piece:
    def __init__(self, piece_id: int):
        self.piece_id = piece_id
        self.shapes = self._create_shapes()
        self.shapes_coords = self._get_shape_coords()
        self.color = self._set_color()
        self.shapes_index = 0

    def _create_shapes(self):
        if self.piece_id == I_PIECE:
            return [
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    ["#", "#", "#", "#"],
                    [" ", " ", " ", " "]
                ],
                [
                    [" ", " ", "#", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", " "]
                ],
            ]
        if self.piece_id == L_PIECE:
            return [
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    [" ", "#", "#", "#"],
                    [" ", "#", " ", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", "#", "#", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", "#"],
                    [" ", "#", "#", "#"],
                    [" ", " ", " ", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", "#"]
                ],
            ]
        if self.piece_id == J_PIECE:
            return [
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    [" ", "#", "#", "#"],
                    [" ", " ", " ", "#"]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", " "],
                    [" ", "#", "#", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", "#", " ", " "],
                    [" ", "#", "#", "#"],
                    [" ", " ", " ", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", "#", "#"],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", " "]
                ],
            ]
        if self.piece_id == S_PIECE:
            return [
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    [" ", " ", "#", "#"],
                    [" ", "#", "#", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", "#"],
                    [" ", " ", " ", "#"]
                ],
            ]
        if self.piece_id == Z_PIECE:
            return [
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    [" ", "#", "#", " "],
                    [" ", " ", "#", "#"]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", "#"],
                    [" ", " ", "#", "#"],
                    [" ", " ", "#", " "]
                ],
            ]
        if self.piece_id == T_PIECE:
            return [
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    [" ", "#", "#", "#"],
                    [" ", " ", "#", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", "#", " "],
                    [" ", "#", "#", " "],
                    [" ", " ", "#", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", "#", " "],
                    [" ", "#", "#", "#"],
                    [" ", " ", " ", " "]
                ],
                [
                    [" ", " ", " ", " "],
                    [" ", " ", "#", " "],
                    [" ", " ", "#", "#"],
                    [" ", " ", "#", " "]
                ],
            ]
        if self.piece_id == O_PIECE:
            return [
                [
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    [" ", "#", "#", " "],
                    [" ", "#", "#", " "]
                ],
            ]

    def _set_color(self):
        if self.piece_id == I_PIECE: return "#00AAEC"
        if self.piece_id == L_PIECE: return "#FE9738"
        if self.piece_id == J_PIECE: return "#563FE0"
        if self.piece_id == S_PIECE: return "#EC1A40"
        if self.piece_id == Z_PIECE: return "#5CD051"
        if self.piece_id == T_PIECE: return "#E14AB7"
        if self.piece_id == O_PIECE: return "#FFDB20"

    def _get_shape_coords(self):
        coords = []
        for shape in self.shapes:
            coord = []
            for idy, y in enumerate(shape):
                for idx, x in enumerate(y):
                    if x == "#": coord.append(Coord(idx, idy))
            coords.append(coord)

        print(coords)
        return coords
