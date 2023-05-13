import time
import re

from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined

from netmiko import Netmiko
from pprint import pprint
from getpass import getpass

from my_devices import nxos1, nxos2

if __name__ == "__main__":
    env = Environment(undefined = StrictUndefined)
    env.loader = FileSystemLoader("./templates/")

    template_file = env.get_template("nxos_ipv4_intf.j2")
    
    nxos1_vars= {
        "device_name": "nxos1",
        "interface": "Ethernet1/1",
        "ip_address": "10.1.100.1",
        "netmask": 24,
        "as_no": 22
    }
    nxos2_vars = {
        "device_name": "nxos2",
        "interface": "Ethernet1/1",
        "ip_address": "10.1.100.2",
        "netmask": 24,
        "as_no": 22
    }

    nxos1_vars['peer_ip'] = nxos2_vars['ip_address']
    nxos2_vars['peer_ip'] = nxos1_vars['ip_address']

    nxos1["j2_vars"] = nxos1_vars
    nxos2["j2_vars"] = nxos2_vars
#    pprint(nxos1)

    for device in (nxos1, nxos2):
        #working with temporary device to get the config
        tmp_device = device.copy()
        j2_vars = tmp_device.pop("j2_vars")
        cfg = template_file.render(**j2_vars)
        device_name = device['j2_vars']['device_name']
        print(f" {device_name} ".center(80, "#"))
        print(f"\n>>> Template output {device_name}")
        print(cfg)
        cfg_lines = [cfg.strip() for cfg in cfg.splitlines()]

        # set netmiko connection
        net_connect = Netmiko(**tmp_device)
        # store ssh connection for later so I do not have to reconnect
        device["ssh_conn"] = net_connect
        pprint(device)
        print(f">>> Configuring {device_name}")
        output = net_connect.send_config_set(cfg_lines)
        print(output)
        print("\n\n")

    # Give BGP enough time to reach the established state
    sleep_time = 15
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)

    print("\n\n")
    print(">>> Testing ping and BGP")
    for device in (nxos1,):
        net_connect = device["ssh_conn"]
        remote_ip = device["j2_vars"]["peer_ip"]

        # Test ping
        output = net_connect.send_command(f"ping {remote_ip}")
        print(output)
        if "64 bytes from" not in output:
            print("\nPing failed!!!")
        print("\n\n")

        # Test BGP
        bgp_verify = f"show ip bgp summary | include {remote_ip}"
        output = net_connect.send_command(bgp_verify)
        # Retrieve the State/PfxRcd field which is the last field
        match = re.search(r"\s+(\S+)\s*$", output)
        prefix_received = match.group(1)
        try:
            # If this is an integer, the BGP session reached the established state
            int(prefix_received)
            print(
                f"BGP reached the established state. Prefixes received {prefix_received}"
            )
        except ValueError:
            print("BGP failed to reach the established state")

    # All done - disconnect on both devices
    for device in (nxos1, nxos2):
        net_connect = device["ssh_conn"]
        net_connect.disconnect()

    print("\n\n")














