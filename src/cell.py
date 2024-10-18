# src/cell.py

import numpy as np
from src.setup import log

class Cell:
    def __init__(self, D, Q, i=0, j=0, type=np.nan):
        self.f = np.array(np.zeros(Q))
        self.feq = np.array(np.zeros(Q))
        self.type = type

        if D == 2 and Q == 9:
            self.boundaries = np.array(np.array(np.zeros(3)) for i in range(3))
        else:
            log("ValueError: The dimension must be 2 and velocities must be 9.")
            raise ValueError("The dimension must be 2 and velocities must be 9.")
        pass
        
    
    def setType(self, type):
        self.type = type
    
    def getBoundaries(self):
        pass
    
    def __str__(self):
        return self.type