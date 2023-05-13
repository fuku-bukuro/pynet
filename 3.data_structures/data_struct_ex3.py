import json
from pprint import pprint

filename = input("your json filename please: ")

ipv4_list = list()
ipv6_list = list()
with open(filename) as f:
   file_out =  json.load(f)

for intf in file_out:
    for ip in file_out[intf]:
        if ip == 'ipv4':
            for i in file_out[intf][ip]:
                ipv4 = str(i)
                mask = str(file_out[intf][ip][i]['prefix_length'])
                ipv4_list.append(ipv4+"/"+mask)

        elif ip == 'ipv6':
            for i in file_out[intf][ip]:
                ipv6 = str(i)
                mask = str(file_out[intf][ip][i]['prefix_length'])
                ipv6_entry = (ipv6, mask)
                ipv6_list.append(ipv6+"/"+mask)

pprint(ipv4_list)
print("+" * 50)
pprint(ipv6_list)
