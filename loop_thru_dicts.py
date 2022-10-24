import json
vlan10 = {'name': 'web', 'id': '10'}
vlan20 = {'name': 'app', 'id': '20'}
vlan30 = {'name': 'db', 'id': '30'}
vlans = [vlan10, vlan20, vlan30]

print(json.dumps(vlans, indent=4))

for vlan in vlans:
    print(vlan)
    print(type(vlan))


for vlan in vlans:
    print("vlan {}".format(vlan['id']))
    print(" name {}".format(vlan['name']))