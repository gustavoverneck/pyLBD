# src/grid.py

import numpy as np
from src.setup import log
from src.cell import Cell

class Grid:
    def __init__(self, D, Q, dims):
        self.D = D  # Dimension
        self.Q = Q  # Number of velocities
        self.N = 9  # Number of populations (rho, T, ...)
        self.M = np.array(np.zeros(self.N) for i in range(self.Q))  # M matrix to transform from f to m
        log(f"Creating grid with {D} dimensions and {Q} velocities.")
        self.createGrid(D, Q, dims)

    
    def createGrid(self, D, Q, dims):
        if (D == 1):
            self.nx = dims[0]
            self.grid = np.array([Cell() for i in range(self.nx)])
        elif (D == 2):
            self.nx = dims[0]
            self.ny = dims[1]
            self.grid = np.array([[Cell()] for i in range(self.ny)] for i in range(self.nx))
        elif (D == 3):
            self.nx = dims[0]
            self.ny = dims[1]
            self.nz = dims[2]
            self.grid = np.array([[[Cell()] for i in range(self.nz)] for i in range(self.ny)] for i in range(self.nx))
        else:
            log("ValueError: The dimension must be between 1 and 3.")
            raise ValueError("The dimension must be between 1 and 3.")
        