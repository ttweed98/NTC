def get_vlans(device):
    if device == "R1":
        vlans = [1,5,10,15,20,25]
        #return vlans
    elif device == 'R2':
        vlans = [3,5,7,9,11]
        #return vlans
    else:
        vlans = 'Unknown Device'

    return vlans

    


print(get_vlans('R3'))