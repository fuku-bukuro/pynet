import yaml
from pprint import pprint

cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io", "device_type": "cisco_xe"}

cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io", "device_type": "cisco_xe"}

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io", "device_type": "arista_eos"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io", "device_type": "arista_eos"}

my_devices = [cisco3, cisco4, arista1, arista2]
for device in my_devices:
    device["username"] = "admin"
    device["password"] = "cisco123"

print()
pprint(my_devices)
print()

with open("my_devices.yml", "w") as f:
    yaml.dump(my_devices, f, default_flow_style=False)
