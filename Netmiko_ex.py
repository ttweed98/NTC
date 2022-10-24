from symbol import parameters
from netmiko import ConnectHandler, Netmiko

# Use the context manager 'with' to automatically disconnect when done with netmiko command executaion

# with ConnectHandler(device_type='cisco_ios', ip='csr1', username='ntc', password='ntc123') as dev1:
#     print(dev1.is_alive())
#     print(dev1.send_command('show ip interface brief'))

# print(dev1.is_alive())

# An alternate approach to establishing a connection without Context Manager

dev1 = ConnectHandler(device_type='cisco_ios', ip='csr1', username='ntc', password='ntc123')
print(dev1.is_alive())
print(dev1.send_command('show ip interface brief'))
#dev1.send_config_set(['interface Loopback200', 'description 2nd interface Configured by Netmiko'])
print(dev1.is_alive())


# Use a dictionary to define Netmiko parameters

# cisco1 = {
#     "device_type": "cisco_ios",
#     "host": "cisco1.lasthop.io",
#     "username": "pyclass",
#     "password": getpass(),
# }

# net_connect = ConnectHandler(**cisco1)

# Connect to multiple devices with Netmiko

# cisco1 = {
#     "device_type": "cisco_ios",
#     "host": "cisco1.lasthop.io",
#     "username": "pyclass",
#     "password": password,
# }

# cisco2 = {
#     "device_type": "cisco_ios",
#     "host": "cisco2.lasthop.io",
#     "username": "pyclass",
#     "password": password,
# }

# nxos1 = {
#     "device_type": "cisco_nxos",
#     "host": "nxos1.lasthop.io",
#     "username": "pyclass",
#     "password": password,
# }

# srx1 = {
#     "device_type": "juniper_junos",
#     "host": "srx1.lasthop.io",
#     "username": "pyclass",
#     "password": password,
# }

# for device in (cisco1, cisco2, nxos1, srx1):
#     net_connect = ConnectHandler(**device)