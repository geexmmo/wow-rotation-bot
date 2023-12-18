import random
import re
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
    "RollTheBones":
        {'value': 0,'pixel': 14,'match': (255, 10, 0),'assign': 1},
    "SliceAndDice":
        {'value': 0,'pixel': 16,'match': (10, 255, 0),'assign': 1},
    "AdrenalinRush":
        {'value': 0,'pixel': 17,'match': (10, 0, 255),'assign': 1},
    "BetweenTheEyes":
        {'value': 0,'pixel': 18,'match': (255, 10, 0),'assign': 1},
    "Vanish":
        {'value': 0,'pixel': 20, 'multi': [
        {'match': (10, 255, 0),'assign': 1},
        {'match': (20, 255, 0),'assign': 2}]},
    "ShadowDance":
        {'value': 0,'pixel': 21,'match': (10, 0, 255),'assign': 1},
    "BladeFlurry":
        {'value': 0,'pixel': 22,'match': (255, 10, 0),'assign': 1},
    "GhostlyStrike":
        {'value': 0,'pixel': 24,'match': (10, 255, 0),'assign': 1},
    "PistolShot":
        {'value': 0,'pixel': 25,'match': (10, 0, 255),'assign': 1},
    "Dispatch":
        {'value': 0,'pixel': 26,'match': (255, 10, 0),'assign': 1},
    "Vial":
        {'value': 0,'pixel': 28,'match': (10, 255, 0),'assign': 1},
    "Ambush":
        {'value': 0,'pixel': 29,'match': (10, 0, 255),'assign': 1},
    "SinisterStrike":
        {'value': 0,'pixel': 30,'match': (255, 10, 0),'assign': 1},
    "CloakOfShadows":
        {'value': 0,'pixel': 32,'match': (10, 255, 0),'assign': 1},
    "Blind":
        {'value': 0,'pixel': 33,'match': (10, 0, 255),'assign': 1},
    "ShadowDanceB":
        {'value': 0,'pixel': 34, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 'expiring'}]},
    "SliceAndDiceB":
        {'value': 0,'pixel': 35, 'multi': [
        {'match': (10, 255, 0),'assign': 1},
        {'match': (20, 255, 0),'assign': 'expiring'}]},
    "BurstSoon":
        {'value': 0,'pixel': 37, 'multi': [
        {'match': (10, 0, 255),'assign': 1},
        {'match': (20, 0, 255),'assign': 'expiring'}]},
    "RollTheBonesB":
        # {'value': 0,'pixel': 38,'match': (255, 10, 0),'assign': 1},
        {'value': 0,'pixel': 38, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 2}]},
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
    "PistolShotB":
        {'value': 0,'pixel': 46,'match': (255, 10, 0),'assign': 1},
    "TrinketReady":
        {'value': 0,'pixel': 47,'match': (10, 255, 0),'assign': 1},
    "BetweenTheEyesHold":
        {'value': 0,'pixel': 49,'match': (10, 0, 255),'assign': 1},
    "BladeFlurryB":
        {'value': 0,'pixel': 50, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 'expiring'}]},
    "SubterfugeB":
        {'value': 0,'pixel': 51, 'multi': [
        {'match': (10, 255, 0),'assign': 1},
        {'match': (20, 255, 0),'assign': 'expiring'}]},
    "CanStealth":
        {'value': 0,'pixel': 52,'match': (10, 0, 255),'assign': 1},
    "RollTheBonesBonus":
        {'value': 0,'pixel': 54,'match': (255, 10, 0),'assign': 1},
    "BladeRush":
        {'value': 0,'pixel': 55,'match': (10, 255, 0),'assign': 1},
    }
    
def rotation(talents):
    # print('fuck', talents["TrinketReady"]['value'], (talents["AOECount"]['value'] >= 5 or (talents["EnemyHP%"]['value'] >= 10 and talents["EnemyHPCutoff"]['value'] >= 2000000 and SpecialStealhState)))
    rand = random.randint(0,3)
    SpecialStealhState = 1 if talents["SubterfugeB"]['value'] == 1 or talents["StealthB"]['value'] or talents["ShadowDanceB"]['value'] or talents["VanishB"]['value'] else 0
    if talents["CanStealth"]['value'] and not talents["VanishB"]['value']:
        if talents["BladeFlurry"]['value'] and talents["BladeFlurryB"]['value'] != 1: return('q')
        elif talents["AdrenalinRush"]['value']: return('v')
        elif talents["RollTheBones"]['value'] and (talents["RollTheBonesBonus"]['value'] and talents["RollTheBonesB"]['value'] <=2): return('t')
        elif talents["SliceAndDice"]['value'] and talents["SliceAndDiceB"]['value'] != 1 and talents["CP"]['value'] >=5: return('5')
        elif talents["CanStealth"]['value'] and not SpecialStealhState: return('x')
    elif talents["canattack"]['value'] and (not talents['Sap']['value'] or not talents['iscasting']['value']):
        # control and healz
        if talents["Kick"]['value'] and talents["EnemyCasting"]['value'] and not talents['ISmoving']['value']: return('l')
        elif talents["Shiv"]['value'] and talents["ENRAGED"]['value']: return('k')
        elif talents["Vial"]['value'] and talents["MyHP"]['value'] <= 50: return('z')
        # elif talents["TrinketReady"]['value'] and talents["MyHP"]['value'] <= 20: return('sft4') #throw trinket on low hp targets
        elif talents["TrinketReady"]['value'] and (talents["AOECount"]['value'] >= 5 or (talents["EnemyHP%"]['value'] >= 10 and talents["EnemyHPCutoff"]['value'] >= 2000000 and SpecialStealhState)): return('sft4') #throw trinket on low hp targets
        # elif talents["TrinketReady"]['value'] and (talents["EnemyHP%"]['value'] >= 10 or talents["ShadowDanceB"]['value']): return('sft4')
        # combat 2
        elif talents["Vanish"]['value'] and talents["BetweenTheEyes"]['value'] and not SpecialStealhState and talents["CP"]['value'] >= 7: return('c')
        elif talents["ShadowDance"]['value'] and talents["BetweenTheEyes"]['value'] and not SpecialStealhState and talents["CP"]['value'] >= 7: return('r')
        elif talents["SliceAndDice"]['value'] and talents["SliceAndDiceB"]['value'] != 1 \
            and not SpecialStealhState and talents["CP"]['value'] >= 5: return('5')
        match talents["CP"]['value']:
            case 0|2|3|4|5:
                if talents["BetweenTheEyes"]['value'] and SpecialStealhState and talents["CP"]['value'] >= 5: return('3')
                elif talents["AdrenalinRush"]['value'] and (talents["BurstSoon"]['value'] or talents["Energy"]['value'] <=50 ): return('v')
                elif talents["GhostlyStrike"]['value'] and talents["EnemyHP%"]['value'] >= 10 and talents["EnemyHPCutoff"]['value'] >= 2000000: return('j') #and talents["BurstSoon"]['value']
                elif talents["RollTheBones"]['value'] and (talents["RollTheBonesBonus"]['value'] and talents["RollTheBonesB"]['value'] <=2) \
                    and not SpecialStealhState: return('t')
                # elif talents["Ambush"]['value'] and talents["CP"]['value'] == 2 and talents["ShadowDanceB"]['value']: return('4')
                elif talents["BladeFlurry"]['value'] and talents["AOECount"]['value'] >= 2 and not SpecialStealhState: return('q')
                elif talents["BladeFlurry"]['value'] and talents["SliceAndDiceB"]['value'] and not talents["BladeFlurryB"]['value']: return('q')
                elif talents["BladeRush"]['value'] and talents["Energy"]['value'] <= 60 and not SpecialStealhState: return('6')
                # elif talents["Ambush"]['value'] and talents["BetweenTheEyesHold"]['value']: return('4')
                elif talents["Energy"]['value'] >= 80 or rand == 1:
                    if talents["SinisterStrike"]['value'] and not talents["PistolShotB"]['value'] and not SpecialStealhState: return('e')
                    elif talents["Ambush"]['value']: return('4')
                    elif talents["PistolShot"]['value'] and talents["PistolShotB"]['value']: return('1')
            case 6:
                if talents["BetweenTheEyes"]['value'] and SpecialStealhState: return('3')
                elif talents["BetweenTheEyes"]['value'] and not talents["BetweenTheEyesHold"]['value']: return('3')
                elif talents["Dispatch"]['value'] and not (talents["Vanish"]['value'] or talents["ShadowDance"]['value'] or SpecialStealhState): return('2')
                elif talents["BladeFlurry"]['value']: return('q')
                elif talents["SinisterStrike"]['value'] and not talents["PistolShotB"]['value']: return('e')
                elif talents["PistolShot"]['value'] and talents["PistolShotB"]['value']: return('1')
            case 7:
                if talents["BetweenTheEyes"]['value'] and SpecialStealhState: return('3')
                elif talents["BetweenTheEyes"]['value'] and not talents["BetweenTheEyesHold"]['value']: return('3')
                elif talents["Dispatch"]['value'] and (not SpecialStealhState or not talents["BetweenTheEyes"]['value']): return('2')