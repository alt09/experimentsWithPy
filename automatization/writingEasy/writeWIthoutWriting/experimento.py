#part of the WWW initiative ( write without writing)
import time 
import pyautogui as auto 
time.sleep(5)

with open('theText.txt','r') as theFile:
    auto.FAILSAFE = False
    for line in theFile:
        auto.typewrite(line)
        auto.press('auto') 


