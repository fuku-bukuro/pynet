#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    }

with ConnectHandler(**device1) as net_con:
    output = net_con.send_command_timing("ping", strip_prompt = False, strip_command = False)
    output += net_con.send_command_timing("\n", strip_prompt = False, strip_command = False)
    output += net_con.send_command_timing("8.8.8.8", strip_prompt = False, strip_command = False)
    output += net_con.send_command_timing("\n", strip_prompt = False, strip_command = False)
    output += net_con.send_command_timing("\n", strip_prompt = False, strip_command = False)
    output += net_con.send_command_timing("\n", strip_prompt = False, strip_command = False)
    output += net_con.send_command_timing("\n", strip_prompt = False, strip_command = False)
    output += net_con.send_command_timing("\n", strip_prompt = False, strip_command = False)

    print(output)

