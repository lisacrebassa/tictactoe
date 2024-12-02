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

def has_winner(self):
    #need at least 5 moves before x hits three in a row
    if (len(self.moves) <5):
       return None
    
    #check rows for win
    for row in range(self.dimension):
        unique_rows = set(self.grid[row])
        if (len(unique_rows) == 1):
            value = unique_rows.pop()
            if (value != None):
                return value
            
    # check columns for win
    for col in range(self.dimension):
        unique_cols = set()
        for row in range(self.dimension):
            unique_cols.add(self.grid[row][col])

        if (len(unique_cols) == 1):
            value = unique_cols.pop()
            if (value != None):
                return value