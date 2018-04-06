# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:48:43 2018

@author: vriosto
"""
import pyautogui as gui
while True:
           x, y = gui.position()
           positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr, end='')
print('\b' * len(positionStr), end='', flush=True)