# Part of the WWW initiative (write without writing)
# This script reads text from a file and simulates typing it using the pyautogui library.

import time 
import pyautogui as auto 

# Pause the script for 5 seconds to allow the user to prepare (e.g., switch to the target window)
time.sleep(2)
i=1
# Iterate through each line in the file
for i in range(1000):
    # Simulate typing the current line
    auto.typewrite('thanks  we  missed you ana (' + str(i + 1) + ')')
    # Press the 'enter' key after typing each line (likely a typo, should specify a valid key, e.g., 'enter')
    auto.press('enter')  
