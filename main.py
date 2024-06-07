import time
import pyautogui as pg
import pydirectinput
import serial
time.sleep(2)
while True:
    try:
        time.sleep(1)
        _1 = pg.locateCenterOnScreen("img/1.PNG", confidence=0.8)
        pg.click(_1.x, _1.y)
    except:
        pass


    try:
        time.sleep(1)
        _2 = pg.locateCenterOnScreen("img/2.PNG", confidence=0.8)
        pg.click(_2.x, _2.y)
    except:
        pass


    try:
        time.sleep(1)
        _3 = pg.locateCenterOnScreen("img/3.PNG", confidence = 0.8)
        pg.click(_3.x,_3.y)
    except:
        pass


    try:
        time.sleep(1)
        _4 = pg.locateCenterOnScreen("img/4.PNG", confidence=0.8)
        pg.click(_4.x, _4.y)

    except:
        pass






    while True:
        try:
            st = pg.locateCenterOnScreen("img/start.PNG", confidence=0.8)
            time.sleep(2)
            break
        except:
            pass

    a = list(range(370))

    for i in range(3):
        pg.keyDown('w')
        pg.keyDown('space')
        pg.keyDown('shift')
        time.sleep(0.1)
        for z in a:
            pydirectinput.moveRel(1000, 0, relative=True)

        pg.keyUp('shift')
        pg.keyUp('w')
        pg.keyUp('space')
        time.sleep(1)
        for f in range(1, 11):
            if f % 2 == 0:
                pg.keyDown('w')
                time.sleep(3)
                pg.keyUp('w')
            if f % 2 == 1:
                pg.keyDown('s')
                time.sleep(3)
                pg.keyUp('s')
        try:
            _7 = pg.locateCenterOnScreen("img/7.PNG", confidence=0.8)
            break
        except:
            pass
        print(i)
        if i == 2:
            time.sleep(2)
            pydirectinput.moveRel(0, 1000, relative=True, )
            time.sleep(0.2)
            pg.keyDown('g')
            time.sleep(0.2)
            pg.keyUp('g')
            time.sleep(2)
            pg.click(button='right')

    while True:
        try:
            time.sleep(2)
            _7 = pg.locateCenterOnScreen("img/7.PNG", confidence=0.8)
            pg.click(_7.x, _7.y)
            break
        except:
            pass


    while True:
        try:
            time.sleep(2)
            _71 = pg.locateCenterOnScreen("img/7-1.PNG", confidence=0.8)
            try:
                ac = pg.locateCenterOnScreen("img/7_2.PNG", confidence=0.8)
                time.sleep(0.5)
                _72 = pg.locateCenterOnScreen("img/no.PNG", confidence=0.8)
                pg.click(_72.x, _72.y)
                time.sleep(0.5)
                hp = pg.locateCenterOnScreen("img/hp.PNG", confidence=0.8)
                pg.click(hp.x, hp.y)
                time.sleep(0.5)
                ac = pg.locateCenterOnScreen("img/ap.PNG", confidence=0.8)
                pg.click(ac.x, ac.y)
                time.sleep(0.5)
                ac = pg.locateCenterOnScreen("img/2.PNG", confidence=0.8)
                pg.click(ac.x, ac.y)
                break
            except:
                pass
            pg.click(_71.x, _71.y)
            break
        except:
            continue

    while True:
        try:
            _8 = pg.locateCenterOnScreen("img/8.PNG", confidence=0.8)
            pg.press('Tab')
            time.sleep(1)
            break
        except:
            pass

    pg.moveTo(pg.size().width-40,pg.size().height//2, duration=0.5)
    time.sleep(1)
    for i in range(60):
        pg.scroll(1)
        print(i)
    while True:
        gr = 0
        try:
            try:
                gr = pg.locateCenterOnScreen("img/m67.PNG", confidence=0.995)

            except:
                try:
                    gr = pg.locateCenterOnScreen("img/rgd-5.PNG", confidence=0.995)

                except:
                    try:
                        gr = pg.locateCenterOnScreen("img/f-1.PNG", confidence=0.995)

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