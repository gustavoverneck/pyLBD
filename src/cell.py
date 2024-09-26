# src/cell.py

import numpy as np
from src.setup import log


class Cell:
    def __init__(self, type, Q):
        pass
        # type: 0=fluid, 1=wall, 2=interface
    
    def __str__(self):
        return f"Cell type: {self.type}"