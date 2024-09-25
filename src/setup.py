# src/setup.py

import os
import matplotlib.pyplot as plt
import numpy as np
import time

def log(message):
    global logfile
    current_time = time.time()
    local_time = time.localtime(current_time)
    milliseconds = int((current_time - int(current_time)) * 1000)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time) + f".{milliseconds:03d}"
    message = current_time + " - " + message + "\n"
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
    log(f"pyLBM: {log_filename} Log")
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
