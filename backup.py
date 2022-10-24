#! /usr/bin/env python

from netmiko import ConnectHandler

devicelist = ['csr1', 'csr2']

for each_device in devicelist:
    hostname = each_device
    #print(hostname)

    print(f"Connecting to device | {hostname} ")


    dev = ConnectHandler(
        host=hostname, username="ntc", password="ntc123", device_type="cisco_ios"
    )

    
    print(f"Saving configuration | {hostname}" )

    dev.send_command("wr mem")

    print(f"Backing up configuration |{hostname}" )

    dev.send_command("term len 0")
    run_config = dev.send_command("show run")

    print(f"Writing config to file |{hostname}\n")

    with open(f"/home/ntc/labs/python/configs/{hostname}.cfg", "w") as config_file:
        config_file.write(run_config)


