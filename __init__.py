#Test 1 Automatizacion SBClient
import pyautogui as p
import time as t

from MainFunctions.countryCode import cc as cc
from Open.mainOpen import open as Mopen
from MainFunctions.confirmacion import confirm as confirm
from MainFunctions.action import actions as actions


#Abrir la ventana deseada con mainOpen.py
a=Mopen()
#Primera Confirmación || confirmacion.py
confirm()
#Obtener Country Code del usuario countryCode.py
cd=cc()
#Acción dependiendo de la ventana que se abrió action.py
#Envía la opcion elegida al inicio y el countryCode
actions(a,cd)
#This isnt a big change
