import enum

class Player(enum.Enum):
    x = 1
    o = 2

    @property
    def other(self):
        return Player.x if self == Player.o else Player.o
    
import copy
from .player import Player

MARKER_TO_CHAR = {
    None: '.',
    Player.x: 'x',
    Player.o: 'o',
}

class Board():
    def __init__(self):
        self.dimension = 3
        self.grid = [[ None for y in range (self.dimension)]for x in range (self.dimension)]
        self.moves = []

    def print(self):
        print()
        for row in range (self.dimension):
            line = []
            for col in range(self.dimension):
                line.append(MARKER_TO_CHAR[self.grid[row][col]])
            print('%s' % (''.join(line)))