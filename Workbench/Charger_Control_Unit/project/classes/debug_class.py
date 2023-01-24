'''
-----------------------------------------------------------------------------
Author       :   Luis de la Barba
Date         :   18/06/2020
Name         :   debug_class.py
Description  :
* This file is for formatting the logging and displaying debugging info
-----------------------------------------------------------------------------
'''

import logging

'''
LEVELS:
    1. NOTSET
    2. DEBUG
    3. INFO
    4. WARNING
    5. ERROR
    6. CRITICAL
'''
logging.getLogger('asyncio').setLevel(logging.WARNING) # Remove log mesage from the asyncio library


name_route      = 'files/'
name_debug_file   = 'debug.log'

route_debug_file   = name_route + name_debug_file
f = open(route_debug_file,'a')
f.write("\n\n************************************************** \n")
f.write("                   NEW SESSION \n")
f.write("************************************************** \n")
f.close()
logging.basicConfig(level=logging.INFO, format='%(message)s')
fh = logging.FileHandler(route_debug_file)
fh.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s","%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)

class DEBUG_CLASS:
    log_display = None      # For displaying the data without registering in a file
    log_file    = None      # Logging data and write in a field
    def __init__(self, name):
        self.log_display    = logging.getLogger(name)
        self.log_file       = logging.getLogger(name)
        self.log_file.addHandler(fh)
        self.__name = name
    def changeLevelToInfo(self):
        self.log_file.setLevel(logging.INFO)
    def changeLevelToDebug(self):
        self.log_file.setLevel(logging.DEBUG)
        pass
