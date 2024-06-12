import time 
import pyautogui as auto 
time.sleep(5)
auto.FAILSAFE = False
for i in range(100):
    auto.click()
