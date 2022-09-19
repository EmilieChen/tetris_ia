import numpy as np


class Board:
    
    @classmethod
    def create_from(cls, grid):
        board = Board(grid.shape)
        board.grid = grid.copy()
        return board
    
    def __init__(self, shape=(10,20)):
        self.grid = np.zeros(shape)
        
    def can_place(self, tetromino):
        pos = tetromino.position()
        x,y = self.unravel(pos)
        mask= (pos >=0) & (pos < self.grid.shape) & (self.grid[x,y] == 0)
        return np.all(mask, axis=(-1,-2))
    
    def placement(self, tetromino):
        mask = self.can_place(tetromino)
        pos  = tetromino.position()
        pos  = pos[mask]
        x, y = self.unravel(pos)
        self.grid[x,y] = tetromino.type
        
    def unravel(self, position):
        x = np.take(position, [0], axis=-1)
        y = np.take(position, [1], axis=-1)
        x = np.clip(x, 0, self.grid.shape[0]-1)
        y = np.clip(y, 0, self.grid.shape[1]-1)
        return x, y
        
    def column_height(self):
        height = self.grid.shape[1] - (self.grid > 0).argmax(axis=1)
        height[self.grid.sum(axis=1) == 0] = 0
        return height
    
    def column_depth(self):
        return self.grid.shape[1] - self.column_height()
    
    #def free_blocks(self):
    #    rows = np.arange(self.grid.shape[0])
    #    cols = self.column_depth()
    #    grid = np.zeros_like(self.grid)
    #    grid[rows,cols-1] = 1
    #    grid = grid[:,::-1].cumsum(axis=1)[:,::-1]
    #    idx = grid.nonzero()
    #    idx = np.stack(idx, axis=1)
    #    return idx
        
    def print(self):
        s = '   o' + '--' * self.grid.shape[0] + 'o\n'
        s += '\n'.join(["{:2d}".format(n) + ' |' + ''.join(['[]' if j else '  ' for j in i]) + '|' for n,i in enumerate(self.grid.T)])
        s += '\n   o' + '--' * self.grid.shape[0] + 'o'
        print(s)

        

class Tetromino:
    
    __tetro = {
        'T': np.array([(0, 0), (-1,  0), ( 1,  0), ( 0, -1)]),
        'J': np.array([(0, 0), (-1,  0), ( 0, -1), ( 0, -2)]),
        'L': np.array([(0, 0), ( 1,  0), ( 0, -1), ( 0, -2)]),
        'Z': np.array([(0, 0), (-1,  0), ( 0, -1), ( 1, -1)]),
        'S': np.array([(0, 0), (-1, -1), ( 0, -1), ( 1,  0)]),
        'I': np.array([(0, 0), ( 0, -1), ( 0, -2), ( 0, -3)]),
        'O': np.array([(0, 0), ( 0, -1), (-1,  0), (-1, -1)]),
    }
    
    __type = {'T': 1, 'J': 2, 'L': 3, 'Z': 4, 'S': 5, 'I': 6, 'O': 7}
    
    @classmethod
    def create(cls, name, anchor=(0,0)):
        return Tetromino(cls.__tetro[name], anchor, cls.__type[name])
    
    def __init__(self, blocks, anchor, type):
        self.blocks = np.array(blocks)
        self.anchor = np.array(anchor).reshape(-1,2)
        self.type   = type
        self.blocks.setflags(write=False)
        self.anchor.setflags(write=False)
        
    def position(self):
        return np.squeeze(self.blocks[None] + self.anchor[:,None])
    
    def move_to(self, anchor):
        return Tetromino(self.blocks, anchor, self.type)
            
    def move_right(self):
        return Tetromino(self.blocks, self.anchor + (1,0), self.type)
    
    def move_left(self):
        return Tetromino(self.blocks, self.anchor - (1,0), self.type)

    def move_down(self):
        return Tetromino(self.blocks, self.anchor + (0,1), self.type)

    def rotate_right(self):
        return Tetromino(self.blocks[:,[1,0]] * (-1,1), self.anchor, self.type)
    
    def rotate_left(self):
        return Tetromino(self.blocks[:,[1,0]] * (1,-1), self.anchor, self.type)
        
    def print(self, shape=(10,20)):
        board = Board(shape)
        board.placement(self)
        board.print()
