hostname = 'R1'
platform = 'ios'
interface = 'Ethernet1/1'

if hostname.lower() == 'r1':
    print('Hostname correct')

print('Done')

# if hostname.lower() == 'r1' and platform == 'ios':
#     print('Hostname and platform are correct')

# print('Done')
#----------------------------------------------------------------------------



#Update the `if` statement with `else`, also change `platform` to `ios`

# if hostname.lower() == 'r1' and platform == 'ios':
#     print('Hostname and platform are correct')
# else:
#     print('Parameters are not correct')
# print('Done')

#----------------------------------------------------------------------------


# The `if-elif-else`

# if interface.lower().startswith('et'):
#     itype = 'ethernet'
# elif interface.lower().startswith('vl'):
#     itype = 'vlan'
# else:
#     itype = 'unknown'

# print(itype)

#----------------------------------------------------------------------------

# More `elif` statements

# if interface.lower().startswith('et'):
#     itype = 'ethernet'
# elif interface.lower().startswith('vl'):
#     itype = 'vlan'
# elif interface.lower().startswith('lo'):
#     itype = 'loopback'
# elif interface.lower().startswith('po'):
#     itype = 'portchannel'
# else:
#     itype = 'unknown'

# print(itype)

#----------------------------------------------------------------------------

# Nested conditionals

# vendor = 'cisco'
# platform = 'nexus'
# model = '9000'

# if vendor == 'cisco':
#     print('Vendor: {}'.format(vendor))
#     if platform == 'nexus':
#         print('Platform: {}'.format(platform))
#         if model == '9000':
#             print('Model: {}'.format(model))
#         else:
#             print('unknown model')
#     else:
#         print('unknown platform')
# else:
#     print('unknown vendor')

#----------------------------------------------------------------------------

# Empty variables

# variable = True

# if variable:
#     print('The result is True')
# else:
#     print('The result is False')

#----------------------------------------------------------------------------

#Valid key in dictionary as a condition

# variable = {'platform': 'nxos'}

# if variable.get('platform'):
#     print('The result is True')
# else:
#     print('The result is False')

#----------------------------------------------------------------------------

#Invalid key in dictionary as a condition

# variable = {'platform': 'nxos'}

# if variable.get('model'):
#     print('The result is True')
# else:
#     print('The result is False')

#----------------------------------------------------------------------------


#Invalid key in dictionary as a condition with a fallback string

# variable = {'platform': 'nxos'}

# if variable.get('model'):
#     print('The result is True')
# else:
#     print('The result is False')




