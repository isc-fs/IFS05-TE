'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   28/07/2021
Name         :   main.py
Description  :
* This file is the main file which constructs the program
-----------------------------------------------------------------------------
'''

#!/usr/bin/python3

import time
import can
import asyncio
from sys import platform
import os
from general import display

if platform == "linux" or platform == "linux2":     # linux
    clear = lambda: os.system('clear')
elif platform == "darwin":                          # OS X
    pass
elif platform == "win32":                           # Windows...
    clear = lambda: os.system('cls')

time.sleep(0.1)
clear()
time.sleep(0.1)

# Local classes
from classes import debug_class
from classes import can_class,charger_class

# Local functions
from general import functions

# Variables
var = debug_class.DEBUG_CLASS(__name__)
var.changeLevelToDebug()
shoot = var.log_file

can0_speed  = '250000' # Must be written as string
can1_speed  = '250000' # Must be written as string
CHARGER_ID_CAN_recv = 0x18FF50E7
CHARGER_ID_CAN_send = 0x1806E7F4
CHARGER_MAXV    =   350
CHARGER_MAXI  = 10    # A
CHARGER_MINI  = 0.05  # A # Current at which the battery stops charging

#*******************************************************************************
#   Function name:           parseMain
#   Descriptions:            Function for analysing the received CAN message
#*******************************************************************************
def parseMain(t):
    msg = can_class.getQueueContent()
    #print(msg)
    if msg:
        if charger.parse(msg,t): pass
        else: shoot.debug(msg)
    #charger.parse(t)









#*******************************************************************************
#   Function name:           queryMain
#   Descriptions:            Function for making the corrresponding queries
#*******************************************************************************
def queryMain(t):
    charger.query(t)











#*******************************************************************************
#   Function name:           state_machine
#   Descriptions:            Function for making the state machine
#*******************************************************************************
async def state_machine():
    while True:
        t = time.time()
        parseMain(t)
        queryMain(t)
        await asyncio.sleep(0.001)

















# Main execution
if __name__ == "__main__":

    # 1. Creates a file that logs all the booting errors of the rasberry
    functions.createBootFile()

    can0 = can_class.CAN0_CLASS(can0_speed)
    charger = charger_class.CHARGER_CLASS(
        CHARGER_ID_CAN_send,CHARGER_ID_CAN_recv, \
        CHARGER_MAXV,CHARGER_MAXI,CHARGER_MINI)

    #while True:
        #can0.wait_for_message()

    loop = asyncio.get_event_loop()             # Sirve para iniciar una cola de loop que se va a ejecutar
    try:
        #asyncio.ensure_future(firstWorker())    # Este comando se usa para introducirlos en la cola del loop, para asi correrlo despues
        #asyncio.ensure_future(secondWorker())
        asyncio.ensure_future(state_machine())
        asyncio.ensure_future(charger.routine(can0))
        asyncio.ensure_future(can0.can_interruption())
        loop.run_forever()                      # Con run forever, cuando terminan todas las funciones, se vuelve a empezar el proceso
    except KeyboardInterrupt:
        pass
    except Exception as e:
        shoot.error(e)
    finally:
        print("Closing Loop")
        loop.close()

    print("\n\n**************************")
    print("********* FIN ************")
    print("**************************\n")

    ##MOSTRAR EL DISPLAY
    display.app.run_server(debug=True, port=1111)

# -------------------- END -----------------------------------------------------
