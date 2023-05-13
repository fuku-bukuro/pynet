import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport = "https",
    host = "arista3.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = "443"
)

cfg = [
    "vlan 225",
    "name green",
    "vlan 226",
    "name red",
]


device = pyeapi.client.Node(connection)
# cannot use short versions of commands as this is not actually CLI but eAPI
output = device.config(cfg)
print(output)

