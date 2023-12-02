talents = {
    'canattack':            {'value': 0,'pixel': 0,'match': (255,141,120),'assign': 1},
    "ISmoving":             {'value': 0,'pixel': 1,'match': (10, 255, 255),'assign': 1},
    "MyHP":                 {'value': 0,'pixel': 2, 'multi': [
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
    "Essence":              {'value': 0,'pixel': 3, 'multi': [
                            {'match': (50,255,0),'assign': 5},
                            {'match': (40,255,0),'assign': 4},
                            {'match': (30,255,0),'assign': 3},
                            {'match': (20,255,0),'assign': 2},
                            {'match': (10,255,0),'assign': 1}]},
    "EnemyHPCutoff":        {'value': 0,'pixel': 4, 'multi': [
                            {'match': (10,10,255),'assign': 500000},
                            {'match': (10,20,255),'assign': 1000000}]},
    "EnemyHP%":             {'value': 0,'pixel': 6, 'multi': [
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
    "EnemyCasting":         {'value': 0,'pixel': 7,'match': (10, 255, 0),'assign': 1},
    "AOECount":             {'value': 0,'pixel': 8, 'multi': [
                            {'match': (0,20,255),'assign': 2},
                            {'match': (0,30,255),'assign': 3},
                            {'match': (0,40,255),'assign': 4},
                            {'match': (0,50,255),'assign': 5},
                            {'match': (0,60,255),'assign': 6},
                            {'match': (0,70,255),'assign': 7},
                            {'match': (0,80,255),'assign': 8}]},
    "FireBreath":           {'value': 0,'pixel': 9,'match': (255, 10, 0),'assign': 1},
    "EternitySurge":        {'value': 0,'pixel': 10,'match': (10, 255, 0),'assign': 1},
    "Desintegrate":         {'value': 0,'pixel': 11,'match': (10, 0, 255),'assign': 1},
    "Pyre":                 {'value': 0,'pixel': 12,'match': (255, 10, 0),'assign': 1},
    "ShatteringStar":       {'value': 0,'pixel': 13,'match': (10, 255, 0),'assign': 1},
    "AzureStrike":          {'value': 0,'pixel': 15,'match': (10, 0, 255),'assign': 1},
    "DragonRage":           {'value': 0,'pixel': 16,'match': (255, 10, 0),'assign': 1},
    "EssenceBurstBuff":     {'value': 0,'pixel': 17,'match': (10, 255, 0),'assign': 1},
    "FeedTheFlamesBuff":    {'value': 0,'pixel': 18, 'multi': [
                            {'match': (10,0,255),'assign': 1},
                            {'match': (20,0,255),'assign': 2},
                            {'match': (30,0,255),'assign': 3},
                            {'match': (40,0,255),'assign': 4},
                            {'match': (50,0,255),'assign': 5},
                            {'match': (60,0,255),'assign': 6},
                            {'match': (70,0,255),'assign': 7},
                            {'match': (80,0,255),'assign': 8},
                            {'match': (90,0,255),'assign': 9},]},
    "ChargedBlastBuff":     {'value': 0,'pixel': 19, 'multi': [
                            {'match': (255,5,0),'assign': 5},
                            {'match': (255,10,0),'assign': 10},
                            {'match': (255,15,0),'assign': 15},
                            {'match': (255,20,0),'assign': 20},]},
    "BurnoutBuff":          {'value': 0,'pixel': 20,'match': (10, 255, 0),'assign': 1},
    "LeapingFlamesBuff":    {'value': 0,'pixel': 21,'match': (10, 0, 255),'assign': 1},
    "DragonRageBuff":       {'value': 0,'pixel': 22,'match': (255, 10, 0),'assign': 1},
    "FireBreathCharge":     {'value': 0,'pixel': 24, 'multi': [
                            {'match': (10,255,0),'assign': 1},
                            {'match': (20,255,0),'assign': 2},
                            {'match': (30,255,0),'assign': 3},
                            {'match': (40,255,0),'assign': 4},]},
    "EternitySurgeCharge":  {'value': 0,'pixel': 25, 'multi': [
                            {'match': (10,0,255),'assign': 1},
                            {'match': (20,0,255),'assign': 2},
                            {'match': (30,0,255),'assign': 3},
                            {'match': (40,0,255),'assign': 4},]},
    'DesintegrateCasting':  {'value': 0,'pixel': 26,'match': (255,10,0),'assign': 1},
    'FireBreathCasting':  {'value': 0,'pixel': 27,'match': (10,255,0),'assign': 1},
    'EternitySurgeCasting':  {'value': 0,'pixel': 28,'match': (10,0,255),'assign': 1},
    'iscasting':  {'value': 0,'pixel': 29,'match': (255,10,0),'assign': 1},
    'HoverBuff':  {'value': 0,'pixel': 30,'match': (10,255,0),'assign': 1},
    }
    
def rotation(talents):
    if talents['canattack']['value']:
        # print(talents['Desintegrate']['value'], talents['DesintegrateCasting']['value'])
        print(talents['ISmoving']['value'], talents['HoverBuff']['value'])
        if talents['EnemyCasting']['value']: return 'j'
        elif talents['BurnoutBuff']['value'] and not talents['iscasting']['value']:
            return '1'
        elif not talents['ISmoving']['value']:
            if (talents['FireBreath']['value'] or talents['FireBreathCasting']['value']) and not talents['EternitySurgeCasting']['value']:
                if not (talents['FireBreathCharge']['value'] or talents['FireBreathCasting']['value']): return '3' #start casting
                match talents['AOECount']['value']:
                    case 0|2:
                        if talents['EnemyHPCutoff']['value'] >= 1000000 and talents['FireBreathCharge']['value'] >= 1: return '3'
                        elif talents['FireBreathCharge']['value'] >= 1: return '3'
                    case 3:
                        if talents['FireBreathCharge']['value'] >= 2: return '3'
                    case 4|5:
                        if talents['FireBreathCharge']['value'] >= 3: return '3'
                    case _:
                        print('FireBreathCharge exception')
                        return '3'
            elif (talents['EternitySurge']['value'] or talents['EternitySurgeCasting']['value']) and not talents['FireBreathCasting']['value']:
                if not (talents['EternitySurgeCharge']['value'] or talents['EternitySurgeCasting']['value']): return '2' #start casting
                match talents['AOECount']['value']:
                    case 0|2:
                        if talents['EternitySurgeCharge']['value'] >= 1: return '2'
                    case 3|4:
                        if talents['EternitySurgeCharge']['value'] >= 2: return '2'
                    case 5|6:
                        if talents['EternitySurgeCharge']['value'] >= 3: return '2'
                    case 7|8:
                        if talents['EternitySurgeCharge']['value'] >= 4: return '2'
                    case _:
                        print('EternitySurgeCharge exception')
                        return '2'
            elif not (talents['iscasting']['value'] or talents['EternitySurge']['value'] or talents['FireBreath']['value']):
                if talents['ShatteringStar']['value'] and (talents['Essence']['value'] >= 4 or talents['EssenceBurstBuff']['value']): return '4'
                elif talents['AOECount']['value'] <= 2:
                    if talents['Desintegrate']['value']: return 'e'
                    else: return '1' #LivigFlames
                elif talents['AOECount']['value'] >= 3:
                    if talents['Pyre']['value']:
                        match talents['AOECount']['value']:
                            case 3:
                                print('case 3')
                                if talents['ChargedBlastBuff']['value'] >= 10: return 'q'
                                else: return '5'
                            case 4|5: 
                                print('case 4|5')
                                if talents['ChargedBlastBuff']['value'] >= 5: return 'q'
                                else: return '5'
                            case 6|7|8: 
                                print('case 6|7|8')
                                return 'q'
                            case _:
                                print('Case exception')
                                return '5'
                    else: return '5'
        else:
            # if moving
            if talents['ShatteringStar']['value'] and (talents['Essence']['value'] >= 4 or talents['EssenceBurstBuff']['value']): return '4'
            elif talents['AOECount']['value'] <= 2 and talents['HoverBuff']['value'] and talents['Desintegrate']['value']: return 'e'
            elif talents['AOECount']['value'] >= 3:
                if talents['Pyre']['value']:
                    match talents['AOECount']['value']:
                        case 3:
                            print('case 3')
                            if talents['ChargedBlastBuff']['value'] >= 10: return 'q'
                            else: return '5'
                        case 4|5: 
                            print('case 4|5')
                            if talents['ChargedBlastBuff']['value'] >= 5: return 'q'
                            else: return '5'
                        case 6|7|8: 
                            print('case 6|7|8')
                            return 'q'
                        case _:
                            print('Case exception')
                            return '5'
                else: return '5'
            else: return '5'