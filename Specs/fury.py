talents = {
    'canattack':
        {'value': 0,'pixel': 0,'match': (255,141,120),'assign': 1},
    "ISmoving":
        {'value': 0,'pixel': 1,'match': (10, 255, 255),'assign': 1},
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
        {'value': 0,'pixel': 4,'match': (10, 255, 0),'assign': 1},
    "Rage%":
        {'value': 0,'pixel': 5, 'multi': [
        {'match': (0,40,255),'assign': 40},
        {'match': (0,50,255),'assign': 50},
        {'match': (0,60,255),'assign': 50},
        {'match': (0,70,255),'assign': 70},
        {'match': (0,80,255),'assign': 80}]},
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
        {'value': 0,'pixel': 8, 'multi': [
        {'match': (10,255,0),'assign': 500000},
        {'match': (20,255,0),'assign': 1000000}, #1m
        {'match': (30,255,0),'assign': 2000000}, #2m
        {'match': (40,255,0),'assign': 10000000},]}, #10m
    "AOECount":
        {'value': 0,'pixel': 9, 'multi': [
        {'match': (20,0,255),'assign': 2},
        {'match': (30,0,255),'assign': 3},
        {'match': (40,0,255),'assign': 4},
        {'match': (50,0,255),'assign': 5},
        {'match': (60,0,255),'assign': 6},
        {'match': (70,0,255),'assign': 7},
        {'match': (80,0,255),'assign': 8}]},
    'iscasting':
        {'value': 0,'pixel': 10,'match': (255,10,0),'assign': 1},
    "Rampage":
        {'value': 0,'pixel': 12,'match': (10, 255, 0),'assign': 1},
    "Bloodthirst":
        {'value': 0,'pixel': 13,'match': (10, 0, 255),'assign': 1},
    "WhirlwindBuff":
        {'value': 0,'pixel': 14,'match': (255, 10, 0),'assign': 1},
    "Recklesness":
        {'value': 0,'pixel': 16,'match': (10, 255, 0),'assign': 1},
    "Charge":
        {'value': 0,'pixel': 17,'match': (10, 0, 255),'assign': 1},
    "EnragedRegen":
        {'value': 0,'pixel': 18,'match': (255, 10, 0),'assign': 1},
    "RagingBlow":
        {'value': 0,'pixel': 19,'match': (10, 255, 0),'assign': 1},
    "Ravager":
        {'value': 0,'pixel': 21,'match': (10, 0, 255),'assign': 1},
    "Spear":
        {'value': 0,'pixel': 22,'match': (255, 10, 0),'assign': 1},
    "Rally":
        {'value': 0,'pixel': 23,'match': (10, 255, 0),'assign': 1},
    "Pummel":
        {'value': 0,'pixel': 25,'match': (10, 0, 255),'assign': 1},
    "VictoryRush":
        {'value': 0,'pixel': 26,'match': (255, 10, 0),'assign': 1},
    "EnragedRegenBuff":
        {'value': 0,'pixel': 27,'match': (10, 255, 0),'assign': 1},
    "Onslaught":
        {'value': 0,'pixel': 29,'match': (10, 0, 255),'assign': 1},
    "Execute":
        {'value': 0,'pixel': 30,'match': (255, 10, 0),'assign': 1},
    "CanStun":
        {'value': 0,'pixel': 31,'match': (10, 255, 0),'assign': 1},
    "StormBolt":
        {'value': 0,'pixel': 33,'match': (10, 0, 255),'assign': 1},
    "RecklesnessBuff":
        {'value': 0,'pixel': 34,'match': (255, 10, 0),'assign': 1},
    "EnragedBuff":
        {'value': 0,'pixel': 35,'match': (10, 255, 0),'assign': 1},
    "GroupLowHP":
        {'value': 0,'pixel': 37,'match': (10, 0, 255),'assign': 1},
    "TalentIWV":
        {'value': 0,'pixel': 38,'match': (255, 10, 0),'assign': 1},
    "TalentSpear":
        {'value': 0,'pixel': 39,'match': (10, 255, 0),'assign': 1},
    "TalentDragonRoar":
        {'value': 0,'pixel': 41,'match': (10, 0, 255),'assign': 1},
    "DragonRoar":
        {'value': 0,'pixel': 42,'match': (255, 10, 0),'assign': 1},
    "MercilessAssault":
        {'value': 0,'pixel': 43,'match': (10, 255, 0),'assign': 1},
    "SophicDevotionBuff":
        {'value': 0,'pixel': 45,'match': (10, 0, 255),'assign': 1},
    "Avatar":
        {'value': 0,'pixel': 46,'match': (255, 10, 0),'assign': 1},
    "AvatarBuff":
        {'value': 0,'pixel': 47,'match': (10, 255, 0),'assign': 1},
    "OdinsFury":
        {'value': 0,'pixel': 49,'match': (10, 0, 255),'assign': 1},
    "PowerStrike":
        {'value': 0,'pixel': 50,'match': (255, 10, 0),'assign': 1},
    }
    
def rotation(talents):
    if talents['canattack']['value']:
        if talents["EnemyCasting"]['value'] and (talents["Pummel"]['value'] or talents['StormBolt']['value']):
            if  talents['Pummel']['value'] and not talents['ISmoving']['value']: return 'l'
            elif  talents['StormBolt']['value']: return 'k'
        # elif talents["Charge"]['value']: return 'f'
        elif talents["Recklesness"]['value'] and talents['EnragedBuff']['value'] and not talents['RecklesnessBuff']['value']: return 'r'
        elif talents["SophicDevotionBuff"]['value'] and talents['EnragedBuff']['value'] and not talents["AvatarBuff"]['value'] and talents["Avatar"]['value'] and talents["EnemyHPCutoff"]['value'] >= 2000000 \
                and talents['EnemyHP%']['value'] >= 50: return 'v'
        elif talents["MyHP"]['value'] <= 60 and talents["VictoryRush"]['value']: return 'e'
        elif talents["MyHP"]['value'] <= 30 and talents["EnragedRegen"]['value']: return 't'
        elif talents["GroupLowHP"]['value'] and talents["Rally"]['value']: return 'x'
        elif talents["TalentIWV"]['value'] and not talents["WhirlwindBuff"]['value'] and talents["AOECount"]['value'] >=2: return '2'
        elif talents["AOECount"]['value'] >=3:
            if talents["Ravager"]['value'] and talents["EnemyHPCutoff"]['value'] >= 1000000 and talents['EnemyHP%']['value'] >= 40 and not talents['ISmoving']['value']:
                return 'z'
            if talents["Spear"]['value'] and talents['TalentSpear']['value'] and talents['RecklesnessBuff']['value'] \
                and talents['EnragedBuff']['value'] and talents["EnemyHPCutoff"]['value'] >= 2000000 \
                and talents['EnemyHP%']['value'] >= 50 and not talents['ISmoving']['value']: return 'j'
            if talents["DragonRoar"]['value'] and talents['TalentDragonRoar']['value'] and talents['RecklesnessBuff']['value'] \
                and talents['EnragedBuff']['value'] and talents["EnemyHPCutoff"]['value'] >= 2000000 \
                and talents['EnemyHP%']['value'] >= 30 and not talents['ISmoving']['value']: return 'j'
        match talents["Rage%"]['value']:
            case 80: #>=90
                if talents["Rampage"]['value']: return '3'
            case _: #>=30
                if talents["EnragedRegenBuff"]['value'] and talents["Bloodthirst"]['value']: return '1'
                elif talents["MercilessAssault"]['value'] and talents["Bloodthirst"]['value']: return '1'
                elif talents["OdinsFury"]['value']: return '4'
                # elif talents["PowerStrike"]['value']: return '6'
                elif talents["Ravager"]['value'] and talents["EnemyHPCutoff"]['value'] >= 1000000 and talents['EnemyHP%']['value'] >= 30 and not talents['ISmoving']['value']: return 'z'
                elif talents["Spear"]['value'] and talents['TalentSpear']['value'] and talents['RecklesnessBuff']['value'] and talents['EnragedBuff']['value'] \
                    and talents["EnemyHPCutoff"]['value'] >= 2000000 and not talents['ISmoving']['value']: return 'j'
                elif talents["DragonRoar"]['value'] and talents['TalentDragonRoar']['value'] and talents['RecklesnessBuff']['value'] and talents['EnragedBuff']['value'] \
                    and talents["EnemyHPCutoff"]['value'] >= 2000000 and not talents['ISmoving']['value']: return 'j'
                elif talents["Execute"]['value']: return 'q'
                elif talents["Onslaught"]['value'] and talents['EnragedBuff']['value']: return '5'
                elif talents["RagingBlow"]['value']: return '4'
                elif talents["Bloodthirst"]['value']: return '1'
