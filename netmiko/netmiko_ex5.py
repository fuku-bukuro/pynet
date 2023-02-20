#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

password = getpass()

with open("devices.txt") as f:
    for device in f:
        dev = {
            "device_type": "cisco_nxos",
            "host": device,
            "username": "pyclass",
            "password": password,
        }
        with Netmiko(**dev) as net_con:
            output = net_con.send_config_from_file("vlans.cfg",strip_command = False, strip_prompt = False)
            output = net_con.send_command("show vlan brief")
            print(output)

