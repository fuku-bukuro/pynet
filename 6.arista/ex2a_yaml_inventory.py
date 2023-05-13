import pyeapi
import yaml
from pprint import pprint
from getpass import getpass

password = getpass()

with open("arista4.yml") as f:
    arista4 = yaml.safe_load(f.read())

arista4['password'] = password

connection = pyeapi.client.connect(**arista4)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

print()
print("-" * 40)
arp_list = output[0]['result']['ipV4Neighbors']
for arp_entry in arp_list:
    mac_address = arp_entry['hwAddress']
    ip_address = arp_entry['address']
    print(f"{ip_address} ---> {mac_address}")

print("-" * 40)
print()
