'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   18/06/2020
Name         :   devices_class.py
Description  :
* This file is for managing the BMS modules
-----------------------------------------------------------------------------
'''

import time
from general import functions

# Local libraries
from classes import debug_class

# Variables
shoot = debug_class.DEBUG_CLASS(__name__).log_file # Logging variable

class DEV_CLASS:
    communication = functions.StatComm.disconnected
    __class_name        = __name__
    __TIME_LIM_PLOT     = 0
    __time_lim_plotted  = 0
    __TIME_LIM_COMM     = 0
    __time_lim_received = 0

#*******************************************************************************
#   Function name:  __init__
#   Descriptions:   Initialize class
#*******************************************************************************
    def __init__(self, name, limplot, limcomm, id=0, lag=0):
        self.__TIME_LIM_PLOT      = limplot
        self.__time_lim_plotted   = time.time() + lag
        self.__TIME_LIM_COMM      = limcomm
        self.__time_lim_received  = limcomm + time.time() + lag
        self.__class_name         = name
        self.identifier           = id

#*******************************************************************************
#   Function name:  plotting
#   Descriptions:   Function for ploting the data at a certain time
#*******************************************************************************
    def plotting(self,t):
        if self.__TIME_LIM_PLOT:
            if t>self.__time_lim_plotted:
                self.__time_lim_plotted += self.__TIME_LIM_PLOT
                self.info()

#*******************************************************************************
#   Function name:  communicating
#   Descriptions:   Function for checking if the device is obtaining the required data
#*******************************************************************************
    def communicating(self,t):
        if self.__TIME_LIM_COMM:
            if t>self.__time_lim_received:
                if self.communication == functions.StatComm.connected:
                    shoot.error("Device '" + self.__class_name + "' with CAN_ID = [" + hex(self.identifier) + "] is disconnected")
                self.communication = functions.StatComm.disconnected

#*******************************************************************************
#   Function name:  receivedMesage
#   Descriptions:   Function for incrementing the time limit
#*******************************************************************************
    def receivedMesage(self,t):
        if self.__TIME_LIM_COMM:
            self.__time_lim_received = t + self.__TIME_LIM_COMM
            if self.communication is not functions.StatComm.connected:
                shoot.info("Device '" + self.__class_name + "' with CAN_ID = [" + hex(self.identifier) + "] is connected")
            self.communication = functions.StatComm.connected

# -------------------- END -----------------------------------------------------
