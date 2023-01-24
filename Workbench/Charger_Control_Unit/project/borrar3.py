'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   14/06/2020
Name         :   main.py
Description  :
* This file is the main file which constructs the program
-----------------------------------------------------------------------------
'''

#!/usr/bin/python3

import time
import can
import threading
import os
clear = lambda: os.system('clear')
clear()
time.sleep(0.1)

# Local classes
from classes import can_class,bms_class,debug_class

# Local functions
from general import functions

# Variables


# Main execution
if __name__ == "__main__":

    # 1. Start the loging file document
    functions.createBootFile()

    # 2. Initialize classes
    canclss = can_class.CAN_CLASS()

    # 3. Create parallel threads for procesing the classes
    can0M = threading.Thread(target=canclss.can0Manager, daemon=True)
    can1M = threading.Thread(target=canclss.can1Manager, daemon=True)

    # 4. Start the threads
    can0M.start()       # Start the created thread
    can1M.start()       # Start the created thread

    print("\n\n**************************")
    print("********* FIN ************")
    print("**************************\n")



    while True:
        pass



# -------------------- END -----------------------------------------------------
