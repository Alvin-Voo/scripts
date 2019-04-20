#!/usr/bin/env python3

import pyautogui
import time

print('Press Ctrl-C to quit.')
# first hover your mouse cursor to the point u need focus
# open python console, run import pyautogui; pyautogui.position() to get cursor position
pyautogui.click(1534, 363)
try:
  while True:
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
except KeyboardInterrupt:
  print('Done')