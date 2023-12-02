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
    if talents["Canattack"] and talents["ShiftingPower"] != 2:
        if talents["CASTING"] and talents["CounterSpell"]: handle_input('','l')
        elif talents["HotStreakBuff"] and (talents["Pyro"] >= 1 or talents["Fireball"] >= 1) and\
            not talents["PyroclasmBuffExpiration"] and not talents["CombusionBuff"] <= 5:
            handle_input('stopcast', 'k')
        elif talents["BLDebuff"] and talents["EnemyHP"] == 2000000 and talents["CombusionBuff"]:
            if talents["TimeWarp"]: handle_input('','x')
        elif talents["CombusionBuff"] != 0:
            if not talents["Pyro"]:
                if talents["HotStreakBuff"]: handle_input('','1')
                elif talents["SunKing"] >= 8 and not talents["CombusionBuff"] <= 5: handle_input('','1')
                elif talents["DragonBreath"] == 1 and talents["CombusionBuff"] <= 1: handle_input('','6') #13
                elif talents["PyroclasmBuff"] and talents["PyroclasmBuffExpiration"] and talents["CombusionBuff"] <= 5 and talents["EnemyHP"] >= 300000: handle_input('','1')
                elif (talents["FireBlast"] or talents["Phoenix"]):
                    if talents["Phoenix"] >= talents["FireBlast"]: handle_input('','4')
                    else: handle_input('','3') #15
                elif talents["Scorch"]: handle_input('','5') #19.
        elif talents["CombusionBuff"] == 0:
            if talents["PlayerMove"]:
                if talents["HotStreakBuff"] and not talents["Pyro"]: handle_input('','1') #12
                elif talents["Scorch"]: handle_input('','5') #19.
            else:
                if talents["HotStreakBuff"] and not talents["Pyro"]:
                    handle_input('','1') #12
                elif talents["ShiftingPower"] != 0 and talents["CombusionBuff"] == 0 and \
                    talents["Combustion"] == 0 and talents["Rune"] == 0 and \
                    (talents["Pyro"] == 0 or talents["Fireball"] == 0):
                    handle_input('','v')
                elif talents["Rune"] == 1 and not talents["Rune"] == 2 and not talents["Combustion"] and \
                    talents["SunKing"] >= 6:
                    handle_input('','j') #11
                elif talents["SunKing"] == 8 and talents["EnemyHP"] >= 300000:
                    handle_input('','1')
                elif talents["PyroclasmBuff"] and talents["EnemyHP"] >= 300000 and not talents["Rune"] == 5 and not talents["Combustion"] == 9 and talents["SunKing"] <= 5 and talents["PyroclasmBuffExpiration"]:
                    handle_input('','1')
                elif talents["Combustion"] == 1 and talents["EnemyHP"] >= 500000 and (talents["Fireball"] <= 1 or talents["Pyro"] <= 1):
                    handle_input('','r') #10
                elif talents["Phoenix"] >= 2 and talents["HeatingUpBuff"] and talents["Rune"] == 2 and talents["Combustion"] in {0,25}:
                        handle_input('','4') #16
                elif talents["FireBlast"] >= 2 and talents["HeatingUpBuff"] and talents["Combustion"] in {0,25,9}:
                        handle_input('','3') #14
                elif talents["FireBlast"] >= 1 and talents["HeatingUpBuff"] and talents["Combustion"] in {0,25}:
                        handle_input('','3') #14
                elif talents["EnemyHP30%"] and talents["Scorch"]:
                    handle_input('','5') #17.
                elif talents["Fireball"] == 0:
                    handle_input('','2') #18.
def get_data(sct_img,talents: dict):
        talents["Canattack"] = 1 if sct_img.pixel(0,0) == (255, 141, 120) else 0
        hpP = sct_img.pixel(1,0) # HP
        if hpP == (238, 242, 0): talents["HP"] = 80
        elif hpP == (134,135,0): talents["HP"] = 60
        elif hpP == (72,68,0): talents["HP"] = 30
        else: talents["HP"] = 0
        talents["TimeWarp"] = 1 if sct_img.pixel(2,0) == (18, 255, 0) else 0
        # talents["BLDebuff"] = 1 if sct_img.pixel(2,0) == (15, 211, 0) else 0
        if sct_img.pixel(3,0) == (255, 246, 0): talents["Combustion"] = 1
        elif sct_img.pixel(3,0) == (0, 255, 255): talents["Combustion"] = 25 # 5 sec before cooldown
        elif sct_img.pixel(3,0) == (0, 204, 204): talents["Combustion"] = 9 # 5 sec before cooldown
        else: talents["Combustion"] = 0
        # print(talents["Combustion"], sct_img.pixel(3,0))
        if sct_img.pixel(3,0) == (205, 203, 5): talents["CombusionBuff"] = 10 # > 5 sec duration
        elif sct_img.pixel(3,0) == (166, 166, 0): talents["CombusionBuff"] = 5 # <= 5 sec duration
        elif sct_img.pixel(3,0) == (104, 104, 0): talents["CombusionBuff"] = 1 # <= 1 sec duration
        else: talents["CombusionBuff"] = 0 # no buff
        if sct_img.pixel(4,0) == (255, 0, 14): talents["Rune"] = 1 # castable
        elif sct_img.pixel(4,0) == (207, 0, 0): talents["Rune"] = 2 # buff active
        elif sct_img.pixel(4,0) == (0, 255, 255): talents["Rune"] = 5 # 5 sec before cooldown
        else: talents["Rune"] = 0
        if sct_img.pixel(5,0) == (255, 0, 232): talents["FireBlast"] = 3
        elif sct_img.pixel(5,0) == (207, 0, 166): talents["FireBlast"] = 2
        elif sct_img.pixel(5,0) == (177, 0, 145): talents["FireBlast"] = 1
        else: talents["FireBlast"] = 0
        if sct_img.pixel(6,0) == (136, 0, 255): talents["Pyro"] = 3
        elif sct_img.pixel(6,0) == (113, 0, 211): talents["Pyro"] = 2
        elif sct_img.pixel(6,0) == (82, 0, 151): talents["Pyro"] = 1
        else: talents["Pyro"] = 0
        if sct_img.pixel(7,0) == (0, 6, 255): talents["Phoenix"] = 2
        elif sct_img.pixel(7,0) == (0, 26, 207): talents["Phoenix"] = 1
        else: talents["Phoenix"] = 0
        talents["Scorch"] = 1# if sct_img.pixel(9,0) == (15, 255, 0) else 0
        if sct_img.pixel(10,0) == (0, 255, 11): talents["Fireball"] = 2
        elif sct_img.pixel(10,0) == (0, 209, 9): talents["Fireball"] = 1
        else: talents["Fireball"] = 0
        talents["CounterSpell"] = 1 if sct_img.pixel(11,0) == (229, 255, 0) else 0
        if sct_img.pixel(12,0) == (181, 0, 8): talents["PyroclasmBuff"] = 1
        elif sct_img.pixel(12,0) == (255, 0, 11): talents["PyroclasmBuff"] = 2
        else: talents["PyroclasmBuff"] = 0
        talents["HotStreakBuff"] = 1 if sct_img.pixel(13,0) == (255, 0, 230) else 0
        talents["HeatingUpBuff"] = 1 if sct_img.pixel(14,0) == (166, 0, 255) else 0
        talents["CASTING"] = 1 if sct_img.pixel(15,0) == (0, 11, 255) else 0
        if sct_img.pixel(16,0) == (0, 255, 236): talents["EnemyHP"] = 2000000 #IF MORE THAN 2Mill hp (not small add)
        elif sct_img.pixel(16,0) == (0, 255, 200): talents["EnemyHP"] = 500000 #sane to cast pyroblast
        elif sct_img.pixel(16,0) == (0, 255, 180): talents["EnemyHP"] = 300000
        else: talents["EnemyHP"] = 0 #he deead
        talents["EnemyHP30%"] = 1 if sct_img.pixel(18,0) == (0, 191, 191) else 0 #IF less THAN 30% hp
        if sct_img.pixel(19,0) == (137, 0, 14):
            talents["AOECount"] = 2
        elif sct_img.pixel(19,0) == (178, 0, 14):
            talents["AOECount"] = 3
        elif sct_img.pixel(19,0) == (255, 0, 20):
            talents["AOECount"] = 5
        else: talents["AOECount"] = 0
        talents["PlayerMove"] = 1 if sct_img.pixel(20,0) == (0, 255, 10) else 0
        if sct_img.pixel(21,0) == (33, 255, 41): talents["SunKing"] = 8 #ready to activate
        elif sct_img.pixel(21,0) == (197, 0, 177): talents["SunKing"] = 7
        elif sct_img.pixel(21,0) == (143, 0, 129): talents["SunKing"] = 6
        elif sct_img.pixel(21,0) == (89, 0, 80): talents["SunKing"] = 5
        elif sct_img.pixel(21,0) == (64, 0, 58): talents["SunKing"] = 4
        else: talents["SunKing"] = 0
        if sct_img.pixel(22,0) == (0, 240, 255): talents["ShiftingPower"] = 1 #castable
        elif sct_img.pixel(22,0) == (0, 180, 191): talents["ShiftingPower"] = 2 #casting
        else: talents["ShiftingPower"] = 0
        talents["PyroclasmBuffExpiration"] = 1 if sct_img.pixel(23,0) == (255, 255, 0) else 0 #expiring in 4.5sec
        talents["DragonBreath"] = 1 if sct_img.pixel(24,0) == (255, 0, 255) else 0
        return talents

if __name__ == '__main__':
        talents = {
            "Canattack":0,
            "HP": 0, #30-,30+,60+,80+
            "TimeWarp":0,
            "Combustion": 0,
            "Rune": 0,
            "FireBlast": 0,
            "Pyro": 0,
            "Phoenix": 0,
            "Scorch": 0,
            "Fireball": 0,
            "CounterSpell": 0,
            "BLDebuff": 0,
            "CombusionBuff": 0,
            "PyroclasmBuff": 0, #2,3,5
            "HotStreakBuff": 0,
            "HeatingUpBuff": 0,
            "CASTING": 0,
            "EnemyHP": 0,
            "EnemyHP30%": 0,
            "AOECount": 0,
            "PlayerMove": 0,
            "SunKing": 0,
            "ShiftingPower": 0,
            "PyroclasmBuffExpiration": 0,
            "DragonBreath": 0,
        }
        monitor_number = 1
        monitor = {
                "top": 0+11,  # 100px from the top
                "left": 0+10,  # 100px from the left
                "width": 35,
                "height": 2,
                "mon": monitor_number,
            }
        ser = serial.Serial('COM6') # open serial
        throttle = 0
        key_modifier = False
        aoe_toggle = False
        with mss() as sct:
            while 'Looping':
                # time.sleep(0.5)
                # sct_img = sct.grab(monitor)
                # frame = np.array(sct_img, dtype=np.uint8)
                # img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                # scale_percent = 2600 # percent of original size
                # width = int(frame.shape[1] * scale_percent / 100)
                # height = int(frame.shape[0] * scale_percent / 100)
                # dim = (width, height)
                # resized = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
                # cv.putText(resized,'Press Q on this window to exit.', (int(scale_percent//100), 10), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
                # cv.putText(resized,'Each number corresponds to pixel number to be used in sct_img.pixel(i,0)', (int(scale_percent//100), 20), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
                # for i in range(0,img_gray.shape[1]):
                #     cv.putText(resized,str(i), (int(scale_percent//100*i), 50), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
                # get_data(sct_img,talents)
                # cv.imshow('Scaled pixel array', resized)
                # if cv.waitKey(25) & 0xFF == ord("q"):
                #         cv.destroyAllWindows()
                #         quit()
                # pass
                # try:
                #     if keyboard.is_pressed('shift+v'):
                #         print('shift+v')
                #         time.sleep(0.3)
                #     elif keyboard.is_pressed('shift+q'):
                #         print('shift+q')
                #         time.sleep(0.3)
                # except: break
                time.sleep(0.3)
                sct_img = sct.grab(monitor)
                # get_data(sct_img,talents)
                action(get_data(sct_img,talents))