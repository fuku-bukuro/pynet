#!/usr/bin/env python
"""
Use processes and Netmiko to connect to each of the devices. Execute
'show version' on each device. Record the amount of time required to do this.
"""
from __future__ import print_function, unicode_literals
from multiprocessing import Process

from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list as devices

def show_version(a_device):
    """Execute show version command using Netmiko."""
    remote_conn = ConnectHandler(**a_device)
    output = remote_conn.send_command_expect("show version")
    remote_conn.disconnect()
    print()
    print("#" * 50)
    print(output)
    print("#" * 50)
    print()


def main():
    """
    Use processes and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Record the amount of time required to do this.
    """
    start_time = datetime.now()

    procs = []
    for a_device in devices:
        my_proc = Process(target = show_version, args = (a_device,))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        # print(a_proc)
        a_proc.join()

    print("\Elapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()


