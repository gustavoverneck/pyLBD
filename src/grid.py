# src/grid.py

import numpy as np
from src.setup import log
from src.cell import Cell


class Grid:
    def __init__(self, D, Q, dims, N=9):
        """         
        Initializes the grid with the given dimensions and velocities.
        Args:
            D (int): Dimension of the grid.
            Q (int): Number of velocities.
            dims (tuple): Dimensions of the grid.
        Attributes:
            D (int): Dimension of the grid.
            Q (int): Number of velocities.
            N (int): Number of populations (rho, T, ...).
            M (np.ndarray): Matrix to transform from velocity space to momentum space.
        Returns:
            None
        """
        
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
            for i in range(self.nx):
                self.grid.append([])
                for j in range(self.ny):
                    self.grid[i].append(Cell(D=D, Q=Q, i=i, j=j, type='fluid'))
            self.grid = np.array(self.grid)
        else:
            log("ValueError: The dimension must be between 2.")
            raise ValueError("The dimension must be between 2.")

    def addVertices(self, vertices):
        """
        Adds the vertices to the grid.
        
        - `vertices`: Vértices ajustados para caber no grid (array Nx3).
        - `grid`: Array `numpy` que representa o grid.
        - `grid_shape`: Tamanho do grid (nx, ny, nz).
        """
        log("Inserting .stl object into LBM grid.")

        for vertex in vertices:
            # Para cada vértice, arredondamos para encontrar a posição no grid
            grid_x, grid_y = np.round(vertex).astype(int)

            # Verifica se o vértice está dentro dos limites do grid
            if 0 <= grid_x < self.nx and 0 <= grid_y < self.ny:
                # Substitui o valor na posição correta (aplica um valor arbitrário, como 1, para marcar a presença do vértice)
                if self.D == 2:  # Caso 2D
                    self.grid[grid_x][grid_y].setType("wall")
                else:  # Caso 3D
                    raise ValueError("Dimension must be 2!")
                    # self.grid[grid_x][grid_y][grid_z].setType("wall")
            pass
    
    def setFluid(self, i=0, j=0):
        '''
        Set the cell as fluid.
        '''
        self.grid[i][j].setType("fluid")
        pass

    def setWall(self, i=0, j=0):
        '''
        Set the cell as wall.
        '''
        self.grid[i][j].setType("wall")
        pass
    
    def setInflow(self, i=0, j=0):
        '''
        Set the cell as inflow.
        '''
        self.grid[i][j].setType("in")
        pass
    
    def setOutflow(self, i=0, j=0):
        '''
        Set the cell as outflow.
        '''
        self.grid[i][j].setType("out")
        pass

    def getBoundaries(self):
        '''
        Self-analizes the grid and set the boundaries of each cell.
        '''
        for i in range(self.nx):
            for j in range(self.ny):
                if self.grid[i][j] != "wall":
                    cell_bounds = []
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < self.nx and 0 <= nj < self.ny:
                                pass
                                #print(self.grid[i][j].boundaries[di][dj])
                                #self.grid[i][j].boundaries[di+1][dj+1].append(self.grid[ni][nj].type)
                            else:
                                cell_bounds.append(None)  # Out of bounds
        

    def __str__(self):
        return f"Grid dimensions: {self.nx}x{self.ny}x{self.nz}"