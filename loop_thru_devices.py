import json

devices = [{'platform': 'nexus', 'hostname': 'nycr01'}, {'platform': 'catalyst', 'hostname': 'nycsw02'}, {'platform': 'mx', 'hostname': 'nycr03'}, {'platform': 'srx', 'hostname': 'nycfw01'}, {'platform': 'asa', 'hostname': 'nycfw02'}]
print(json.dumps(devices, indent=4))

for item in devices:
    platform = item.get('platform')
    if platform == "nexus":
         print("Vendor is Cisco")
    elif platform == "catalyst":
         print("Vendor is Cisco")
    elif platform == "aci":
         print("Vendor is Cisco")
    elif platform == "srx" or platform == "mx":
         print("Vendor is Juniper")
    else:
         print("Unknown Vendor")

# Another option to verify

cisco_platforms = ['catalyst', 'nexus', 'aci']
juniper_platforms = ['mx', 'srx']

for item in devices:
    platform = item.get('platform')
    if platform in cisco_platforms:
        print("Vendor is Cisco")
    elif platform in juniper_platforms:
        print("Vendor is Juniper")
    else:
        print("Unknown Vendor")
