from enum import Enum
import typer
from rich.live import Live
from rich.table import Table
from typing_extensions import Annotated
from importlib import import_module
from mss import mss
import cv2 as cv
import numpy as np
import time
import serial
import random
# from pynput import keyboard
import keyboard

app = typer.Typer()
# console = Console()

class Specs(str, Enum):
    fury = "fury"
    sub = "sub"
    outlaw = "outlaw"
    dev = "dev"
    balance = "balance"
    spriest = "spriest"

def handle_input(name: str, key_type=None):
    if key_type:
        # print(key_type)
        ser.write(str.encode(key_type))

def load_spec(spec):
    print('Starting spec:', spec)
    #import submodule from options for rotation and talents info
    spec_ref = import_module(str(spec))
    out_talents = spec_ref.talents
    out_rotation = spec_ref.rotation
    return out_talents, out_rotation

def status(talents, sct_img):
    for i in talents:
        # print(i)
        pixel_value = sct_img.pixel(talents[i]['pixel'],1)
        if not 'multi' in (talents[i]):
            talents[i]['value'] = talents[i]['assign'] if pixel_value == talents[i]['match'] else 0
        else:
            # print(i, pixel_value, end=' ')
            gen = (item for item in talents[i]['multi'] if item['match'] == pixel_value)
            match = next(gen, None)
            if match:
                # print(match['assign'])
                talents[i]['value'] = match['assign']
            else: talents[i]['value'] = 0
    return talents

def generate_table(talents,sct_img, snap_pixel_value) -> Table:
    table = Table()
    table.add_column("Talent\nName")
    table.add_column("Talent\nValue")
    table.add_column("Pixel\nIndex")
    table.add_column("Pixel Value",width=15)
    if len(snap_pixel_value): table.add_column('Snap PixelValue')

    for i in talents:
        value = talents[i]['value']
        pixel_index = talents[i]['pixel']
        pixel_value = sct_img.pixel(talents[i]['pixel'],1)
        if any('Snap PixelValue' in column.header for column in table.columns): # type: ignore
            table.add_row(f"{i}",
                          f"[red]{value}" if value == 0 else f"[green]{value}",
                          f"{pixel_index}",f"{pixel_value}",
                          f"[yellow]{snap_pixel_value[i]}" if snap_pixel_value[i] != pixel_value else f"{snap_pixel_value[i]}")
        else: table.add_row(f"{i}",
                            f"[red]{value}" if value == 0 else f"[green]{value}",
                            f"{pixel_index}",
                            f"{pixel_value}")
    return table

@app.command()
def config(spec: Annotated[Specs, typer.Option]):
    talents, _ = load_spec(spec)
    snap_pixel_value = {}
    with mss() as sct:
        sct_img = sct.grab(monitor)
        with Live(generate_table(talents,sct_img, snap_pixel_value), refresh_per_second=2) as live:
            while 'Looping':
                time.sleep(0.3)
                # screengrab
                sct_img = sct.grab(monitor)
                # use class function to populate talent data
                talents = status(talents, sct_img)
                # scale to % for visibility
                frame = np.array(sct_img, dtype=np.uint8)
                scale_percent = 2600 # scale to percent of original size
                width = int(frame.shape[1] * scale_percent / 100)
                height = int(frame.shape[0] * scale_percent / 50)
                dim = (width, height)
                resized = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
                # cv text
                cv.putText(resized,'Press Q on this window to exit.', (int(scale_percent//100), 10), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
                cv.putText(resized,'Each number corresponds to pixel number that will be used in sct_img.pixel(i,0)', (int(scale_percent // 100), 25), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
                cv.putText(resized,'Press S to snap current pixel values to console output.', (int(scale_percent // 100), 40), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
                # mark individual scaled pixels and assing numbers
                for i in range(0,frame.shape[1]):
                    cv.putText(resized,"_", (int(scale_percent//100*i)+2, 55), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
                    cv.putText(resized,str(i), (int(scale_percent//100*i+2), 70), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
                # display scaled canvas
                cv.imshow('Scaled pixel array', resized)
                # cv termination on Q
                keypressed = cv.waitKey(25) & 0xFF
                if keypressed == ord("q"):
                        cv.destroyAllWindows()
                        quit()
                # pixel value snapshot
                elif keypressed == ord("s"):
                    for i in talents:
                        snap_pixel_value[i] = sct_img.pixel(talents[i]['pixel'],1)
                # console table output
                live.update(generate_table(talents,sct_img, snap_pixel_value))
            
            
@app.command()
def run(spec: Annotated[Specs, typer.Option]):
    talents, rotation = load_spec(spec)
    with mss() as sct:
        while 'Looping':
            time.sleep(0.3)
            sct_img = sct.grab(monitor)
            talents = status(talents, sct_img)
            # print(talents)
            handle_input('', rotation(talents))

if __name__ == '__main__':
        monitor_number = 1
        monitor = {
                "top": 0+11,  # 110px from the top
                "left": 0+10,  # 100px from the left
                "width": 56,
                "height": 2,
                "mon": monitor_number,
            }
        ser = serial.Serial('COM6') # open serial
        app()