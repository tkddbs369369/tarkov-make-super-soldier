
import pyautogui as pg
import time
import pydirectinput
time.sleep(2)

a = list(range(370))

for i in range(2):
    pg.keyDown('w')
    pg.keyDown('space')
    pg.keyDown('shift')
    time.sleep(0.1)
    for i in a:
        pydirectinput.moveRel(1000,0,relative=True)
        time.sleep(0.001)
    pg.keyUp('shift')
    pg.keyUp('w')
    pg.keyUp('space')
    time.sleep(1)
    for i in range(1,11):
        if i % 2 == 0:
            pg.keyDown('w')
            time.sleep(3)
            pg.keyUp('w')
        if i % 2 == 1:
            pg.keyDown('s')
            time.sleep(3)
            pg.keyUp('s')




# 시리얼 포트 닫기
