from netmiko import ConnectHandler
csr_vars = {'ip' : 'csr2', 'device_type': 'cisco_ios', 'username': 'ntc', 'password': 'ntc123'}
sshconnection = ConnectHandler(**csr_vars)