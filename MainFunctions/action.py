
import pyautogui as p
import time as t

def actions(a,cc):
	if a=='GD':
	    cd= (cc+'LEN')
	    p.typewrite(cd, interval=0.2)
	    t.sleep(1)
	    p.press('tab')

	elif a=='CE':
		pass
