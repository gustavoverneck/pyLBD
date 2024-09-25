# src/grid.py

import numpy as np
from src.setup import log

class Grid:
    def __init__(self, D, Q, nx=0, ny=0, nz=0):
        self.D = D  # Dimension
        self.Q = Q  # Number of velocities
        self.N = 9  # Number of populations (rho, T, ...)
        self.createGrid(D, Q, nx, ny, nz)
        log(f"Creating grid with {D} dimensions and {Q} velocities.")

    
    def createGrid(self, D, Q, nx, ny, nz):
        if (D == 1):
            self.nx = nx
            self.grid = np.array([np.zeros(self.N)] for i in range(self.nx))
        elif (D == 2):
            self.nx = nx
            self.ny = ny
            self.grid = np.array([[np.zeros(self.N)] for i in range(self.ny)] for i in range(self.nx))
        elif (D == 3):
            self.nx = nx
            self.ny = ny
            self.nz = nz
            self.grid = np.array([[[np.zeros(self.N)] for i in range(self.nz)] for i in range(self.ny)] for i in range(self.nx))
        else:
            log("ValueError: The dimension must be between 1 and 3.")
            raise ValueError("The dimension must be between 1 and 3.")
    
    

        
    