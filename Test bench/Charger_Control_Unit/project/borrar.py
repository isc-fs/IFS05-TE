
import time
import threading
from sys import platform
import os
if platform == "linux" or platform == "linux2":     # linux
    clear = lambda: os.system('cls')
elif platform == "darwin":                          # OS X
    pass
elif platform == "win32":                           # Windows...
    clear = lambda: os.system('cls')

clear()

from classes import bms_class,sevcon_class,debug_class
from general import functions


id = 0x12c
lim_maxV = 4100
lim_minV = 3000
lim_maxT = 45
numCells = 8
shunt    = 4000

bms = [ bms_class.BMS_CLASS(id, lim_maxV, lim_minV, lim_maxT, numCells, shunt),
        bms_class.BMS_CLASS(id+10, lim_maxV, lim_minV, lim_maxT, numCells, shunt),
        bms_class.BMS_CLASS(id+20, lim_maxV, lim_minV, lim_maxT, numCells, shunt)]

time.sleep(0.1)
TPDO1 = 0x101
TPDO2 = TPDO1 + 1
TPDO3 = TPDO2 + 1
TPDO4 = TPDO3 + 1
TPDO5 = TPDO4 + 1
sevcon = sevcon_class.SEVCON_CLASS(TPDO1,TPDO2,TPDO3,TPDO4,TPDO5)

def display_info():
    while True:
        t = time.time()
        for x in range(len(bms)):
            bms[x].plotting(t)
            bms[x].communicating(t)
            sevcon.plotting(t)
            #sevcon.communicating(t)

# Main execution
if __name__ == "__main__":
    can0M = threading.Thread(target=display_info, daemon=True).start()
    while True:
        pass





#
