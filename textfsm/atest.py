#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    }

with ConnectHandler(**device1) as net_con, open("interfaces.txt", "w") as f:
    f.write(net_con.send_command("show ip int bri"))

