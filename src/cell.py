# src/cell.py

import numpy as np
from src.setup import log


class Cell:
    def __init__(self, type, Q):
        self.f = np.array(np.zeros(Q))
        self.feq = np.array(np.zeros(Q))
        # type: 0=fluid, 1=wall, 2=interface
    
    def __str__(self):
        return f"Cell type: {self.type}"

    def getBoundaries(self):
        pass