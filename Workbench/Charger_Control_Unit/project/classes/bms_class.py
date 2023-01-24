'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   17/06/2020
Name         :   bmd_class.py
Description  :
* This file is for managing the BMS modules
-----------------------------------------------------------------------------
'''

# Libraries
import time


# Local libraries
from classes import debug_class,devices_class
from general import functions

# Variables
shoot = debug_class.DEBUG_CLASS(__name__).log_file # Logging variable

TIME_LIM_PLOT = 5.0
TIME_LIM_COMM = 1.0

#*******************************************************************************
#   Function name:  BMS_CLASS
#   Descriptions:   Class for BMS managemant
#*******************************************************************************
class BMS_CLASS(devices_class.DEV_CLASS):
    __CANID         = 0
    __error         = functions.StatErr.notInitiated
    __lim_maxV      = 0
    __lim_minV      = 0
    __lim_maxT      = 0
    __numCells      = 12
    __shunt         = 0
    __maxV          = 0
    __minV          = 0
    __maxT          = 0
    __cellVoltagemV = [0]*12
    __temperature   = [0]*2
    __mess_shunt    = [0]*2
    __max_flag          = 3
    __flag_error_volt   = 0
    __flag_error_temp   = 0
    __voltageMatrix = {1:[[0]*12],
                        2:[[0]*12],
                        3:[[0]*12],
                        4:[[0]*12],
                        5:[[0]*12]}
    __tempMatrix =     {1:[[0]*12],
                        2:[[0]*12],
                        3:[[0]*12],
                        4:[[0]*12],
                        5:[[0]*12]}

    __voltageErrorMatrix = {1:[[0]*12],
                            2:[[0]*12],
                            3:[[0]*12],
                            4:[[0]*12],
                            5:[[0]*12]}

    __tempErrorMatrix =     {1:[[0]*12],
                            2:[[0]*12],
                            3:[[0]*12],
                            4:[[0]*12],
                            5:[[0]*12]}





#*******************************************************************************
#   Function name:  __init__
#   Descriptions:   Initialize BMS class
#*******************************************************************************
    def __init__(self,id, lim_maxV, lim_minV, lim_maxT, numCells, shunt):
        self.__CANID    = id
        self.__lim_maxV = lim_maxV
        self.__lim_minV = lim_minV
        self.__lim_maxT = lim_maxT
        self.__numCells = numCells
        self.__shunt    = shunt
        self.__mess_shunt[1] = shunt & 0xFF
        self.__mess_shunt[0] = (shunt >> 8) & 0xFF
        devices_class.DEV_CLASS.__init__(self, __name__, TIME_LIM_PLOT,TIME_LIM_COMM)

#*******************************************************************************
#   Function name:  info
#   Descriptions:   Class for potting managemant
#*******************************************************************************
    def info(self):
        shoot.debug(" **********************************************************")
        shoot.debug("    " + __name__ + " - ID " + hex(self.__CANID))
        shoot.debug(" **********************************************************")
        shoot.debug("  - Link : " + str(self.communication))
        shoot.debug("  - Err  : " + str(self.__error))
        shoot.debug("  - Max V (mV)")
        shoot.debug("       Data: " + str(self.__maxV) + " || Lim: " + str(self.__lim_maxV))
        shoot.debug("  - Min V (mV)")
        shoot.debug("       Data: " + str(self.__minV) + " || Lim: " + str(self.__lim_minV))
        shoot.debug("  - Max T (ºC)")
        shoot.debug("       Data: " + str(self.__maxT) + " || Lim: " + str(self.__lim_maxT))
        shoot.debug(" ------------------------------------")
        text      = "  - Cells(mV) : [ "
        for x in self.__cellVoltagemV:
            text = text + str(x) + " "
        text = text + "]"
        shoot.debug(text)
        text      = "  - Temp(ºC)  : [ "
        for x in self.__temperature:
            text = text + str(x) + " "
        text = text + "]\n\n"
        shoot.debug(text)

#*******************************************************************************
#   Function name:  parse
#   Descriptions:   Class for analizing a received CAN message
#*******************************************************************************
    def parse(self, id, msg, t):
        if id>self.__CANID and id<self.__CANID+6: ##+6 o +18?
            m = id%self.__CANID
            self.receivedMesage(t)
            can = self.__CANID//100
            if m<4:
                for x in range(4): # x is the number of the correspondient cell
                    pos = (m-1)*4+x
                    v =  ((msg[2*x]<<8) + msg[2*x+1])
                    self.__cellVoltagemV[pos] = v
                    self.__voltageMatrix[can][pos] = v
                    if v>self.__lim_maxV and v<self.__lim_minV and pos<self.__numCells:
                        self.__flag_error_volt += 1
                        self.__voltageErrorMatrix[can][pos] = 1
                        if self.__flag_error_volt > self.__max_flag: self.__error = functions.StatErr.errorMaxCellV
                    else: self.__flag_error_volt = 0
            else:
                for x in range(2): # we read 2 temperatures
                    temp = msg[x]-40
                    self.__temperature[x] = temp
                    self.__tempMatrix[can][pos] = v
                    if temp>self.__lim_maxT:
                        self.__flag_error_temp += 1
                        self.__tempErrorMatrix[can][pos] = 1
                        if self.__flag_error_temp > self.__max_flag: self.__error = functions.StatErr.errorBattT
                    else: self.__flag_error_temp = 0
            return True
        else: return False

    def getMatrixes(self):
        ret = [self.__tempMatrix, self.__voltageMatrix, self.__tempErrorMatrix, self.__voltageErrorMatrix]
        return ret
    
    def getNumCells(self):
        return self.__numCells

# -------------------- END -----------------------------------------------------
