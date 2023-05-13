#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "session_log": "output_c1_ex1.log"
    }

with ConnectHandler(**device1) as net_con:
    print(net_con.find_prompt())

