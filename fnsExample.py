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

interfaces = ['ethernet0/1', 'loopback50','management0', 'vlan50']
for item in interfaces:
    intftype = get_interface_type(item)
    print(intftype)