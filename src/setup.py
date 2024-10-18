# src/setup.py

import os
import matplotlib.pyplot as plt
import numpy as np
import time
from watermark import watermark


author = "Gustavo A. Verneck\n\nRequirements: "
watermark_output = watermark(iversions=True, author=author, globals_=globals())

print(watermark_output)

def log(message):
    global logfile
    current_time = time.time()
    local_time = time.localtime(current_time)
    milliseconds = int((current_time - int(current_time)) * 1000)
    current_time = time.strftime("[%Y-%m-%d] [%H:%M:%S", local_time) + f".{milliseconds:03d}]"
    message = current_time + " " + message + "\n"
    logfile.write(message)
    print(message)

def isOk():
    global logfile
    log_created = 0
    if not os.path.exists('log'):
        os.makedirs('log')
        log_created = 1
    
    # Log
    log_filename = time.strftime("%Y-%m-%d-%H_%M_%S")
    logfile = open(f"log/{log_filename}.txt", "w+")
    log(f"pyLBM: {log_filename} Log initialized.")
    log("Starting application.")
    if log_created:
        log("Log folder doesn't exists. Creating 'log' folder.")
    else:
        log("Log folder already exists. Doing nothing.")

    if not os.path.exists('data'):
        log("Data folder doesn't exists. Creating 'data' folder.")
        os.makedirs('data')
    else:
        log("Data folder already exists. Doing nothing.")

    if not os.path.exists('input'):
        log("Input folder already exists. Doing nothing.")
        os.makedirs('input')
    else:
        log("Input folder already exists. Doing nothing.")
    
    return True


def readParams(file="input/params.in"):
    nx = np.nan; ny = np.nan; nz = np.nan; D = np.nan; Q = np.nan
    try:
        with open(file, 'r') as f:
            f.close()
    except FileNotFoundError:
        log(f"File {file} not found.")
        log(f"Creatiung '{file}' template file.")
        with open(file, 'w') as f:
            f.write("nx=100\nny=100\nnz=1\nD=2\nQ=9\n")
            f.close()

    with open(file, 'r') as f:
        for line in f.readlines():
            a = line.split("=")
            match a[0]:
                case "nx":
                    nx = int(a[1])
                case "ny":
                    ny = int(a[1])
                case "nz":
                    nz = int(a[1])
                case "D":
                    D = int(a[1])
                case "Q":
                    Q = int(a[1])
                case _:
                    pass
        f.close()
        inputData = {}
        
        if not np.isnan(D):
            inputData["D"] = D
        if not np.isnan(Q):
            inputData["Q"] = Q
        if not np.isnan(nx):
            inputData["nx"] = nx
        if not np.isnan(ny):
            inputData["ny"] = ny
        if not np.isnan(nz):
            inputData["nz"] = nz
                
        return inputData
            