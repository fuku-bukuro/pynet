"""For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory."""
#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()


dev1 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    }

dev2 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    }

for i in (dev1, dev2):
    with ConnectHandler(**i) as net_con:
        if i == dev1:
            print(net_con.find_prompt())
            with open("output_c1_ex3.log", "a") as f:
                f.write(net_con.send_command("show version"))
        else:
            print(net_con.find_prompt())
