
'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   28/07/2021
Name         :   charger_class.py
Description  :
* This file is for managing the charger class
-----------------------------------------------------------------------------
'''
# Importing the libraries
import time
import asyncio
import can
from general import functions
from classes import can_class,debug_class,devices_class

# Variables
var = debug_class.DEBUG_CLASS(__name__)
var.changeLevelToDebug()
shoot = var.log_file
TIME_LIM_PLOT = 2
TIME_LIM_COMM = 5

class CHARGER_CLASS(devices_class.DEV_CLASS):
    __TIME_LIM_SEND = 0.45;   # Interval to send mesage in seconds
    __error         = functions.StatErr.notInitiated

    meas_V          = 0
    meas_I          = 0
    hardw_fail      = 0
    charger_temp    = 0
    input_volt      = 0
    start_state     = 0
    comm_state      = 0

    __data = [0,0,0,0,0]

    BMS = [[0 for x in range(12)] for y in range(10)]
    BMS_id = [0x12C,0x12C+10,0x12C+20,0x12C+30,0x12C+40,0x12C+50,0x12C+60,0x12C+70,0x12C+80,0x12C+90]

# ******************************************************************************
#   Function name:  __init__
#   Descriptions:   Function for initializing the class
# ******************************************************************************
    def __init__(self,id_send,id_recv,max_v,max_i,min_i,lag=0):
        self._ID_CAN_send = id_send
        self._ID_CAN_recv = id_recv
        self._LIMIT_MAX_V = max_v;
        self._LIMIT_MAX_I = max_i;
        self._LIMIT_MIN_I = min_i;

        # Voltage
        self.__data[0] = (max_v*10 >> 8) & 0xFF
        self.__data[1] = max_v*10 & 0xFF
        # Current
        self.__data[2] = (max_i*10 >> 8) & 0xFF
        self.__data[3] = max_i*10 & 0xFF
        # Mode
        self.__data[4] = 1 #// 1 for No charging, 0 is for charging
        self.__message = can.Message(arbitration_id=self._ID_CAN_send,data=self.__data)

        self.__LAG = lag
        devices_class.DEV_CLASS.__init__(self, __name__, \
            TIME_LIM_PLOT,TIME_LIM_COMM,self._ID_CAN_send,lag)

# ******************************************************************************
#   Function name:  query
#   Descriptions:   Function to check if i need to send a mesage new mesage and the received mesajes interval are within the limits
# ******************************************************************************
    def query(self,t):
        self.plotting(t)
        self.communicating(t)

# ******************************************************************************
#   Function name:  __init__
#   Descriptions:   Function for initializing the class
# ******************************************************************************
    async def routine(self,can_bus):
        await asyncio.sleep(self.__LAG)
        if self.__TIME_LIM_SEND:
            while True:
                can_bus.sendMessage(self.__message)
                mess = [0,0]

                mess[0] = (int(self.meas_V) >> 8) & 0xFF;
                mess[1] = int(self.meas_V) & 0xFF;
                var = can.Message(arbitration_id=0x100,data=mess)
                can_bus.sendMessage(var)
                await asyncio.sleep(self.__TIME_LIM_SEND)

#*******************************************************************************
#   Function name:  info
#   Descriptions:   Class for potting managemant
#*******************************************************************************
    def info(self):
        shoot.debug("")
        shoot.debug(" *********************************************************")
        shoot.debug("    " + __name__ + " - ID_send " + hex(self._ID_CAN_send) + " - ID_recv " + hex(self._ID_CAN_recv))
        shoot.debug(" **********************************************************")
        shoot.debug("   - Status: " + str(self.communication))
        shoot.debug("   - V (volts) = " + str(self.meas_V) + "   || MAX V (volts) = " + str(self._LIMIT_MAX_V))
        shoot.debug("   - I (Amps)  = " + str(self.meas_I) + "   || MAX I (Amps)  = " + str(self._LIMIT_MAX_I))
        shoot.debug("   - 1. Hardware Failure = " + str(self.hardw_fail) + " (0: Normal. || 1: Hardware Failure)")
        shoot.debug("   - 2. Charger Temp     = " + str(self.charger_temp) + " (0: Normal. || 1: Over temperature protection)")
        shoot.debug("   - 3. Input Volts      = " + str(self.input_volt) + " (0: Input voltage is normal. || 1. Input voltage is wrong, the charger will stop working.)")
        shoot.debug("   - 4. Start State      = " + str(self.start_state) + " (0: Charger detects battery voltage and starts charging. || 1: Charger stays turned off (to prevent reverse polarity).)")
        shoot.debug("   - 5. Communications   = " + str(self.comm_state) + " (0: Communication is normal. || 1: Communication receive time-out.)")
        shoot.debug(" **********************************************************")

        for h in range(0,10):
            text = "   - BMS " + str(h) + ": ["
            for w in range(0,11):
                text +=  str(self.BMS[h][w]) + ", "
            text += str(self.BMS[h][w+1]) + "]"
            shoot.debug(text)
        shoot.debug("")

#*******************************************************************************
#   Function name:           parse
#   Descriptions:            Function for analysing the received CAN message
#*******************************************************************************
    def parse(self, msg,t): # Preguntar a Luis por self
        buf = msg.data
        if (msg.arbitration_id==self._ID_CAN_recv):
            self.receivedMesage(t)
            self. meas_V = ((buf[0]<<8) + buf[1])/10
            self. meas_I = ((buf[2]<<8) + buf[3])/10
            self.hardw_fail     = (buf[4]>>0) & 0x01
            self.charger_temp   = (buf[4]>>1) & 0x01
            self.input_volt     = (buf[4]>>2) & 0x01
            self.start_state    = (buf[4]>>3) & 0x01
            self.comm_state     = (buf[4]>>4) & 0x01
            return True
        elif(msg.arbitration_id==0x20 and msg.dlc>0):
            if (msg.data[0]==0):
                self.startCharging();
                shoot.debug("CARGAAAAAA")
            else:
                self.stopCharging()
                shoot.debug("NO CARGES")
            return True

        else:
            for i in range(0,10):
                if (msg.arbitration_id>self.BMS_id[i] and msg.arbitration_id<self.BMS_id[i]+4):
                    m = msg.arbitration_id%self.BMS_id[i]
                    pos = 0
                    if(m>0 and m<5):
                        if(m<4):
                            for x in range(0,4):
                                pos = (m-1)*4 + x
                                self.BMS[i][pos] = (buf[2*x] << 8) + buf[2*x + 1]
                    return True

            return False

#*******************************************************************************
#   Function name:           stopCharging
#   Descriptions:            Function for stoping the charge
#*******************************************************************************
    def stopCharging(self):
        self.__message.data[4] = 1 #// 1 for No charging, 0 is for charging


#*******************************************************************************
#   Function name:           startCharging
#   Descriptions:            Function for starting the charge
#*******************************************************************************
    def startCharging(self):
        self.__message.data[4] = 0 #// 1 for No charging, 0 is for charging

# -------------------- END -----------------------------------------------------
