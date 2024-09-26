# app.py

# Para introduzir arquivos .stl do blender:
# pip install numpy-stl


from src.setup import isOk, readParams
from src.lbm import LBM


if __name__ == '__main__':
    if isOk(): # This will create the log file and the folders if they don't exist.
        inputParams = readParams(file='input/params.in') # This will read the parameters from the file 'params.in' and store them.
        lbm = LBM(params=inputParams)

        