'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   19/06/2020
Name         :   sevcon_class.py
Description  :
* This file is for managing the SEVCON controller
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
class SEVCON_CLASS(devices_class.DEV_CLASS):
    __error      = functions.StatErr.notInitiated
    __TPDO1      = [0]*5     # TPDO1, target:id, id, target_iq, iq
    __TPDO2      = [0]*5     # TPDO2, batt_volt, batt_curr, line_contactor, capacitor_voltage
    __TPDO3      = [0]*5     # TPDO3, throtle value, target_torque, torque
    __TPDO4      = [0]*5     # TPDO4, Heatsink_temp
    __TPDO5      = [0]*5     # TPDO5, max_speed, velocity


#*******************************************************************************
#   Function name:  __init__
#   Descriptions:   Initialize SEVCON_CLASS
#*******************************************************************************
    def __init__(self,TPDO1,TPDO2,TPDO3,TPDO4,TPDO5):
        self.__TPDO1[0] = TPDO1
        self.__TPDO2[0] = TPDO2
        self.__TPDO3[0] = TPDO3
        self.__TPDO4[0] = TPDO4
        self.__TPDO5[0] = TPDO5
        devices_class.DEV_CLASS.__init__(self, __name__, TIME_LIM_PLOT,TIME_LIM_COMM)

#*******************************************************************************
#   Function name:  info
#   Descriptions:   Class for potting managemant
#*******************************************************************************
    def info(self):
        shoot.debug(" **********************************************************")
        shoot.debug("    " + __name__)
        shoot.debug(" **********************************************************")
        shoot.debug("    TPDO1: " + hex(self.__TPDO1[0]))
        shoot.debug("     - Id:" + str(self.__TPDO1[2]) + " // target Id:"  + str(self.__TPDO1[1]))
        shoot.debug("     - Iq:" + str(self.__TPDO1[4]) + " // target Iq:"  + str(self.__TPDO1[3]))
        shoot.debug("    TPDO2: " + hex(self.__TPDO2[0]))
        shoot.debug("     - Battery (V): " + str(self.__TPDO2[1]) + " // Capacitor (V):" + str(self.__TPDO2[4]))
        shoot.debug("     - Current (A): " + str(self.__TPDO2[2]))
        shoot.debug("     - Contactor (mV): " + str(self.__TPDO2[3]))
        shoot.debug("    TPDO3: " + hex(self.__TPDO3[0]))
        shoot.debug("     - Torque: " + str(self.__TPDO3[3]) + " // Target Torque" + str(self.__TPDO3[2]))
        shoot.debug("     - Throttle: " + str(self.__TPDO3[1]))
        shoot.debug("    TPDO4: " + hex(self.__TPDO4[0]))
        shoot.debug("     - Heatsink (ºC): " + str(self.__TPDO4[1]))
        shoot.debug("    TPDO5: " + hex(self.__TPDO5[0]))
        shoot.debug("     - Speed (rad/s):" + str(self.__TPDO5[2]) + " // Max Speed (rad/s): " + str(self.__TPDO5[1]))

#*******************************************************************************
#   Function name:  parse
#   Descriptions:   Class for analizing a received CAN message
#*******************************************************************************
    def parse(self, id, msg, t):
        if id == self.__TPDO1[0]:
            self.__TPDO1[1] = ((msg[1]<<8)+msg[0])*0.0625
            self.__TPDO1[2] = ((msg[3]<<8)+msg[2])*0.0625
            self.__TPDO1[3] = ((msg[5]<<8)+msg[4])*0.0625
            self.__TPDO1[4] = ((msg[7]<<8)+msg[6])*0.0625
        elif id == self.__TPDO2[0]:
            self.__TPDO2[1] = ((msg[1]<<8)+msg[0])*0.0625
            self.__TPDO2[2] = ((msg[3]<<8)+msg[2])*0.0625
            self.__TPDO2[3] = ((msg[5]<<8)+msg[4])*1.0
            self.__TPDO2[4] = ((msg[7]<<8)+msg[6])*0.0625
        elif id == self.__TPDO3[0]:
            self.__TPDO3[1] = ((msg[1]<<8)+msg[0])/32767
            self.__TPDO3[2] = ((msg[3]<<8)+msg[2])/100
            self.__TPDO3[3] = ((msg[1]<<8)+msg[0])*0.0625
        elif id == self.__TPDO4[0]:
            self.__TPDO4[1] = msg[0]
        elif id == self.__TPDO5[0]:
            self.__TPDO5[1] = (msg[3]<<24)+(msg[2]<<16)+(msg[1]<<8)+msg[0]
            self.__TPDO5[2] = (msg[7]<<24)+(msg[6]<<16)+(msg[5]<<8)+msg[4]

# -------------------- END -----------------------------------------------------
