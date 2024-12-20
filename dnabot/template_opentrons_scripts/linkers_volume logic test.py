linkers_volume = 50
robot = 'OT-2'

# outer if statement
if robot =='Flex':
    if linkers_volume > 100:
        linker_vol =100
        print('Flex linker vol', linker_vol)
    elif robot =='OT-2':
        if linkers_volume > 40:
            linker_vol = 40
            print('OT-2 linker vol', linker_vol)
    else:
        linker_vol = linkers_volume    
        print('bottom of script', linker_vol)    


