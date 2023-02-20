#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}
with ConnectHandler(**device) as net_con:
    print(net_con.find_prompt())
    print(net_con.config_mode())
    print(net_con.exit_config_mode())
    print(net_con.find_prompt())
    net_con.write_channel("disable\n")
    time.sleep(2)
    print(net_con.read_channel())
    print(net_con.enable())
    print(net_con.find_prompt())

