import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport = "https",
    host = "arista3.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = "443"
)

device = pyeapi.client.Node(connection)
# cannot use short versions of commands as this is not actually CLI but eAPI
output = device.enable(["show version", "show ip arp"])
print(output)

