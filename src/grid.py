# src/grid.py
import numpy as np


class Grid:
    def __init__(self, model, D, Q, nx=0, ny=0, nz=0) -> None:
        self.D = D
        self.Q = Q
        if (D >= 1 and D <= 3):
            self.nx = nx
            if (D >= 2):
                self.ny = ny
                if (D == 3):
                    self.nz = nz
        else:
            raise ValueError("The dimension must be between 1 and 3.")
        
    def createGrid(self):
        if (self.D == 1):
            self.grid = np.zeros((self.nx, self.Q))
        elif (self.D == 2):
            self.grid = np.zeros((self.nx, self.ny, self.Q))
        elif (self.D == 3):
            self.grid = np.zeros((self.nx, self.ny, self.nz, self.Q))
        else:
            raise ValueError("The dimension must be between 1 and 3.")

    