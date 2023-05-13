from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from my_funcs import yaml_read_devices
import yaml
import pyeapi
from getpass import getpass
import re

if __name__ == "__main__":
    env = Environment(undefined = StrictUndefined)
    env.loader = FileSystemLoader("./templates/")

    output = yaml_read_devices("ex4_arista_devices.yml")
    password = getpass()
    filling = "-" * 20
    cfg = list()
    
    for device, device_dict in output.items():

        jinja_vars = device_dict.pop('data')
        template = env.get_template('ex4.j2')
        jinja_cfg = template.render(**jinja_vars)
        intf_name = re.search(r"(.*)\n\s(.*)$", jinja_cfg).group(1)
        ip_address = re.search(r"(.*)\n\s(.*)$", jinja_cfg).group(2)
        cfg = [intf_name, ip_address]
        
        device_dict['password'] = password
        connection = pyeapi.client.connect(**device_dict)
        device_node = pyeapi.client.Node(connection)
        device_node.config(cfg)
        output = device_node.enable("show ip interface brief")
        intf_brief = output[0]['result']['interfaces']
        print()
        print(filling+f" {device} "+filling)
        for intf, intf_dict in intf_brief.items():
            std_out = ""
            ip_address = intf_dict['interfaceAddress']['ipAddr']['address']
            mask = intf_dict['interfaceAddress']['ipAddr']['maskLen']
            intf_status = intf_dict['lineProtocolStatus']
            std_out += f"Interface {intf} -- {ip_address}/{mask} is {intf_status}"
            print(std_out)
        print()

