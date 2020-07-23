#! python3

import time
import pyautogui

print('NudgeBot activated, press CTRL-C to quit')

try:
    while True:
        pyautogui.moveRel(10, 0, 0.5)
        pyautogui.moveRel(-10, 0, 0.5)
        time.sleep(10)
except KeyboardInterrupt:
    print('NudgeBot deactivated.')