import time
import pyautogui
import numpy as np
import keyboard
import os
import nantianshan
import yuliushan
import qingyushan

class Status():
    MOVE = 1
    BATTLE = 2
    START = 3
    SWITCHTOSELL = 4
    SWITCHTOMAP = 5
    SELL = 6

# find png
def toPngPos(pngname,isMoveTo = False,con = 0.8):
    pos = pyautogui.locateOnScreen("./Assets/" + pngname,confidence=con)
    if pos != None:
        last = pyautogui.position()
        pyautogui.moveTo(pyautogui.center(pos))
        pyautogui.click()
        if isMoveTo == False:
            pyautogui.moveTo(last)
        return True
    return False
def toPngPosNotClick(pngname,isMoveTo = False):
    pos = pyautogui.locateOnScreen("./Assets/" + pngname,confidence=0.8)
    if pos != None:
        last = pyautogui.position()
        pyautogui.moveTo(pyautogui.center(pos))
        if isMoveTo == False:
            pyautogui.moveTo(last)
        return True
    return False

# 按格子移动鼠标
def moveGrid(x,y):
    global gamePos
    global status
    last = pyautogui.position()
    pyautogui.moveTo(gamePos)
    pyautogui.move(x*56,y*56)
    pyautogui.click()
    pyautogui.move(-x*56,-y*56)

    pyautogui.moveTo(last)
    if toPngPos("gongji.png"):
        status = Status.BATTLE

# 按格子移动鼠标
def moveSellGrid(x,y):
    pyautogui.move(x*100,y*100)
    pyautogui.click()
    
moveIndex = 0

def doMove():
    global moveIndex
    global status
    if moveIndex < len(movePositions):
        moveGrid(movePositions[moveIndex][0],movePositions[moveIndex][1])
        time.sleep(0.5)
        moveIndex = moveIndex + 1
        if toPngPos("gongji.png"):
            status = Status.BATTLE
        if toPngPos("lingqu.png"):
            time.sleep(0.2)
        if toPngPos("battlefailed.png"):
            time.sleep(0.2)
            toPngPos("quit.png")
            status = Status.SWITCHTOSELL
        if moveIndex >= len(movePositions):
            status = Status.SWITCHTOSELL
    else:
        status = Status.SWITCHTOSELL
    print("Move")

def doBattle():
    global status
    time.sleep(1)
    if toPngPos("battlefailed.png"):
        time.sleep(0.2)
        toPngPos("quit.png")
        status = Status.SWITCHTOSELL
        return
    if toPngPos("tuichu.png"):
        time.sleep(0.2)
    if toPngPos("lingqu.png"):
        status = Status.MOVE
    print("Battle")
def findEntry():
    global status
    global moveIndex
    global gamePos
    print("Entry")
    for entry in mapentry:
        if toPngPos(entry,False,0.9):
            time.sleep(1)
            if toPngPos("chuansong0.png",True):
                moveIndex = 0
                gamePos = pyautogui.position()
                status = Status.MOVE
                break

sellPos = [
    [0,0],[1,0],[1,0],[1,0],[1,0],[1,0],
    [0,-1],[-1,0],[-1,0],[-1,0],[-1,0],[-1,0],
    # [0,-1],[1,0],[1,0],[1,0],[1,0],[1,0]
]
sellIndex = 0
def doSell():
    global sellIndex
    global status
    if sellIndex < len(sellPos):
        pyautogui.move(sellPos[sellIndex][0]*90,sellPos[sellIndex][1]*90)
        pyautogui.click()
        time.sleep(0.5)
        toPngPos("sellall.png")
        time.sleep(1)
        sellIndex = sellIndex + 1
        if sellIndex >= len(sellPos):
            if toPngPos("sellexit.png",True):
                sellIndex = 0
                status = Status.SWITCHTOMAP
    else:
        if toPngPos("sellexit.png",True):
            sellIndex = 0
            status = Status.SWITCHTOMAP

gamePos = pyautogui.position()
status = Status.START
map = qingyushan.QingYuShan()
movePositions = map.MovePosition
mapentry = map.EnterNames
# 主循环
isStop = False
def checkQuit(key):
    global isStop
    if key.event_type == "down" and key.name == "esc":
        print("exit")
        isStop = True
keyboard.hook(checkQuit)

try:
    while(True):
        if isStop:
            break
        if status == Status.START:
            time.sleep(1)
            findEntry()
        elif status == Status.MOVE:
            doMove()
        elif status == Status.BATTLE:
            doBattle()
        elif status == Status.SWITCHTOSELL:
            if toPngPos("bag0.png"):
                time.sleep(0.2)
                if toPngPos("sellentry.png"):
                    time.sleep(0.2)
                    if toPngPosNotClick("sellexit.png",True):
                        pyautogui.move(-220,-150)
                        status = Status.SELL
        elif status == Status.SELL:
            doSell()
        elif status == Status.SWITCHTOMAP:
            if toPngPos("xianyuan.png"):
                status = Status.START
except Exception as err:
    print("Done",err)

