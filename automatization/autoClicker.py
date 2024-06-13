# This script simulates 100 mouse clicks using the pyautogui library after a delay of 5 seconds.

import time 
import pyautogui as auto 

# Pause the script for 5 seconds to allow the user to prepare (e.g., move the mouse to the desired location)
time.sleep(5)

# Disable the fail-safe feature of pyautogui, which stops the script if the mouse is moved to a corner of the screen
auto.FAILSAFE = False

# Simulate 100 mouse clicks
for i in range(100):
    auto.click()
