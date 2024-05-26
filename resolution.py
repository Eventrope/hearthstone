import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f'X: {x} Y: {y}', end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nDone')

    # refresh = 1071, 2583
    # freeze=1172,2223
    # heropower = 1059, 8383
    # click_x, click_y = 1071, 232  # Example coordinates