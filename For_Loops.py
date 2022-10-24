commands = ['interface Eth2/1', 'description Configured by Python', 'speed 100', 'duplex full']
for command in commands:
    print(command)

#Another example
for item in commands:
    print(item)

interface = {}
interface['duplex'] = 'full'
interface['speed'] = '100'
interface['description'] = 'Configured by Python'

print(interface)

for key in interface.keys():
    print(key)

for value in interface.values():
    print(value)

for key, value in interface.items():
    print(key, '--->', value)