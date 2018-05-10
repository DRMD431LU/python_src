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

def download_csv(name,url, *args,**kwargs):
	webbrowser.open(url)
	match1=False
	while not match1:
		im=gui.screenshot()
		im.getpixel((973, 131))
		match1=gui.pixelMatchesColor(973,131,(85,85,85))
	match1=False
	gui.click(973,131)
	while not match1:
		gui.press('end')
		center_x,center_y,match=location("csv.png")
		match1=match
	match1=False
	gui.click(center_x,center_y)
	# center_x,center_y=location("option_btn.png")
	# gui.click(center_x,center_y)
	# center_x,center_y,match=location("submit.png")
	# gui.click(center_x,center_y)
	center_x,center_y,match=location("guardar.png")
	gui.typewrite(name)
	# center_x,center_y,match=location("txt.png")
	gui.press("enter")
	center_x,center_y,match=location("yes.png")
	gui.click(center_x,center_y)

def location(lookup, *args, **kwargs):
	match=False
	while not match:
		print("searching " + lookup)
		im=gui.screenshot()
		location=gui.locateOnScreen(lookup)
		print(location)
		if location:
			center_x,center_y=gui.center(location)
			match=location
		else:
			im=None
	return center_x,center_y,match

def archivos():
	urls={
'acsa':r'http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=182&courseid=1',
'acsa0':r'http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=180&courseid=1',
'ceab':r"http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=167&courseid=1",
'ceap':r"http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=157&courseid=1",
'cfa':r"http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=183&courseid=1",
'cfa0':r"http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=162&courseid=1",
'meab':r"http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=159&courseid=1",
'meac':r"http://aulavirtual.utel.edu.mx/blocks/configurable_reports/viewreport.php?id=149&courseid=1",
}
	names={
'acsa':"ACSA.csv",
'acsa0':"ACSA0.csv",
'ceab':"CEAB.csv",
'ceap':"CEAP.csv",
'cfa':"CFA.csv",
'cfa0':"CFA0.csv",
'meab':"MEAB.csv",
'meac':"MEAC.csv",
}

	download_csv(names['acsa'],urls['acsa'])
	download_csv(names['acsa0'],urls['acsa0'])
	download_csv(names['ceab'],urls['ceab'])
	download_csv(names['ceap'],urls['ceap'])
	download_csv(names['cfa'],urls['cfa'])
	download_csv(names['cfa0'],urls['cfa0'])
	download_csv(names['meab'],urls['meab'])
	download_csv(names['meac'],urls['meac'])

print("hello world")
archivos()

# match1=False
# while not match1:
# 	center_x,center_y,match=location("option_btn.png")
# 	math1=match
	
# match1=False
# gui.click(center_x,center_y)







#print(im.getpixel((1222,277)))

#browser.refresh()

#continue_link = browser.find_element_by_partial_link_text('Accesos con status')
#res=rq.get("")


#element = browser.find_element_by_xpath("//a[@text()='Accesos con status AB018_II']")

