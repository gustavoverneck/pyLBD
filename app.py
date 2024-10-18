# app.py

# Para introduzir arquivos .stl do blender:
# pip install numpy-stl


from src.setup import isOk, readParams
from src.lbm import LBM
from src.stl_import import load_stl_file, scale_and_dimensionalize


stl_obj_dir = 'input/obj.stl'


if __name__ == '__main__':
    if isOk(): # This will create the log file and the folders if they don't exist.
        inputParams = readParams(file='input/params.in') # This will read the parameters from the file 'params.in' and store them.
        nx = inputParams['nx']; ny = inputParams['ny']; D = inputParams['D']; Q = inputParams['Q']
        lbm = LBM(params=inputParams)
        
        # Set initial parameters
        for j in range(ny):
            lbm.grid.setInflow(i=0, j=j)
            lbm.grid.setOutflow(i=nx-1, j=j)
        for i in range(nx):
           lbm.grid.setWall(i=i, j=0)
           lbm.grid.setWall(i=i, j=ny-1)
        
        vertices = load_stl_file(stl_obj_dir)
        vertices = scale_and_dimensionalize(vertices, grid_shape=lbm.dims, target_dimension=2, position=(0,0,0), scale=0.5, rotation_angle=45)
        
        lbm.loadObject(vertices)
        lbm.updateBoundaries()
        lbm.printGrid()
