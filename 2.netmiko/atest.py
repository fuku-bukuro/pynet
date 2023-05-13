#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    }

net_con = ConnectHandler(**device1)
print(net_con.find_prompt())

