from netmiko import ConnectHandler
import os


def ez_cisco(hostname, show_command, username="ntc", password="ntc123"):
    platform = "cisco_ios"
    device = ConnectHandler(
        ip=hostname, username=username, password=password, device_type=platform
    )

    output = device.send_command(show_command)
    device.disconnect()

    return output


response = ez_cisco("csr1", "show version")
print(response)

response = ez_cisco("csr2", "show ip int brief")
print(response)

response = ez_cisco("csr3", "show run | inc snmp")
print(response)

# Send a list of commands using Netmiko
device = ConnectHandler(
        ip='csr1', username='ntc', password='ntc123', device_type='cisco_ios'
    )
commands = ['interface Loopback100', 'ip address 10.200.1.20 255.255.255.0']
output = device.send_config_set(commands)

#os.system('cat path_to_config.txt_file') # this displays content of config.txt
#output=device.send_config_from_file('pathtofile')