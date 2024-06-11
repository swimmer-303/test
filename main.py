import pyautogui
import time

# Infinite loop
while True:
    # Press spacebar
    pyautogui.press('space')
    print("Spacebar pressed")

    # Wait for 5 seconds
    time.sleep(5)
    print("Waited for 5 seconds")
