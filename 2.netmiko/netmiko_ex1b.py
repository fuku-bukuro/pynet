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
    output = net_con.send_command("ping", expect_string = "Protocol", strip_prompt = False, strip_command = False)
    output += net_con.send_command("\n", expect_string = "Target", strip_prompt = False, strip_command = False)
    output += net_con.send_command("8.8.8.8", expect_string = "Repeat", strip_prompt = False, strip_command = False)
    output += net_con.send_command("\n", expect_string = "Datagram", strip_prompt = False, strip_command = False)
    output += net_con.send_command("\n", expect_string = "Timeout", strip_prompt = False, strip_command = False)
    output += net_con.send_command("\n", expect_string = "Extended", strip_prompt = False, strip_command = False)
    output += net_con.send_command("\n", expect_string = "Sweep", strip_prompt = False, strip_command = False)
    output += net_con.send_command("\n", expect_string = "#", strip_prompt = False, strip_command = False)

    print(output)

