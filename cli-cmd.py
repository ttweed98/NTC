"""Comment and uncomment lines as needed to demo to students"""
#! /usr/bin/env python
import sys
import argparse

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

# interface = input('Please enter the interface name:')
# interface_type = get_interface_type(interface)
# print(f"The interface type is {interface_type}")

# print(sys.argv)
# if len(sys.argv) != 2:
#     print('You need to specify the interface name.')
# else:
#     interface = sys.argv[1]
#     interface_type = get_interface_type(interface)
#     print(f"The interface type is {interface_type}")

parser = argparse.ArgumentParser(description = 'ARGPARSE DEMO')
parser.add_argument('-i', '--interface', help='Interface name', required = True)
#parser.add_argument('-p','--print', help='specify if you want the interfacetype printed', type=bool, default = False)
parser.add_argument('-p','--print', help='specify if you want the interfacetype printed', action='store_true')

args = parser.parse_args()

interface = args.interface
print(interface)
interface_type = get_interface_type(interface)

print(args.print)
#print(type(args.print))
if args.print:
    print(f'The interface type is {interface_type} ')