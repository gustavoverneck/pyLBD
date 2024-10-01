# src/lbm.py

import numpy as np
from src.setup import log
from src.grid import Grid

class LBM:
    def __init__(self, params) -> None:
        self.D = params["D"]
        self.Q = params["Q"]
        self.getDimensions(params)
        self.createGrid()

    def getDimensions(self, params):
        if (self.D == 1):
            self.nx = params["nx"]
            self.dims = (self.nx, 1, 1)
        elif (self.D == 2):
            self.nx = params["nx"]
            self.ny = params["ny"]
            self.dims = (self.nx, self.ny, 1)
        elif (self.D == 3):
            self.nx = params["nx"]
            self.ny = params["ny"]
            self.nz = params["nz"]
            self.dims = (self.nx, self.ny, self.nz)
        else:
            log("ValueError: The dimension must be between 1 and 3.")
            raise ValueError("The dimension must be between 1 and 3.")

    def createGrid(self):       
        self.grid = Grid(self.D, self.Q, self.dims)

    def streaming(self):
        pass

    def collision(self):
        pass

    def equilibrium(self):
        pass
