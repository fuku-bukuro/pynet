#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


dev1 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    }

cmds = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup", "do ping google.com"]

for cmd in cmds:
    with ConnectHandler(**dev1) as net_con:
        output = net_con.send_config_set(cmds)
        print(output)
 
