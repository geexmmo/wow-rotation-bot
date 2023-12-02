import time
talents = {
    'canattack':
        {'value': 0,'pixel': 0,'match': (255,141,120),'assign': 1},
    "ISmoving":
        {'value': 0,'pixel': 1, 'multi': [
        {'match': (10, 255, 255),'assign': 1},
        {'match': (20, 255, 255),'assign': 2}]},
    "MyHP":
        {'value': 0,'pixel': 2, 'multi': [
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
    "EnemyCasting":
        {'value': 0,'pixel': 3,'match': (10, 255, 0),'assign': 1},
    "Insanity":
        {'value': 0,'pixel': 5, 'multi': [
        {'match': (0,20,255),'assign': 20},
        {'match': (0,45,255),'assign': 45},
        {'match': (0,60,255),'assign': 60},
        {'match': (0,80,255),'assign': 80},
        {'match': (0,100,255),'assign': 100},
        {'match': (0,120,255),'assign': 120},
        {'match': (0,130,255),'assign': 130},
        {'match': (0,150,255),'assign': 150},]},
    "EnemyHP%":
        {'value': 0,'pixel': 6, 'multi': [
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
    "EnemyHPCutoff":
        {'value': 0,'pixel': 7, 'multi': [
        {'match': (10,255,0),'assign': 500000},
        {'match': (20,255,0),'assign': 1000000}, #1m
        {'match': (30,255,0),'assign': 2000000}, #2m
        {'match': (40,255,0),'assign': 10000000},]}, #10m
    "AOECount":
        {'value': 0,'pixel': 8, 'multi': [
        {'match': (20,0,255),'assign': 2},
        {'match': (30,0,255),'assign': 3},
        {'match': (40,0,255),'assign': 4},
        {'match': (50,0,255),'assign': 5},
        {'match': (60,0,255),'assign': 6},
        {'match': (70,0,255),'assign': 7},
        {'match': (80,0,255),'assign': 8}]},
    'IScasting':
        {'value': 0,'pixel': 10,'match': (255,10,0),'assign': 1},
    "vapiric":
        {'value': 0,'pixel': 11, 'multi': [
        {'match': (10, 255, 0),'assign': 1},
        {'match': (20, 255, 0),'assign': 0}]}, #checking if casted because dots can be applied after data retrieval resulting in duplicate casts
    "SWP":
        {'value': 0,'pixel': 12,'match': (10, 0, 255),'assign': 1},
    "shadowcrash":
        {'value': 0,'pixel': 13, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 2}]},
    "dplague":
        {'value': 0,'pixel': 15,'match': (10, 255, 0),'assign': 1},
    "mindblast":
        {'value': 0,'pixel': 16, 'multi': [
        {'match': (10, 0, 255),'assign': 1},
        {'match': (20, 0, 255),'assign': 2}]},
    "voidbolt":
        {'value': 0,'pixel': 17, 'multi': [
        {'match': (255, 10, 0),'assign': 1},
        {'match': (255, 20, 0),'assign': 2}]},
    "surgeOfinsanity":
        {'value': 0,'pixel': 18,'match': (10, 255, 0),'assign': 1},
    "SWD":
        {'value': 0,'pixel': 20,'match': (10, 0, 255),'assign': 1},
    "Shadowfiend":
        {'value': 0,'pixel': 21,'match': (255, 10, 0),'assign': 1},
    "voiderruption":
        {'value': 0,'pixel': 22,'match': (10, 255, 0),'assign': 1},
    "voidformbuff":
        {'value': 0,'pixel': 23,'match': (10, 0, 255),'assign': 1},
    "voidtorrent":
        {'value': 0,'pixel': 25,'match': (255, 10, 0),'assign': 1},
    "mindgames":
        {'value': 0,'pixel': 26,'match': (10, 255, 0),'assign': 1},
    "halo":
        {'value': 0,'pixel': 27,'match': (10, 0, 255),'assign': 1},
    "mindflay":
        {'value': 0,'pixel': 28,'match': (255, 10, 0),'assign': 1},
    "vampiric.debuff":
        {'value': 0,'pixel': 30, 'multi': [
        {'match': (10, 255, 0),'assign': 1},
        {'match': (20, 255, 0),'assign': 'expiring'}]},
    "SWP.debuff":
        {'value': 0,'pixel': 31, 'multi': [
        {'match': (10, 0, 255),'assign': 1},
        {'match': (20, 0, 255),'assign': 'expiring'}]},
    "dplague.debuff":
        {'value': 0,'pixel': 32,'match': (255, 10, 0),'assign': 1},
    "instamindblast":
        {'value': 0,'pixel': 33,'match': (10, 255, 0),'assign': 1},
    "PWS":
        {'value': 0,'pixel': 35,'match': (10, 0, 255),'assign': 1},
    "AngelicFeather":
        {'value': 0,'pixel': 36,'match': (255, 10, 0),'assign': 1},
    "SPEEDBUFF":
        {'value': 0,'pixel': 37,'match': (10, 255, 0),'assign': 1},
    "Silence":
        {'value': 0,'pixel': 38,'match': (10, 0, 255),'assign': 1},
    "Dispel":
        {'value': 0,'pixel': 40,'match': (255, 10, 0),'assign': 1},
    "Dispellable":
        {'value': 0,'pixel': 41,'match': (10, 255, 0),'assign': 1},
    "special-casts":
        {'value': 0,'pixel': 42,'match': (10, 0, 255),'assign': 1}, #casts that should not be interrupted
    }
    
def rotation(talents):
    if talents["canattack"]['value'] and talents["ISmoving"]['value'] == 0:
        # interrupt casting
        if talents["voidbolt"]['value']: return 'f'
        # don't interrupt
        elif not talents["IScasting"]['value'] or not talents["special-casts"]['value']:
            #voiderruption
            if talents["voiderruption"]['value'] and not talents["voidformbuff"]['value'] \
                and talents["mindblast"]['value'] == 0 and talents["Insanity"]['value'] >= 70\
                and not talents["voidtorrent"]['value'] and not talents["EnemyHP%"]['value'] <= 10 \
                    and talents["EnemyHPCutoff"]['value'] >= 2000000: return 'r'
            #!voiderruption
            elif talents["EnemyCasting"]['value'] and talents["Silence"]['value']: return 'l' #interrupt
            elif talents["EnemyHP%"]['value'] <= 20 and talents["SWD"]['value']: return '2' #SWD
            elif talents["dplague"]['value'] and (talents["voidformbuff"]['value'] or talents["Insanity"]['value'] >= 100) \
                and not talents["dplague.debuff"]['value']: return '3'
            elif talents["instamindblast"]['value']: return '4'
            elif talents["Dispel"]['value'] and talents["Dispellable"]['value']: return 'j'
            elif talents["Shadowfiend"]['value'] == 1 and \
                talents["EnemyHPCutoff"]['value'] >= 2000000 and \
                talents["EnemyHP%"]['value'] >= 20: return 'v'
            #dotsqqqqqq
            elif talents["shadowcrash"]['value'] == 1 and talents["vampiric.debuff"]['value'] != 1 and talents["AOECount"]['value'] >= 3: return 'e'
            elif talents["vapiric"]['value'] and talents["vampiric.debuff"]['value'] != 1 \
                and (not talents["shadowcrash"]['value'] or talents["AOECount"]['value'] <= 3): return '5'
            #!dots
            elif talents["AOECount"]['value'] >= 3 and talents["halo"]['value']: return 'k'
            elif talents["surgeOfinsanity"]['value']: return '6'
            elif talents["mindblast"]['value']: return '4'
            elif talents["voidtorrent"]['value'] and not talents["voidformbuff"]['value']: return 'z'
            elif talents["mindgames"]['value']: return 'c'
            elif talents["mindflay"]['value']: return '6'
    elif talents["ISmoving"]['value'] == 1:
        if talents["canattack"]['value']:
            if talents["voidbolt"]['value']: return 'f'
            elif talents["EnemyHP%"]['value'] <= 20 and talents["SWD"]['value']: return '2' #SWD
            elif talents["EnemyCasting"]['value'] and talents["Silence"]['value']: return 'l' #interrupt
            elif talents["dplague"]['value'] and talents["Insanity"]['value'] >= 70 and not talents["dplague.debuff"]['value']: return '3'
            elif talents["instamindblast"]['value']: return '4'
            elif talents["PWS"]['value'] and not talents["SPEEDBUFF"]['value']: return 'q'
            elif talents["AngelicFeather"]['value'] and not talents["SPEEDBUFF"]['value']: return 'sftq'
        else:
            if talents["PWS"]['value'] and not talents["SPEEDBUFF"]['value']: return 'q'
            elif talents["AngelicFeather"]['value'] and not talents["SPEEDBUFF"]['value']: return 'sftq'