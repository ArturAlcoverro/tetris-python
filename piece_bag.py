import random

from piece import Piece


class PieceBag:
    def __init__(self):
        self.bag = []

    def _fill_bag(self):
        self.bag = list(range(1, 8))
        random.shuffle(self.bag)

    def next(self):
        if len(self.bag) == 0:
            self._fill_bag()
        return Piece(self.bag.pop())
