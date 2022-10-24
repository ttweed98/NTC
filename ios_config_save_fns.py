from netmiko import ConnectHandler

def showrun(hostname):
    platform = 'cisco_ios'
    host = hostname
    username = 'ntc'
    password = 'ntc123'

    try:
        device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        print(f"The device being connected to is referenced as {device}.")
        # output = device.send_command('show running-config')
    except:
        print(f"{hostname} is unreachable.")
        return False

    output = device.send_command('show running-config')

    return output

def saveconfig(filename):
    with open(filename, 'w') as file:
        file.write(showrun(hostname))

    return

if __name__ == "__main__":
    hostname = input("Which device do you want to save? ")
    filename = input(" What filename do you want to use to save the config? ")
    if (showrun(hostname)):
        saveconfig(filename)
        print("Connected to device and saved config")
    else:
        print(f"Could not connect to device {hostname} successfully")