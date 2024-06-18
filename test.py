import pydirectinput
import time
import pyautogui as pg
time.sleep(1)
while True:
    gr = 0
    try:
        try:
            gr = pg.locateCenterOnScreen("img/m67.PNG", confidence=0.8)
        except:
            pass
        try:
            gr = pg.locateCenterOnScreen("img/rgd-5.PNG", confidence=0.8)
        except:
            pass
        try:
            gr = pg.locateCenterOnScreen("img/f-1.PNG", confidence=0.8)
        except:
            pass
        pg.keyDown('ctrl')
        time.sleep(1)
        pg.moveTo(gr.x, gr.y)
        pg.click()
        time.sleep(1)
        pg.keyUp('ctrl')
        time.sleep(1)
        break
    except:
        for i in range(12):
            pg.scroll(-1)
pg.press('Tab')