# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:43:10 2018

@author: vriosto
"""

import threading, time

print('Start of program.')

def takeANap():
    time.sleep(15)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')