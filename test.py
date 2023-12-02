import serial
import time
ser = serial.Serial('COM6') # open serial

def handle_input(name: str, key_type=None):
    if key_type:
        print(key_type)
        ser.write(str.encode(key_type))

time.sleep(2)
handle_input('f','alt2')
time.sleep(0.5)
print('send')
handle_input('f','alt2')
time.sleep(0.5)
print('send')
handle_input('f','alt2')
