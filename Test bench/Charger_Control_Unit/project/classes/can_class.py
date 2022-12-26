
'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   28/07/2021
Name         :   can_class.py
Description  :
* This file is for managin the CAN ports
-----------------------------------------------------------------------------
'''

'''
* Add the next lines to the config.txt FILE (sudo nano /boot/config.txt)
dtparam=spi=on
dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25
dtoverlay=spi0-hw-cs
dtoverlay=mcp2515-can1,oscillator=8000000,interrupt=24
dtoverlay=spi0-hw-cs
'''

# Libraries
import os
import subprocess
import sys
import time
import can
import asyncio

from classes import debug_class
from general import functions

# Variables
var = debug_class.DEBUG_CLASS(__name__)
#var.changeLevelToDebug()
shoot = var.log_file

queue_max  = 35
queue_read = 0
queue_end  = 0
queue = []
for i in range(0,queue_max):
    queue.append(can.Message())

def getQueueContent():
    global queue_read
    if queue_read != queue_end:
        var = queue[queue_read]
        queue_read += 1
        if queue_read >= queue_max:
            queue_read = 0
        return var
    else:
        return 0

class CAN_CLASS:
    __can_bus = "0"
    __can_speed = "250000"
    __can_obj = 0

# ******************************************************************************
#   Function name:  __init__
#   Descriptions:   Function for initializing the CAN0_CLASS module
# ******************************************************************************
    def __init__(self,can_bus,speed):
        self.__can_bus = can_bus
        self.__can_speed = speed
        self.__checkHardware()
        self.__initHardware()

# ******************************************************************************
#   Function name:  __checkHardware
#   Descriptions:   Private function for checking the hardware state
# ******************************************************************************
    def __checkHardware(self):

        if (self.__can_bus=='0'):
            aux = "1"
        elif (self.__can_bus=='1'):
            aux = "0"

        f = open(functions.route_boot_file, "r")
        repeat_loop = True

        while repeat_loop:
            a = f.readline()
            if (('mcp251x spi0.'+ aux) in a) and ('failed' in a):
                repeat_loop   = False
                shoot.error(a)
                raise AssertionError("The CAN" + self.__can_bus + " hardware is not connected properly")
            if a == "":
                shoot.info("CAN" + self.__can_bus + "  module succesfully detected")
                repeat_loop = False
        f.close()

# ******************************************************************************
#   Function name:  __initHardware
#   Descriptions:   Private function for initialiting the can comunication
# ******************************************************************************
    def __initHardware(self):
        flag = False
        result = subprocess.run(
            ['sudo','ip','link','set','can'+self.__can_bus,'up','type','can','bitrate',self.__can_speed], capture_output=True, text=True
        )
        if result.stderr == "":
            shoot.info("(" +  'can'+self.__can_bus + ") " + "Succesfully initialized")
            flag = True
        elif ("busy" in result.stderr):
            shoot.warning("(" +  'can'+self.__can_bus + ") " + result.stderr + " * (If says it is busy, it may just mean that has already been initialized, so will work properly but check Crystal Hertz)")
            flag = True
        else:
            shoot.error("(" +  'can'+self.__can_bus + ") " + result.stderr)

        if flag==True:
            try:
                self.__can_obj = can.interface.Bus("can" + self.__can_bus, bustype='socketcan_native')
                shoot.info("("+ "can" + self.__can_bus + ") Normal operation")
            except Exception as e:
                shoot.error("("+ "can" + self.__can_bus + ") __canManager function, error ocurred")
                shoot.error("("+ "can" + self.__can_bus + ") " + str(e))

# ******************************************************************************
#   Function name:  __canManager
#   Descriptions:   Function for waiting for a message
# ******************************************************************************
    def wait_for_message(self):
        try:
            msg = self.__can_obj.recv()
            self.__printRawMessage(msg)
            # data.interpret_can_msg(0, msg.arbitration_id, msg.data)
        except Exception as e:
            shoot.error("("+ "can" + self.__can_bus + ") " + str(e))

# ******************************************************************************
#   Function name:  printRawMessage
#   Descriptions:   Function that prints the received message
# ******************************************************************************
    def __printRawMessage(self,msg):
        shoot.debug(msg)

# ******************************************************************************
#   Function name:  __clasifyMessage
#   Descriptions:   Function that stores in a queue the data obtained
# ******************************************************************************
    def __clasifyMessage(self,msg):
        global queue_end
        global queue
        #msg.arbitration_id, msg.data
        queue[queue_end] = msg
        queue_end += 1
        if queue_end >= queue_max:
            queue_end = 0

# ******************************************************************************
#   Function name:  can_interruption
#   Descriptions:   Function for managing the asyncio libraries for receiving
#   the data
# ******************************************************************************
    async def can_interruption(self):

        reader = can.AsyncBufferedReader()

        listeners = [
            self.__printRawMessage, # Callback function
            reader,                 # AsyncBufferedReader() listener
            self.__clasifyMessage,  # Function for saving the data
        ]
        # Create Notifier with an explicit loop to use for scheduling of callbacks
        notifier = can.Notifier(self.__can_obj, listeners)

        while True:
            # Wait for next message from AsyncBufferedReader
            msg = await reader.get_message()

# ******************************************************************************
#   Function name:  can_interruption
#   Descriptions:   Function for managing the asyncio libraries for receiving
#   the data
# ******************************************************************************
    def sendMessage(self, msg):
        try:
            self.__can_obj.send(msg)
        except can.CanError:
            shoot.warning("There is an error sending a CAN message with id:"+ hex(msg.arbitration_id))

# -------------------- END -----------------------------------------------------

class CAN0_CLASS(CAN_CLASS):

# ******************************************************************************
#   Function name:  __init__
#   Descriptions:   Function for initializing the CAN0_CLASS module
# ******************************************************************************
    def __init__(self,speed):
        CAN_CLASS.__init__(self,'0',speed)

# -------------------- END -----------------------------------------------------

class CAN1_CLASS(CAN_CLASS):

# ******************************************************************************
#   Function name:  __init__
#   Descriptions:   Function for initializing the CAN0_CLASS module
# ******************************************************************************
    def __init__(self,speed):
        CAN_CLASS.__init__(self,'1',speed)

# -------------------- END -----------------------------------------------------
