#! /usr/bin/env python


def get_vlans():
    return [1, 5, 10, 20]


def vlan_exists(vlan_id):
    return vlan_id in get_vlans()

def print_vlans():
    vlans = [1,5,10,11,14,15]
    #print(vlans)
    return vlans




# vlans = get_vlans()
# print(vlans)

# print(vlan_exists(10))
# print(vlan_exists(12))

vlan_list = print_vlans()
print(vlan_list)