interface = 'Management0'

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

print(iftype)