import pydirectinput
import time
import pyautogui as pg
time.sleep(4)
eror = pg.locateCenterOnScreen("img/1.PNG", confidence=0.8)

if eror:
    print(123)