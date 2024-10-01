# src/grid.py

import numpy as np
from src.setup import log
from src.cell import Cell
from src.stl_import import load_stl_file, scale_and_dimensionalize


class Grid:
    def __init__(self, D, Q, dims):
        self.D = D  # Dimension
        self.Q = Q  # Number of velocities
        self.N = 9  # Number of populations (rho, T, ...)
        self.M = np.array(np.zeros(self.N) for i in range(self.Q))  # M matrix to transform from f to m (velocity space to momentum space)
        log(f"Creating grid with {D} dimensions and {Q} velocities.")
        self.createGrid(D, Q, dims)

    
    def createGrid(self, D, Q, dims):
        self.grid = []
        if (self.D >= 1 and self.D <= 3):
            self.nx = dims[0]
            self.ny = dims[1]
            self.nz = dims[2]
            for i in range(self.nx):
                self.grid.append([])
                for j in range(self.ny):
                    self.grid[i].append([])
                    for k in range(self.nz):
                        self.grid[i][j].append(Cell(D=D, Q=Q, i=i, j=j, k=k, type='fluid'))
            self.grid = np.array(self.grid)
        else:
            log("ValueError: The dimension must be between 1 and 3.")
            raise ValueError("The dimension must be between 1 and 3.")
    
    def addVertices(self, vertices):
        """
        Adds the vertices to the grid.
        
        - `vertices`: Vértices ajustados para caber no grid (array Nx3).
        - `grid`: Array `numpy` que representa o grid.
        - `grid_shape`: Tamanho do grid (nx, ny, nz).
        """
        for vertex in vertices:
            # Para cada vértice, arredondamos para encontrar a posição no grid
            grid_x, grid_y, grid_z = np.round(vertex).astype(int)

            # Verifica se o vértice está dentro dos limites do grid
            if 0 <= grid_x < self.nx and 0 <= grid_y < self.ny and (self.nz == 1 or 0 <= grid_z < self.nz):
                # Substitui o valor na posição correta (aplica um valor arbitrário, como 1, para marcar a presença do vértice)
                if self.nz == 1:  # Caso 2D
                    self.grid[grid_x][grid_y][0].setType("wall")
                else:  # Caso 3D
                    self.grid[grid_x][grid_y][grid_z].setType("wall")
            pass
    
    def setFluid(self, i=0, j=0, k=0):
        '''
        Set the cell as fluid.
        '''
        self.grid[i][j][k].setType("fluid")
        pass

    def setWall(self, i=0, j=0, k=0):
        '''
        Set the cell as wall.
        '''
        self.grid[i][j][k].setType("wall")
        pass
    
    def setInflow(self, i=0, j=0, k=0):
        '''
        Set the cell as inflow.
        '''
        self.grid[i][j][k].setType("in")
        pass
    
    def setOutflow(self, i=0, j=0, k=0):
        '''
        Set the cell as outflow.
        '''
        self.grid[i][j][k].setType("out")
        pass

