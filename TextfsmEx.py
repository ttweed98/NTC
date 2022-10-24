from netmiko import ConnectHandler
import textfsm

with ConnectHandler(host = 'csr1', username = 'ntc', password = "ntc123", device_type = "cisco_ios") as csr1Connection:
    showLLDPnei = csr1Connection.send_command("show lldp neighbors")
print(showLLDPnei)
filevar1 = open('../../files/LLDPoutput.raw', 'w')
filevar1.write(showLLDPnei)
filevar1.close()

# table = textfsm.TextFSM(open('../../textfsm/cisco_ios_show_lldp_neighbors.textfsm') )

# data = table.ParseText('../../files/LLDPoutput.raw')

# print(data)