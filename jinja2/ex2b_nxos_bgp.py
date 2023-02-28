from __future__ import unicode_literals, print_function
from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("./templates/")


template = env.get_template("nxos_ipv4_intf.j2")
nxos1 = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.1",
    "netmask": 24,
    "peer_ip": "10.1.100.2",
    "as_no": 22
}

nxos2 = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.2",
    "netmask": 24,
    "peer_ip": "10.1.100.1",
    "as_no": 22
}

for device in (nxos1, nxos2):
    output = template.render(**device)
    print(output)

