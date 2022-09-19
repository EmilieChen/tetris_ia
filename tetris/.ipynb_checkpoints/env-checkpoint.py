from .model import TetrisEngine
from .render import Rendering
import numpy as np


def wrap_state(state):
    grid, piece = state
    return Board(grid), Tetromino(piece)


class TetrisEnv:
    
    def __init__(self, random_start=False):
        self.game = TetrisEngine(random_start)
        self.screen = None
        
    def seed(self, seed):
        self.game.seed(seed)
        
    def reset(self):
        self.game.clear()
        if self.screen: self.screen.init()
        state = self.game.state()
        return wrap_state(state)

    def step(self, action):
        state, reward, done = self.game.step(action)
        return wrap_state(state), reward, done
           
    def render(self, mode=None):
        if not self.screen:
            self.screen = Rendering(self.game)
            self.screen.init()
        frame = self.screen.render()
        return frame
               
    def close(self):
        if self.screen: 
            self.screen.render()
            self.screen.close()
            self.screen = None
            
    def __repr__(self):
        return str(self.game)


class Board:
    
    def __init__(self, grid=np.zeros((10,20))):
        self.grid = np.array(grid).copy()
        
    def rows(self):
        return self.grid.shape[1]
    
    def columns(self):
        return self.grid.shape[0]
        
    def can_place(self, tetromino):
        pos = tetromino.position()
        #x,y = pos[:,0], pos[:,1]
        #return np.all((pos >=0) & (pos < self.grid.shape)) and np.all(self.grid[x,y] == 0)
        mask = pos[:,1] >= 0  # mask for cutting out the blocks above the ceiling
        x,y = pos[mask,0], pos[mask,1]
        return np.all(pos[:,0] >=0) and np.all(pos < self.grid.shape) and np.all(self.grid[x,y] == 0)
    
    def add(self, tetromino):
        new_board = Board(self.grid)
        new_board.grid[tetromino.coords()] = 1
        return new_board
        
    def __repr__(self):
        s = '   o' + '--' * self.grid.shape[0] + 'o\n'
        s += '\n'.join(["{:2d}".format(n) + ' |' + ''.join(['[]' if j else '  ' for j in i]) + '|' for n,i in enumerate(self.grid.T)])
        s += '\n   o' + '--' * self.grid.shape[0] + 'o'
        return s


class Tetromino:
    
    __tetro = {
        'T': [(0, 0), (-1,  0), ( 1,  0), ( 0, -1)],
        'J': [(0, 0), (-1,  0), ( 0, -1), ( 0, -2)],
        'L': [(0, 0), ( 1,  0), ( 0, -1), ( 0, -2)],
        'Z': [(0, 0), (-1,  0), ( 0, -1), ( 1, -1)],
        'S': [(0, 0), (-1, -1), ( 0, -1), ( 1,  0)],
        'I': [(0, 0), ( 0, -1), ( 0, -2), ( 0, -3)],
        'O': [(0, 0), ( 0, -1), (-1,  0), (-1, -1)],
    }
        
    @classmethod
    def create(cls, name, anchor=(0,0)):
        return Tetromino((anchor, cls.__tetro[name], name))
    
    def __init__(self, triplet):
        anchor, blocks, name = triplet
        self.anchor = np.array(anchor, dtype=int)
        self.blocks = np.array(blocks, dtype=int)
        self.name   = name
        
    def position(self):
        return self.blocks + self.anchor
    
    def coords(self):
        xy  = self.position()
        idx = (xy[:,0], xy[:,1])
        return idx
    
    def start(self):
        """Starting row of the tetromino, taking into account its height."""
        return -self.blocks[:,1].min()
    
    def place_at(self, x, y):
        return Tetromino(((x,y), self.blocks, self.name))
            
    def move_right(self):
        return Tetromino((self.anchor + ( 1,0), self.blocks, self.name))
    
    def move_left(self):
        return Tetromino((self.anchor + (-1,0), self.blocks, self.name))

    def move_down(self):
        return Tetromino((self.anchor + ( 0,1), self.blocks, self.name))

    def rotate_right(self):
        return Tetromino((self.anchor, self.blocks[:,[1,0]] * (-1,1), self.name))
    
    def rotate_left(self):
        return Tetromino((self.anchor, self.blocks[:,[1,0]] * (1,-1), self.name))
    
    def drop(self, board, column=None):
        if column is None:
            piece = self
        else:
            middle= board.columns() // 2
            piece = self.place_at(middle, 0)  # all tetrominos start at row 0 
            piece = move_to_column(piece, board, column)
        return push_down(piece, board)
        
    def action_for(self, landed):
        """Action that brings the tetromino 'self' closer to the tetromino 'landed' passed as input."""
        if landed is None: landed = self
        diff = landed.anchor[0] - self.anchor[0]
        move_left  = diff < 0
        move_right = diff > 0
        rotate_left  = np.all(landed.blocks == self.rotate_left().blocks)
        rotate_left |= np.all(landed.blocks == self.rotate_left().rotate_left().blocks)
        rotate_right = np.all(landed.blocks == self.rotate_right().blocks)
        rotate_right|= np.all(landed.blocks == self.rotate_right().rotate_right().blocks)
        if rotate_left:
            action = 3
        elif rotate_right:
            action = 4
        elif move_left:
            action = 1 
        elif move_right:
            action = 2
        else:  # drop down
            action = 5
        return action
        
    def __repr__(self):
        grid = np.zeros((7, 4))
        x = self.blocks[:,0] + grid.shape[0]//2
        y = self.blocks[:,1] + self.start()
        grid[x,y] = 1
        #grid = np.zeros((10, 20))
        #grid[self.coords()] = 1
        s = '   o' + '--' * grid.shape[0] + 'o\n'
        s += '\n'.join(["{:2d}".format(n) + ' |' + ''.join(['[]' if j else '  ' for j in i]) + '|' for n,i in enumerate(grid.T)])
        s += '\n   o' + '--' * grid.shape[0] + 'o'
        return s


def move_to_column(piece, board, column):
    while board.can_place(piece):
        delta = piece.anchor[0] - column
        if delta < 0:
            piece = piece.move_right() 
        elif delta > 0:
            piece = piece.move_left()
        else:
            return piece
    return None


def push_down(piece, board):
    if piece is None or not board.can_place(piece): 
        return None
    while True:
        down = piece.move_down()
        if board.can_place(down):
            piece = down
        else:
            return piece
