def vlan_exists(vlan_id):
    vlans = [1,10,20,30]
    if vlan_id in vlans:
        return True
    return False

print(vlan_exists(10))
print("\n")
print(vlan_exists(5))

