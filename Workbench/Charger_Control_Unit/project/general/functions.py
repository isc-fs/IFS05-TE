'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   16/06/2020
Name         :   functions.py
Description  :
* This file defines function and variables for general purposes
-----------------------------------------------------------------------------
'''

# Libraries
import os
import time
from enum import Enum,auto

name_route      = 'files/'
name_boot_file  = 'log_boot.txt'

route_boot_file  = name_route + name_boot_file

start_time = time.time()

#*******************************************************************************
#   Function name:  StatusComunication
#   Descriptions:   Class for the status of the
#*******************************************************************************
class StatComm(Enum):
    connected       = auto()
    disconnected    = auto()

#*******************************************************************************
#   Function name:  StatusError
#   Descriptions:   Class for managing all the possible errors
#*******************************************************************************
class StatErr(Enum):
    allOK           = auto()    # Works fine
    notInitiated    = auto()    # Hasnt been initialized yet
    errorMaxBattV   = auto()    # Maximum voltage of the battery exceeded
    errorMinBatV    = auto()    # Minimum voltage of the battery exceeded
    errorCellV   = auto()    # Maximum Voltage of a single cell exceeded
    errorBattT   = auto()    # Minimum Temperature of a single cell exceeded

#*******************************************************************************
#   Function name:  createLogFile
#   Descriptions:   Function for saving th eboot log into a file
#*******************************************************************************
def createBootFile():
    os.system('dmesg>' + route_boot_file)

# Main execution
if __name__ == "__main__":
    pass
# -------------------- END -----------------------------------------------------
