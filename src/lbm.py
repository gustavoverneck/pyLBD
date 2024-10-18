# src/lbm.py

import numpy as np
from src.setup import log
from src.grid import Grid
import matplotlib.pyplot as plt

class LBM:
    def __init__(self, params) -> None:
        self.D = params["D"]
        self.Q = params["Q"]
        self.getDimensions(params)
        self.createGrid()

    def getDimensions(self, params):
        if (self.D == 2):
            self.nx = params["nx"]
            self.ny = params["ny"]
            self.dims = (self.nx, self.ny, 1)
        else:
            log("ValueError: The dimension must be 2.")
            raise ValueError("The dimension must be 2.")

    def createGrid(self):       
        self.grid = Grid(self.D, self.Q, self.dims)

    def loadObject(self, vertices):
        self.grid.addVertices(vertices)

    def streaming(self):
        pass

    def collision(self):
        pass

    def equilibrium(self):
        pass

    def updateBoundaries(self):
        log("Updating grid boundaries.")
        self.grid.getBoundaries()

    def printGrid(self):
        from matplotlib.colors import ListedColormap
        from matplotlib.lines import Line2D

        log("Plotting LBM grid structure.")

        cmap = ListedColormap(["oldlace", "black", "lightskyblue", "coral"])

        colors = np.zeros_like(self.grid.grid)
        colors_dict = {"fluid": 0, "wall": 1, "in": 2, "out": 3}
        for i in range(self.nx):
            for j in range(self.ny):
                colors[j][i] = colors_dict[self.grid.grid[i][j].type]


        plt.imshow(colors.astype(float), cmap=cmap, interpolation='nearest')
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Fluid', markersize=10, markerfacecolor='oldlace'),
            Line2D([0], [0], marker='o', color='w', label='Wall', markersize=10, markerfacecolor='black'),
            Line2D([0], [0], marker='o', color='w', label='In', markersize=10, markerfacecolor='lightskyblue'),
            Line2D([0], [0], marker='o', color='w', label='Out', markersize=10, markerfacecolor='coral')
        ]

        plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.25, 1), borderaxespad=0.)
        plt.title('LBM Grid')
        plt.xlabel(" ")
        plt.ylabel(" ")
        plt.xticks([])
        plt.yticks([])
        plt.savefig("data/raw_grid.svg", dpi=600)
        #plt.show()
