# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
import pyautogui as gui
#from selenium.webdriver.common.by import By
#import pandas as pd
#import openpyxl as xl

browser=wb.Firefox()
browser.get('http://aulavirtual.utel.edu.mx/login/index.php')

MoodleSession = {'name':'MoodleSession','value':'bar'}

MOODLEID = {'name':'MOODLEID','value':'gpacheco'}
browser.add_cookie(MoodleSession)
browser.add_cookie(MOODLEID)
username=browser.find_element_by_id('username')
username.clear()
username.send_keys('gpacheco')
passwd=browser.find_element_by_id('password')
passwd.clear()
passwd.send_keys('Necromancer666')
passwd.send_keys(Keys.RETURN)
#
MoodleSession = {'name':'MoodleSession','value':'bar'}

MOODLEID = {'name':'MOODLEID','value':'gpacheco'}
browser.add_cookie(MoodleSession)
browser.add_cookie(MOODLEID)
gui.click(89, 55)
#im=gui.screenshot()
#im.getpixel((9, 81))
#print(im.getpixel((1222,277)))

browser.refresh()

#continue_link = browser.find_element_by_partial_link_text('Accesos con status')
print("hello world")

#element = browser.find_element_by_xpath("//a[@text()='Accesos con status AB018_II']")

