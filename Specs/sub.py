import random
talents = {
    'canattack':
        {'value': 0,'pixel': 0,'match': (255,141,120),'assign': 1},
    "AOECount":
        {'value': 0,'pixel': 1, 'multi': [
        {'match': (20,0,255),'assign': 2},
        {'match': (30,0,255),'assign': 3},
        {'match': (40,0,255),'assign': 4},
        {'match': (50,0,255),'assign': 5},
        {'match': (60,0,255),'assign': 6},
        {'match': (70,0,255),'assign': 7},
        {'match': (80,0,255),'assign': 8}]},
    'iscasting':
        {'value': 0,'pixel': 3,'match': (255,10,0),'assign': 1},
    "EnemyHPCutoff":
        {'value': 0,'pixel': 4, 'multi': [
        {'match': (10,255,0),'assign': 500000},
        {'match': (20,255,0),'assign': 1000000}, #1m
        {'match': (30,255,0),'assign': 2000000}, #2m
        {'match': (40,255,0),'assign': 10000000},]}, #10m
    "Energy":
        {'value': 0,'pixel': 5, 'multi': [
        {'match': (0,30,255),'assign': 30},
        {'match': (0,40,255),'assign': 40},
        {'match': (0,50,255),'assign': 50},
        {'match': (0,60,255),'assign': 60},
        {'match': (0,70,255),'assign': 70},
        {'match': (0,80,255),'assign': 80},
        {'match': (0,90,255),'assign': 90},]},
    "EnemyHP%":
        {'value': 0,'pixel': 7, 'multi': [
        {'match': (255,100,0),'assign': 100},
        {'match': (255,90,0),'assign': 90},
        {'match': (255,80,0),'assign': 80},
        {'match': (255,70,0),'assign': 70},
        {'match': (255,60,0),'assign': 60},
        {'match': (255,50,0),'assign': 50},
        {'match': (255,40,0),'assign': 40},
        {'match': (255,30,0),'assign': 30},
        {'match': (255,20,0),'assign': 20},
        {'match': (255,10,0),'assign': 10},
        {'match': (255,1,0),'assign': 1}]},
    "EnemyCasting":
        {'value': 0,'pixel': 8,'match': (10, 255, 0),'assign': 1},
    "ISmoving":
        {'value': 0,'pixel': 9,'match': (10, 255, 255),'assign': 1},
    "MyHP":
        {'value': 0,'pixel': 11, 'multi': [
        {'match': (255,100,0),'assign': 100},
        {'match': (255,90,0),'assign': 90},
        {'match': (255,80,0),'assign': 80},
        {'match': (255,70,0),'assign': 70},
        {'match': (255,60,0),'assign': 60},
        {'match': (255,50,0),'assign': 50},
        {'match': (255,40,0),'assign': 40},
        {'match': (255,30,0),'assign': 30},
        {'match': (255,20,0),'assign': 20},
        {'match': (255,10,0),'assign': 10}]},
    "CP":
        {'value': 0,'pixel': 12, 'multi': [
        {'match': (20,255,0),'assign': 2},
        {'match': (30,255,0),'assign': 3},
        {'match': (40,255,0),'assign': 4},
        {'match': (50,255,0),'assign': 5},
        {'match': (60,255,0),'assign': 6},
        {'match': (70,255,0),'assign': 7},]},
    "ENRAGED":
        {'value': 0,'pixel': 13,'match': (10, 0, 255),'assign': 1},
    "Shadow Blades":
        {'value': 0,'pixel': 14,'match': (255, 10, 0),'assign': 1},
    "Slice and Dice":
        {'value': 0,'pixel': 16,'match': (10, 255, 0),'assign': 1},
    "Symbols of Death":
        {'value': 0,'pixel': 17,'match': (10, 0, 255),'assign': 1},
    "Rapture":
        {'value': 0,'pixel': 18,'match': (255, 10, 0),'assign': 1},
    "Vanish":
        {'value': 0,'pixel': 20, 'multi': [
        {'match': (10, 255, 0),'assign': 1},
        {'match': (20, 255, 0),'assign': 2}]},
    "Shadow Dance":
        {'value': 0,'pixel': 21,'match': (10, 0, 255),'assign': 1},
    "Thistle Tea":
        {'value': 0,'pixel': 22, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 2},
        {'match': (255, 30, 0),'assign': 3}]},
    "Secret Technique":
        {'value': 0,'pixel': 24,'match': (10, 255, 0),'assign': 1},
    "Cold Blood":
        {'value': 0,'pixel': 25,'match': (10, 0, 255),'assign': 1},
    "Eviscerate":
        {'value': 0,'pixel': 26,'match': (255, 10, 0),'assign': 1},
    "Vial":
        {'value': 0,'pixel': 28,'match': (10, 255, 0),'assign': 1},
    "Shadowstrike":
        {'value': 0,'pixel': 29,'match': (10, 0, 255),'assign': 1},
    "Gloomblade|Backstab":
        {'value': 0,'pixel': 30,'match': (255, 10, 0),'assign': 1},
    "Black Powder":
        {'value': 0,'pixel': 32,'match': (10, 255, 0),'assign': 1},
    "Shuriken Storm":
        {'value': 0,'pixel': 33,'match': (10, 0, 255),'assign': 1},
    "ShadowDanceB":
        {'value': 0,'pixel': 34, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 'expiring'}]},
    "Slice and DiceB":
        {'value': 0,'pixel': 35, 'multi': [
        {'match': (10, 255, 0),'assign': 1},
        {'match': (20, 255, 0),'assign': 'expiring'}]},
    "RaptureB":
        {'value': 0,'pixel': 37, 'multi': [
        {'match': (10, 0, 255),'assign': 1},
        {'match': (20, 0, 255),'assign': 'expiring'}]},
    "ShurikenTornado":
        {'value': 0,'pixel': 38,'match': (255, 10, 0),'assign': 1},
    "Shiv":
        {'value': 0,'pixel': 39,'match': (10, 255, 0),'assign': 1},
    "VanishB":
        {'value': 0,'pixel': 41,'match': (10, 0, 255),'assign': 1},
    "StealthB":
        {'value': 0,'pixel': 42,'match': (255, 10, 0),'assign': 1},
    "Kick":
        {'value': 0,'pixel': 43,'match': (10, 255, 0),'assign': 1},
    "Sap":
        {'value': 0,'pixel': 45,'match': (10, 0, 255),'assign': 1},
    "SoDBuff":
        {'value': 0,'pixel': 46,'match': (255, 10, 0),'assign': 1},
    "TrinketReady":
        {'value': 0,'pixel': 47,'match': (10, 255, 0),'assign': 1},
    "FLAGGEL":
        {'value': 0,'pixel': 48,'match': (10, 0, 255),'assign': 1},
    }
    
def rotation(talents):
    # print('SthB: ',talents["StealthB"]['value'] ,'van b: ',talents["VanishB"]['value'], 'GB:', talents["Gloomblade|Backstab"]['value'], 'EneRg:', talents["Energy"]['value'])
    rand = random.randint(0,2)
    if talents["canattack"]['value'] and not talents['Sap']['value']:
        if talents["EnemyCasting"]['value'] and talents["Kick"]['value'] and not talents['ISmoving']['value']: return('l')
        elif talents["ENRAGED"]['value'] and talents["Shiv"]['value']: return('k')
        elif talents["MyHP"]['value'] <= 50 and talents["Vial"]['value']: return('z')
        elif talents["TrinketReady"]['value'] and (talents["EnemyHP%"]['value'] <= 10 or talents["ShadowDanceB"]['value']): return('sft4') #throw trinket on low hp targets
        match talents["CP"]['value']:
            case 0|2|3|4:
                # print('0-4cp')
                if talents["ShadowDanceB"]['value'] != 0:
                    if talents["Symbols of Death"]['value'] and not talents["SoDBuff"]['value']: return('j')
                    elif talents["Shadow Blades"]['value'] and talents["AOECount"]['value'] <= 3: return('v')
                    elif talents["Energy"]['value'] <= 30 and talents["Thistle Tea"]['value'] !=0: return('s')
                    elif talents["ShurikenTornado"]['value'] and talents["AOECount"]['value'] >= 3: return('f')
                    elif talents["AOECount"]['value'] >= 3 and talents["Shuriken Storm"]['value']: return('q')
                    elif talents["Vanish"]['value'] == 2 and talents["Shadowstrike"]['value']: return('c') #vanish
                    elif talents["Shadowstrike"]['value']: return('5')
                else:
                    if talents["AOECount"]['value'] >= 3 and talents["FLAGGEL"]['value']: return('sft1')
                    elif talents["ShurikenTornado"]['value'] and talents["AOECount"]['value'] >= 3: return('f')
                    elif talents["AOECount"]['value'] >= 3 and talents["Shuriken Storm"]['value']: return('q')
                    elif talents["Energy"]['value'] <= 30 and talents["Thistle Tea"]['value'] >= 2: return('s')
                    # elif talents["Vanish"]['value'] == 1 and talents["ShadowDanceB"]['value'] == 'expiring': return('c') #vanish on shadowdance ending and low cp
                    elif not talents["StealthB"]['value'] and not talents["VanishB"]['value'] and talents["Gloomblade|Backstab"]['value']: 
                        if talents["Energy"]['value'] >= 70:
                            return('e')
                        elif rand == 1:
                            return('e')
                    elif talents["Shadowstrike"]['value']: return('5')
            case 5:
                match talents["ShadowDanceB"]['value']:
                    case 1:
                        if talents["RaptureB"]['value'] != 1 and talents["EnemyHPCutoff"]['value'] >= 1000000 and talents["Rapture"]['value']: return('3')
                        elif talents["AOECount"]['value'] >= 2 and talents["Black Powder"]['value']: return('4')
                        elif talents["Eviscerate"]['value']: return('1')
                        elif talents["Shadowstrike"]['value']: return('5')
                    case 'expiring':
                        if talents["Energy"]['value'] >= 50 and talents["Gloomblade|Backstab"]['value']: return('e')
                        elif talents["Shadowstrike"]['value']: return('5')
                    case _:
                        if talents["RaptureB"]['value'] != 1 and talents["EnemyHP%"]['value'] >= 30 and talents["Rapture"]['value']: return('3')
                        elif talents["Slice and DiceB"]['value'] != 1 and talents["AOECount"]['value'] != 4 and talents["Slice and Dice"]['value']: return('6')
                        elif not talents["StealthB"]['value'] and not talents["VanishB"]['value'] and talents["Gloomblade|Backstab"]['value'] and talents["Energy"]['value'] >= 50: return('e')
                        elif talents["Shadowstrike"]['value']: return('5')
                        elif talents["Eviscerate"]['value']: return('1')
            case 6:
                match talents["ShadowDanceB"]['value']:
                    case 1:
                        if talents["RaptureB"]['value'] != 1 and talents["EnemyHPCutoff"]['value'] >= 1000000 and talents["EnemyHP%"]['value'] >= 30 and talents["Rapture"]['value']: return('3')
                        elif talents["AOECount"]['value'] >= 2 and talents["Black Powder"]['value']: return('4')
                        elif talents["Eviscerate"]['value']: return('1')
                        elif talents["Shadowstrike"]['value']: return('5')
                    case 'expiring':
                        if talents["CP"]['value'] >= 6 and talents["Secret Technique"]['value']:
                            if talents["Cold Blood"]['value']: return('y') #Cold Blood
                            return('2') #Secret Technique
                        elif talents["Energy"]['value'] >= 50 and talents["Gloomblade|Backstab"]['value']:
                            return('e')
                        elif talents["Shadowstrike"]['value']:
                            return('5')
                    case _:
                        if talents["RaptureB"]['value'] != 1 and talents["EnemyHP%"]['value'] >= 30 and talents["EnemyHPCutoff"]['value'] >= 1000000 and talents["Rapture"]['value']: return('3')
                        elif talents["AOECount"]['value'] >= 3 and talents["Black Powder"]['value']: return('4')
                        elif talents["Eviscerate"]['value']: return('1')
            case 7: #-3
                # print('7cp')
                match talents["ShadowDanceB"]['value']:
                    case 1:
                        if talents["RaptureB"]['value'] != 1 and talents["EnemyHP%"]['value'] >= 30 and talents["EnemyHPCutoff"]['value'] >= 1000000 and talents["Rapture"]['value']: return('3')
                        elif talents["AOECount"]['value'] >= 2 and talents["Black Powder"]['value']: return('4')
                        elif talents["Eviscerate"]['value']: return('1')
                        # elif talents["Shadowstrike"]['value']: return('5')
                    case 'expiring':
                        if talents["CP"]['value'] >= 6 and talents["Secret Technique"]['value']:
                            if talents["Cold Blood"]['value']: return('y') #Cold Blood
                            return('2') #Secret Technique
                        elif talents["Eviscerate"]['value']: return('1')
                    case _:
                        if talents["RaptureB"]['value'] != 1 and talents["EnemyHP%"]['value'] >= 30 and talents["Rapture"]['value']: return('3')
                        elif talents["EnemyHP%"]['value'] >= 30 and talents["EnemyHPCutoff"]['value'] >= 2000000 and talents["Shadow Dance"]['value'] and (
                            talents["Thistle Tea"]['value'] >= 1 or talents["Symbols of Death"]['value']):
                            return('r')
                        elif talents["AOECount"]['value'] >= 3 and talents["Black Powder"]['value']: return('4')
                        elif talents["Eviscerate"]['value']: return('1')