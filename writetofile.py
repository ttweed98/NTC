from pprint import pprint as pp

vlans = [
    {'id': '10', 'name': 'USERS'},
    {'id': '20', 'name': 'VOICE'},
    {'id': '30', 'name': 'WLAN'},
    {'id': '40', 'name': 'APP'},
    {'id': '50', 'name': 'WEB'}
]


# pp(vlans)

import json
content = json.dumps(vlans, indent = 4)
# print(content)

# write vlans into a file

# vlans_file = open('configs/vlans.cfg', 'w')
# vlans_file.write(content)

with open('configs/vlans.cfg', 'a') as vlans_file:
    vlans_file.write(content)

