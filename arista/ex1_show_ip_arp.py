import pyeapi
from pprint import pprint
from getpass import getpass

arista3 = {
    "transport": "https",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "port": "443",
}

connection = pyeapi.client.connect(**arista3)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

print()
print("-" * 40)
arp_list = output[0]['result']['ipV4Neighbors']
for arp_entry in arp_list:
    mac_address = arp_entry['hwAddress']
    ip_address = arp_entry['address']
    #print("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))
    print(f"{ip_address} ---> {mac_address}")
print("-" * 40)
print()

#ip_arp_list = list()
#for i in output:
#    for k,v in i.items():
#        arp_entry = {
#            "ip_addr": i['address'],
#            "mac_addr": i['hwAddress']
#            }
#    ip_arp_list.append(arp_entry)
#pprint(ip_arp_list)

