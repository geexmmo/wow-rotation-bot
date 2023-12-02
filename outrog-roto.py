from mss import mss
import cv2 as cv
import numpy as np
import time
import serial
# from pynput import keyboard
import keyboard

def handle_input(name: str, key_type=None):
    if key_type:
        ser.write(str.encode(key_type))

def action(talents: dict):
    # pass
    #talents[""]
    if aoe_toggle: print('ENG:',talents["Energy"],'AOE TOGGLE: ', f'{aoe_toggle}'*60, sep='\t')
    else: print('ENG:',talents["Energy"],'AOE TOGGLE: ', f'{aoe_toggle}', sep='\t')
    if talents["Canattack"]:
        match talents["Combopoints"]:
            #prepull
            case 0:
                if not talents["SkullB"] and talents["Roll the Bones"]: handle_input('Roll the Bones', 'r')
                if aoe_toggle and talents["Blade Flurry"]: handle_input('Blade Flurry', 'q')
                if talents["Ardernaline Rush"]: handle_input('Ardernaline Rush', 'e')
                if not talents["Slice and DiceB"] and talents["Slice and Dice"]: handle_input('Slice and Dice', 'j')
                if talents["Ambush"]: handle_input('', '4')
                if talents["OpportunityB"] and talents["Pistol Shot"]: handle_input('', '1')
                if talents["BladeFlurryB"] and talents["Blade Rush"]: handle_input('', '6')
                if talents["Sinister Strike"]: handle_input('', '4')
                if talents["Energy"] == 30 and talents["Blade Rush"]: handle_input('', '6')
            case 3: #-3
                if aoe_toggle and talents["Blade Flurry"]: handle_input('Blade Flurry', 'q')
                if not talents["SkullB"] and talents["Roll the Bones"]: handle_input('Roll the Bones', 'r')
                if talents["Ambush"]: handle_input('', '5')
                if talents["OpportunityB"] and talents["Pistol Shot"]: handle_input('', '1')
                if talents["Energy"] == 30 and talents["Blade Rush"]: handle_input('', '6')
                if talents["Shadow Dance"]: handle_input('', 's')
                if talents["Sinister Strike"]: handle_input('', '4')
                if not talents["Slice and DiceB"] and talents["Slice and Dice"]: handle_input('Slice and Dice', 'j')
            case 4: #-3
                if talents["Ambush"]: handle_input('', '5')
                if talents["Energy"] != 70 and talents["Blade Rush"]: handle_input('', '6')
                if talents["OpportunityB"] and talents["Pistol Shot"]: handle_input('', '1')
                if talents["Shadow Dance"]: handle_input('', 's')
                if not talents["Slice and DiceB"] and talents["Slice and Dice"]: handle_input('Slice and Dice', 'j')
                if talents["Sinister Strike"]: handle_input('', '4')
            case 5: #-3
                # if not talents["SkullB"] and talents["Ambush"]: handle_input('', '5')
                if talents["OpportunityB"] and talents["Pistol Shot"]: handle_input('', '1')
                if talents["Shadow Dance"]: handle_input('', 's')
                if talents["Sinister Strike"]: handle_input('', '4')
            case 6: #-3
                if talents["Sinister Strike"]: handle_input('', '4')
            case 7: #-3
                if talents["Cold blood"] and talents["Between the Eyes"]: handle_input('', 'v')
                if talents["Between the Eyes"]: handle_input('', '2')
                if talents["Dispatch"]: handle_input('', '3')
                if talents["Slice and Dice"] and not talents["Slice and DiceB"]: handle_input('', 'j')
    elif talents["Canattack"]:
        pass

def get_data(sct_img,talents: dict):
        p1 = sct_img.pixel(0,0) # HP
        if p1 == (238, 242, 0): talents["HP"] = 80
        elif p1 == (134,135,0): talents["HP"] = 60
        elif p1 == (72,68,0): talents["HP"] = 30
        else: talents["HP"] = 0
        p2 = sct_img.pixel(1,0) #CP
        if p2 == (255, 244, 0): talents["Combopoints"] = 7
        elif p2 == (222, 225, 0): talents["Combopoints"] = 6
        elif p2 == (191, 183, 16): talents["Combopoints"] = 5
        elif p2 == (129, 118, 10): talents["Combopoints"] = 4
        else: talents["Combopoints"] = 0
        p3 = sct_img.pixel(2,0)
        if p3 == (115, 0, 89): talents["Energy"] = 90
        elif p3 == (70, 24, 67): talents["Energy"] = 70
        elif p3 == (48, 16, 43): talents["Energy"] = 50
        elif p3 == (32, 3, 33): talents["Energy"] = 30
        else: talents["Energy"] = 0
        talents["Canattack"] = 1 if sct_img.pixel(3,0) == (255, 141, 120) else 0
        talents["Roll the Bones"] = 1 if sct_img.pixel(4,0) == (62, 255, 0) else 0
        talents["Slice and Dice"] = 1 if sct_img.pixel(6,0) == (255, 250, 0) else 0
        talents["Cold blood"] = 1 if sct_img.pixel(7,0) == (2, 255, 184) else 0
        talents["Ardernaline Rush"] = 1 if sct_img.pixel(8,0) == (0, 255, 81) else 0
        talents["Vanish"] = 1 if sct_img.pixel(10,0) == (68, 4, 255) else 0
        talents["Shadow Dance"] = 1 if sct_img.pixel(11,0) == (68, 4, 255) else 0
        talents["Between the Eyes"] = 1 if sct_img.pixel(12,0) == (12, 215, 255) else 0
        talents["Ambush"] = 1 if sct_img.pixel(13,0) == (0, 58, 255) else 0
        talents["Dispatch"] = 1 if sct_img.pixel(15,0) == (11, 168, 255) else 0
        talents["Pistol Shot"] = 1 if sct_img.pixel(16,0) == (255, 230, 0) else 0 #no cd care
        talents["Sinister Strike"] = 1 if sct_img.pixel(17,0) == (255, 0, 31) else 0
        # print(sct_img.pixel(17,0))
        talents["Blade Rush"] = 1 if sct_img.pixel(18,0) == (0, 255, 5) else 0
        talents["Blade Flurry"] = 1 if sct_img.pixel(19,0) == (245, 0, 255) else 0
        #Buffs
        talents["OpportunityB"] = 1 if sct_img.pixel(21,0) == (0, 58, 255) else 0
        talents["BladeFlurryB"] = 1 if sct_img.pixel(22,0) == (90, 158, 255) else 0
        talents["ShadowDanceB"] = 1 if sct_img.pixel(23,0) == (121, 249, 255) else 0
        talents["Slice and DiceB"] = 1 if sct_img.pixel(25,0) == (190, 255, 8) else 0
        talents["SkullB"] = 1 if sct_img.pixel(26,0) == (255, 0, 14) else 0
        return talents

if __name__ == '__main__':
        talents = {
            "HP":0, #30-,30+,60+,80+
            "Combopoints": 0, #<3=0, 4,5,6,7
            "Energy": 0, #<=30=0, 30+,50+,70+,90+
            "Canattack": 0,
            "Roll the Bones": 0,
            "Slice and Dice": 0,
            "Cold blood": 0,
            "Ardernaline Rush" : 0,
            "Vanish": 0,
            "Shadow Dance": 0,
            "Between the Eyes": 0,
            "Ambush": 0,
            "Dispatch": 0,
            "Pistol Shot": 0,
            "Sinister Strike": 0,
            "Blade Rush": 0,
            "Blade Flurry": 0,
            "OpportunityB": 0,
            "BladeFlurryB": 0,
            "ShadowDanceB": 0,
            "Slice and DiceB": 0,
            "SkullB": 0,
            "Незаметность": 0,
            "Исчезновение": 0,
            "Увертка": 0
        }
        monitor_number = 1
        monitor = {
                "top": 0+20,  # 100px from the top
                "left": 0+30,  # 100px from the left
                "width": 30,
                "height": 1,
                "mon": monitor_number,
            }
        ser = serial.Serial('COM6') # open serial
        throttle = 0
        key_modifier = False
        aoe_toggle = False
        with mss() as sct:
            while 'Looping':
                time.sleep(0.2)
                # sct_img = sct.grab(monitor)
                # frame = np.array(sct_img, dtype=np.uint8)
                # img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                # scale_percent = 2600 # percent of original size
                # width = int(frame.shape[1] * scale_percent / 100)
                # height = int(frame.shape[0] * scale_percent / 100)
                # dim = (width, height)
                # resized = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
                # get_data(sct_img,talents)
                # cv.imshow('Test', resized)
                # get_data(sct_img,talents)
                # if cv.waitKey(25) & 0xFF == ord("q"):
                #         cv.destroyAllWindows()
                #         quit()
                # pass
                try:  # used try so that if user pressed other than the given key error will not be shown
                    if keyboard.is_pressed('shift+z'):
                        print('You Pressed shift+z Key!')
                        time.sleep(0.4)
                    if keyboard.is_pressed('q'):
                        print('You Pressed Q Key!')
                        aoe_toggle = not aoe_toggle
                        time.sleep(0.4)
                except: break
                time.sleep(0.2)
                sct_img = sct.grab(monitor)
                action(get_data(sct_img,talents))