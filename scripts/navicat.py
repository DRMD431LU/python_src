import subprocess as sub
import pyautogui as gui, requests as rq
import time
import datetime as dt


def location(lookup, *args, **kwargs):
	match=False
	while not match:
		print("searching"+ lookup)
		im=gui.screenshot()
		location=gui.locateOnScreen(lookup)
		print(location)
		if location:
			center_x,center_y=gui.center(location)
			match=location
		else:
			im=None
	return center_x,center_y,match
def navicat_auto(): 
	start_time = time.time()
	st = dt.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
	st,a=st.split(" ")
	path=r"C:\Users\vriosto\Desktop\new_indicadores"+st+".csv"

	sub.Popen(r"C:\Program Files\PremiumSoft\Navicat Premium Essentials 12\navicat.exe")
	center_x,center_y,match=location("test.png")
	gui.doubleClick(center_x,center_y)

	center_x,center_y,match=location("db.png")
	gui.doubleClick(center_x,center_y)

	center_x,center_y,match=location("public.png")
	gui.doubleClick(center_x,center_y)
	center_x,center_y,match=location("tables.png")
	gui.doubleClick(center_x,center_y)
	gui.press('end')
	gui.press('end')
	time.sleep(1)
	center_x,center_y,match=location("materia_table.png")
	gui.click(button='right',x=center_x,y=center_y)
	center_x,center_y,match=location("empty_table.png")
	gui.click(center_x,center_y)
	center_x,center_y,match=location("empty_btn.png")
	gui.click(center_x,center_y)
	center_x,center_y,match=location("materia_table_active.png")
	gui.doubleClick(center_x,center_y)
	center_x,center_y,match=location("import.png")
	gui.click(center_x,center_y)
	gui.moveTo(100, 200,1)  
	gui.moveTo(None, 500,1)
	center_x,center_y,match=location("csv_nav.png")
	gui.click(center_x,center_y)
	center_x,center_y,match=location("next.png")
	gui.click(center_x,center_y)
	center_x,center_y,match=location("import_file.png")
	gui.click(center_x,center_y)
	gui.typewrite(path)
	center_x,center_y,match=location("next.png")
	gui.click(center_x,center_y)
	gui.moveTo(100, 200,1)  
	
	center_x,center_y,match=location("next_active.png")
	gui.doubleClick(center_x,center_y)
	gui.moveTo(100, 200,1)  
	
	center_x,center_y,match=location("next_active.png")
	gui.doubleClick(center_x,center_y)
	gui.moveTo(100, 200,1)  
	
	center_x,center_y,match=location("next_active.png")
	gui.click(center_x,center_y)
	gui.moveTo(100, 200,1)  
	gui.moveTo(None, 500,1)
		
	center_x,center_y,match=location("append.png")
	gui.click(center_x,center_y)
	gui.moveTo(100, 200,1)  
	center_x,center_y,match=location("next.png")
	gui.click(center_x,center_y)
	center_x,center_y,match=location("start.png")
	gui.click(center_x,center_y)


