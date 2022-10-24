# hostname = 'R1'
# platform = 'ios-xr'

# if hostname.lower() == 'r1' and platform == 'ios':
#     print('Hostname correct')
# else:
#     print("Hostname and platform are not correct")

# print('Params provided are not right')

# interface = 'Management0'

# if interface.lower().startswith('et'):
#         iftype = 'ethernet'
# elif interface.lower().startswith('vl'):
#         iftype = 'vlan'
# elif interface.lower().startswith('lo'):
#     iftype = 'loopback'
# elif interface.lower().startswith('po'):
#     iftype = 'portchannel'
# else:
#     iftype = 'unknown'

# print(iftype)

vendor = 'cisco'
platform = 'nexus'
model = '9500'

if vendor == 'cisco':
    print(f'Vendor: {vendor}')
    if platform == 'nexus':
        print(f'Platform: {platform}')
        if model == '9000':
            print(f'Model: {model}')
        else:
            print('Unknown model')
    else:
        print('Unknown platform')
else:
    print('Unknown vendor')