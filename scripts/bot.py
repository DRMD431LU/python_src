# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
import pyautogui as gui, requests as rq
import webbrowser
import threading, time
match=False
center_x=None
center_y=None
url=r'http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=182&courseid=1'
webbrowser.open(url)


#from selenium.webdriver.common.by import By
#import pandas as pd
#import openpyxl as xl
#res=rq.get("viewreport.php?id=182&courseid=1&download=1&format=csv")
#type(res)
#browser=wb.Firefox()
#browser.get('http://aulavirtual.utel.edu.mx/login/index.php')


#MoodleSession = {'name':'MoodleSession','value':'bar'}

#MOODLEID = {'name':'MOODLEID','value':'gpacheco'}
#browser.add_cookie(MoodleSession)
#browser.add_cookie(MOODLEID)
#username=browser.find_element_by_id('username')
##username.clear()
#username.send_keys('gpacheco')
#passwd=browser.find_element_by_id('password')
##passwd.clear()
#passwd.send_keys('Necromancer666')
#passwd.send_keys(Keys.RETURN)
##
#MoodleSession = {'name':'MoodleSession','value':'bar'}
#
#MOODLEID = {'name':'MOODLEID','value':'gpacheco'}
#browser.add_cookie(MoodleSession)
#browser.add_cookie(MOODLEID)
#gui.click(89, 55)

while not match:
    im=gui.screenshot()
    im.getpixel((973, 131))
    match=gui.pixelMatchesColor(973,131,(85,85,85))

gui.press('end')
time.sleep(2)
im=gui.screenshot()
location=gui.locateOnScreen('csv.png')
center_x,center_y=gui.center(location)
gui.click(center_x,center_y)
time.sleep(2)
im=gui.screenshot()
gui.locateOnScreen('submit.png')

#print(im.getpixel((1222,277)))

#browser.refresh()

#continue_link = browser.find_element_by_partial_link_text('Accesos con status')
#res=rq.get("")
print("hello world")

#element = browser.find_element_by_xpath("//a[@text()='Accesos con status AB018_II']")

