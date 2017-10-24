import pyautogui as p
import time as t

p.press('win')
t.sleep(0.5)
p.typewrite('slack')
t.sleep(1)
p.press('enter')
p.moveTo(450,950)
t.sleep(3)
p.click()
test = p.confirm(text='Continue?', title='', buttons=['Yes', 'No'])
if test == 'No':
		exit()
t.sleep(1)
p.moveTo(700,400)
p.click()
p.typewrite("Miryam Montero")
p.press('enter')
t.sleep(2)
p.typewrite("You look nice!! :blush: [sended from python script]")
test = p.confirm(text='Continue?', title='', buttons=['Yes', 'No'])
if test == 'No':
		exit()
p.press('enter')
