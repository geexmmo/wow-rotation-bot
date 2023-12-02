talents = {
    "MyHP":
        {'value': 0,'pixel': 0, 'multi': [
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
    'canattack':
        {'value': 0,'pixel': 1,'match': (255,141,120),'assign': 1},
    "ISmoving":
        {'value': 0,'pixel': 3,'match': (10, 255, 255),'assign': 1},
    "EnemyHP%":
        {'value': 0,'pixel': 4, 'multi': [
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
        {'value': 0,'pixel': 5,'match': (10, 255, 0),'assign': 1},
    "AOECount":
        {'value': 0,'pixel': 7, 'multi': [
        {'match': (20,0,255),'assign': 2},
        {'match': (30,0,255),'assign': 3},
        {'match': (40,0,255),'assign': 4},
        {'match': (50,0,255),'assign': 5},
        {'match': (60,0,255),'assign': 6},
        {'match': (70,0,255),'assign': 7},
        {'match': (80,0,255),'assign': 8}]},
    'IScasting':
        {'value': 0,'pixel': 8,'match': (255,10,0),'assign': 1},
    "EnemyHPCutoff":
        {'value': 0,'pixel': 9, 'multi': [
        {'match': (10,255,0),'assign': 500000},
        {'match': (20,255,0),'assign': 1000000}, #1m
        {'match': (30,255,0),'assign': 2000000}, #2m
        {'match': (40,255,0),'assign': 10000000},]}, #10m
    "BloodLust":
        {'value': 0,'pixel': 11,'match': (10, 0, 255),'assign': 1},
    "Startsurge":
        {'value': 0,'pixel': 12,'match': (255, 10, 0),'assign': 1},
    "Sunfire":
        {'value': 0,'pixel': 13,'match': (10, 255, 0),'assign': 1},
    "Moonfire":
        {'value': 0,'pixel': 14,'match': (10, 0, 255),'assign': 1},
    "Wrath":
        {'value': 0,'pixel': 16,'match': (255, 10, 0),'assign': 1},
    "Starfall":
        {'value': 0,'pixel': 17,'match': (10, 255, 0),'assign': 1},
    "StarfallBuff":
        {'value': 0,'pixel': 18, 'multi': [
        {'match': (10, 0, 255),'assign': 1},
        {'match': (20, 0, 255),'assign': 2},]},
    "LunarEclipseBuff":
        {'value': 0,'pixel': 20,'match': (255, 10, 0),'assign': 1},
    "SloarBeam":
        {'value': 0,'pixel': 21,'match': (10, 255, 0),'assign': 1},
    "ChosenOfElune":
        {'value': 0,'pixel': 22,'match': (10, 0, 255),'assign': 1},
    "ChosenOfEluneBuff":
        {'value': 0,'pixel': 24,'match': (255, 10, 0),'assign': 1},
    "StellarDebuff":
        {'value': 0,'pixel': 25,'match': (10, 255, 0),'assign': 1},
    "SolarEclipseBuff":
        {'value': 0,'pixel': 26,'match': (10, 0, 255),'assign': 1},
    "SunfireDebuff":
        {'value': 0,'pixel': 28, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 'expiring'},]},
    "FreeStarfallBuff":
        {'value': 0,'pixel': 29,'match': (10, 255, 0),'assign': 1},
    "FreeStartsurgeBuff":
        {'value': 0,'pixel': 30,'match': (10, 0, 255),'assign': 1},
    "MoonfireDebuff":
        {'value': 0,'pixel': 32, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 'expiring'},]},
    "Starfire":
        {'value': 0,'pixel': 33,'match': (10, 255, 0),'assign': 1},
    "FreeMoonfireBuff":
        {'value': 0,'pixel': 34,'match': (10, 0, 255),'assign': 1},
    "FuryOfElune":
        {'value': 0,'pixel': 35,'match': (255, 10, 0),'assign': 1},
    "PulsarProcSoon":
        {'value': 0,'pixel': 37,'match': (10, 255, 0),'assign': 1},
    "TriketReady":
        {'value': 0,'pixel': 38,'match': (255, 10, 0),'assign': 1},
    }
    
def rotation(talents):
    # print('Moonfire',talents["Moonfire"]['value'],'MoonfireDebuff',talents["MoonfireDebuff"]['value'],'EnemyHPCutoff',talents["EnemyHPCutoff"]['value'],'EnemyHP%',talents["EnemyHP%"]['value'])
    print('AOE: ', talents["AOECount"]['value'], talents["LunarEclipseBuff"]['value'])
    # TODO
    # count Chosen proc buffs so i wont be spending talents["ChosenOfElune"]['value'] when it will be free in close time
    # mouseover roots
    # mouseover
    if talents["canattack"]['value']:
        # always available casts and interrupts
        if talents["EnemyCasting"]['value'] and talents["SloarBeam"]['value']: return 'l' #interrupt
        elif not talents["ChosenOfEluneBuff"]['value'] and talents["ChosenOfElune"]['value'] \
            and not talents["PulsarProcSoon"]['value'] and talents["EnemyHPCutoff"]['value'] >= 2000000 and talents["EnemyHP%"]['value'] >= 30: return 'r'
        elif talents["FuryOfElune"]['value'] and talents["EnemyHPCutoff"]['value'] >= 2000000 and talents["EnemyHP%"]['value'] <= 10: return 'x'
        elif talents["Sunfire"]['value'] and talents["SunfireDebuff"]['value'] != 1 and not talents["EnemyHP%"]['value'] <= 10: return '2'
        elif talents["Moonfire"]['value'] and talents["MoonfireDebuff"]['value'] != 1 and not talents["EnemyHP%"]['value'] <= 10: return '1'
        elif talents["TriketReady"]['value'] and talents["ChosenOfEluneBuff"]['value']: return 'sft4'
        # movement
        elif talents["ISmoving"]['value']:
            if talents["Starfall"]['value'] and talents["StarfallBuff"]['value'] <= 2: return '5'
            elif talents["Startsurge"]['value'] and talents["FreeStartsurgeBuff"]['value']: return '6'
        elif not talents["ISmoving"]['value'] and not talents["IScasting"]['value']:
            if talents["AOECount"]['value'] >= 3:
                if talents["Starfall"]['value'] and talents["StarfallBuff"]['value'] < 2: return '5'
                elif talents["Startsurge"]['value'] and talents["FreeStartsurgeBuff"]['value']: return '6'
                elif talents["ChosenOfEluneBuff"]['value']: return '3'
                elif talents["Wrath"]['value'] and not talents["LunarEclipseBuff"]['value']: return '4'
                elif talents["Starfire"]['value']: return '3'
            else:
                if talents["Startsurge"]['value']: return '6'
                elif talents["Starfall"]['value'] and talents["FreeStarfallBuff"]['value'] and talents["StarfallBuff"]['value'] <= 2: return '5'
                elif talents["ChosenOfEluneBuff"]['value']: return '4'
                elif talents["Starfire"]['value'] and not talents["SolarEclipseBuff"]['value']: return '3'
                elif talents["Wrath"]['value']: return '4'