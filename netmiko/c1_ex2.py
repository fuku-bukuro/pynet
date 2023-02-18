#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()


dev1 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "output_c1_ex2-1.log"
    }

dev2 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "output_c1_ex2-2.log"
    }

for i in (dev1, dev2):
    with ConnectHandler(**i) as net_con:
        print(net_con.find_prompt())

