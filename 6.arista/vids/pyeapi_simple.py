import pyeapi
from getpass import getpass
import ipdb

ipdb.set_trace()
connection = pyeapi.client.connect(
    transport = "https",
    host = "arista3.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = "443",
)

# enable = getpass("input enable password: ")
# device = pyeapi.client.Node(connection, enablepwd = enable)

device = pyeapi.client.Node(connection)

