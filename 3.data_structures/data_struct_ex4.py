import json
from pprint import pprint

with open('arp.json') as f:
    arista_arp = json.load(f)

arp_dict = {}
arp_entries = arista_arp["ipV4Neighbors"]

for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr

print(arp_dict)
