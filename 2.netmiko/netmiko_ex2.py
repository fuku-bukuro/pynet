#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


dev1 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False
    }
cmd = "show lldp neighbors detail"
with ConnectHandler(**dev1) as net_con:
    start_time = datetime.now()
    output = net_con.send_command(cmd)
    end_time = datetime.now()

 #   print("+" * 60)
 #   print(output)
 #   print("+" * 60)
    print("\n\nExecution Time {}".format(end_time - start_time))
    print()

with ConnectHandler(**dev1) as net_con:
    start_time = datetime.now()
    output = net_con.send_command(cmd, delay_factor = 8)
    end_time = datetime.now()

#    print("+" * 60)
#    print(output)
#    print("+" * 60)
    print("\n\nExecution Time {}".format(end_time - start_time))
    print()

