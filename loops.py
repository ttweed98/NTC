interfaces = ['Ethernet1/1', 'Vlan100', 'Loopback100', 'GigabitEthernet2/6']

for interface in interfaces:
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

    print(interface + '---' + iftype)