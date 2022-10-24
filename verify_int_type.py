def get_interface_type(interface):
    if interface.lower().startswith('et'):
        iftype = 'ethernet'
    elif interface.lower().startswith('vl'):
        iftype = 'vlan'
    elif interface.lower().startswith('lo'):
        iftype = 'loopback'
    elif interface.lower().startswith('po'):
        iftype = 'portchannel'
    else:
        iftype = 'unknown'
    

    return iftype
print("this line should print when this file is imported by another ")

if __name__=="__main__":
    intf = 'GigabitEthernet1/2'
    int_type = get_interface_type(intf)
    print(int_type)