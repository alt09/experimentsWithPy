# Part of the WWW initiative (write without writing)
# This script reads text from a file and simulates typing it using the pyautogui library.

import time 
import pyautogui as auto 

# Pause the script for 5 seconds to allow the user to prepare (e.g., switch to the target window)
time.sleep(5)

# Open the file 'theText.txt' in read mode
with open('theText.txt', 'r') as theFile:
    # Disable the fail-safe feature of pyautogui, which stops the script if the mouse is moved to a corner of the screen
    auto.FAILSAFE = False

    # Iterate through each line in the file
    for line in theFile:
        # Simulate typing the current line
        auto.typewrite(line)
        # Press the 'enter' key after typing each line (likely a typo, should specify a valid key, e.g., 'enter')
        auto.press('enter')  
