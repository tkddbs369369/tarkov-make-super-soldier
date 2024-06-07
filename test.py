
import pyautogui as pg
import time
import pydirectinput
time.sleep(2)

pg.moveTo(pg.size().width-40,pg.size().height//2, duration=0.5)
time.sleep(1)
for i in range(10):
    pg.scroll(1)
    print(i)
while True:
    try:
        try:
            gr = pg.locateCenterOnScreen("img/m67.PNG", confidence=0.995)
            print(gr)
        except:
            try:
                gr = pg.locateCenterOnScreen("img/rgd-5.PNG", confidence=0.995)
                print(gr)
            except:
                try:
                    gr = pg.locateCenterOnScreen("img/f-1.PNG", confidence=0.995)
                    print(gr)
                except:
                    pass
        pg.keyDown('ctrl')
        time.sleep(1)
        pg.moveTo(gr.x, gr.y)
        pg.click()
        pg.keyUp('ctrl')
        time.sleep(1)
        break
    except:
        for i in range(12):
            pg.scroll(-1)
pg.press('Tab')