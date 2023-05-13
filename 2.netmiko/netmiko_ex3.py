#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


dev1 = {
    "device_type": "cisco_xe",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    }

cmds = ["show version", "show lldp neighbors"]

for cmd in cmds:
    with ConnectHandler(**dev1) as net_con:
        output = net_con.send_command(cmd, use_textfsm = True)
        pprint(output)
        if cmd == "show lldp neighbors":
            output = net_con.send_command(cmd, use_textfsm = True)
            print("Neighbor's interface is {}".format(output[0]['neighbor_interface']))
 
