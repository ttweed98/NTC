# def addition():
#     answer = 44 + 76
#     return answer

# print(addition())

# router = 'R2'
# vendor = 'arista'

# def get_vlans(device, vendor):
#     print(device)
#     print(vendor)
#     if device == 'R1':
#         if vendor == 'cisco':
#             vlans = [1,2,5,7,8,10]
#         else:
#             vlans = []
#     else:
#         vlans = [10,20,50,70,80,100]

#     return vlans

# print(get_vlans('cisco', 'R3'))



























# router = 'R1'
# vendor = 'juniper'

# vlans_list = get_vlans(router, vendor)
# print(vlans_list)


# def vlan_exist(vlan_id):
#     vlans = [1, 5, 10, 100]
#     if vlan_id in vlans:
#         return True
#     return False


# vlan = 25

# if vlan_exist(vlan):
#     print('VLAN exists')
# else:
#     print('VLAN does not exists')















# def get_interface_type(interface):
#     if interface.lower().startswith('et'):
#         itype = 'ethernet'
#     elif interface.lower().startswith('vl'):
#         itype = 'vlan'
#     elif interface.lower().startswith('lo'):
#         itype = 'loopback'
#     else:
#         itype = 'unknown'

#     return itype


# print(get_interface_type('Management0'))



# interfaces = ['Ethernet1/1', 'Vlan100', 'Loopback100', 'Port-Channel1', 'Management0']

# for interface in interfaces:
#     print(get_interface_type(interface))































def interface_settings(interface, speed='auto', duplex='auto'):
    print('-'*40)
    print('Interface: {}'.format(interface))
    print('Speed: {}'.format(speed))
    print('Duplex: {}'.format(duplex))

interface_settings('ethernet1/3', duplex ='full', speed ='100M')
































































