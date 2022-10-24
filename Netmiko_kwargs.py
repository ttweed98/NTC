from netmiko import ConnectHandler
csr_vars = {'ip' : 'csr2', 'device_type' : 'cisco_ios', 'username' : 'ntc', 'password' : 'ntc123'}
cisco_devices = ['csr1', 'csr2', 'csr3']

for each_device in cisco_devices:
    csr_vars['ip'] = each_device
    csr_connection = ConnectHandler(**csr_vars)

    print(f'Checking connectivity to {each_device}:' , csr_connection.is_alive())
    csr_connection.disconnect()

    print(f"Disconnecting from the Cisco device: {each_device}")

    print('Check connectivity after disconnect:', csr_connection.is_alive())

    print('-' * 60)


# from netmiko import ConnectHandler
# csr_vars = {'ip' : 'csr2', 'device_type' : 'cisco_ios', 'username' : 'ntc', 'password' : 'ntc123'}
# cisco_devices = ['csr1', 'csrA','csr2', 'csr3', 'csr4','csr5']

# for item in cisco_devices:
#     csr_vars['ip'] = item
#     try:
#         devConn = ConnectHandler(**csr_vars)
        
#         statusofconnection = devConn.is_alive()
       
#         # print(statusofconnection)
#         if statusofconnection:
#             print(f"The connection to {item} has been established")
#     except:
#         print('This is not a valid device')