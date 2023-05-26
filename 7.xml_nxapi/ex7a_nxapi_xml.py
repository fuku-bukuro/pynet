import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
#from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format = "xml",
    host = "nxos1.lasthop.io",
    username = "pyclass",
    password = getpass(),
    transport = "https",
    port = 8443,
    verify = False
)

output = device.show("show interface Ethernet1/1")
print(
    "Interface: {}; State: {}; MTU: {}".format(
        output.find(".//interface").text,
        output.find(".//state").text,
        output.find(".//eth_mtu").text,
    )
)
    
