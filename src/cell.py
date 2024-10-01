# src/cell.py

import numpy as np
from src.setup import log


class Cell:
    def __init__(self, D, Q, i=0, j=0, k=0, type=np.nan):
        self.f = np.array(np.zeros(Q))
        self.feq = np.array(np.zeros(Q))

        if D == 1:
            self.boundaries = np.zeros(2)
        elif D == 2:
            self.boundaries = np.array(np.array(np.zeros(3)) for i in range(3))
        elif D == 3:
            self.boundaries = np.array(np.array(np.array(np.zeros(3)) for i in range(3)) for j in range(3))
        else:
            log("ValueError: The dimension must be between 1 and 3.")
            raise ValueError("The dimension must be between 1 and 3.")
    
    def setType(self, type):
        self.type = type
    
    def getBoundaries(self):
        pass
    
    def __str__(self):
        return f"Cell type: {self.type}"