from mss import mss
import cv2 as cv
import numpy as np
import time
import serial
import random
# from pynput import keyboard
import keyboard

def handle_input(name: str, key_type=None):
    if key_type:
        ser.write(str.encode(key_type))

def action(talents: dict):
