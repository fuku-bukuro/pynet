from jnpr.junos import Device
from lxml import etree
from getpass import getpass

juniper_srx = {
    "host": "srx2.lasthop.io",
    "user": "pyclass",
    "password": getpass()
}

a_device = Device(**juniper_srx)
a_device.open()

# show version | display xml rpc

"""
# pyclass@srx2> show version | display xml rpc 
# <rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.1X46/junos">
#     <rpc>
#  ===>>>    <get-software-information>    <<<===============
#         </get-software-information>
#     </rpc>
#     <cli>
#         <banner></banner>
#     </cli>
# </rpc-reply>
"""
# <get-software-information>
#xml_out = a_device.rpc.get_software_information()
#print(etree.tostring(xml_out, encoding="unicode"))

# <get-lldp-neighbors-information>
xml_out = a_device.rpc.get_lldp_neighbors_information()
print(etree.tostring(xml_out, encoding="unicode"))

