import keyboard  # using module keyboard
import time
while True:  # making a loop
    time.sleep(0.5)
    test = keyboard.key_to_scan_codes([1,2])
    print(test)
