#! /usr/bin/env python

from pprint import pprint as pp
import json

facts1 = {'vendor': 'cisco', 'os': 'nxos', 'ipaddr': '10.1.1.1'}
facts2 = {'vendor': 'cisco', 'os': 'ios', 'ipaddr': '10.2.1.1'}
facts3 = {'vendor': 'arista', 'os': 'eos', 'ipaddr': '10.1.1.2'}

devices = [facts1, facts2, facts3]

#print devices vs pprint devices vs print with json.dumps

print(devices)

print('-' * 60)

pp(devices)

print('----------------------------------------------------------------')

print(json.dumps(devices, indent=4))