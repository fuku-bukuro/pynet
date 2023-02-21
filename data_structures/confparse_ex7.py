from ciscoconfparse import CiscoConfParse
import re

parse = CiscoConfParse('bgp.cfg')
neighbors = parse.find_objects(r" neighbor")

neighbor_list = list()
for neighbor in neighbors:
    neighbor_ip = re.search(r" \S+ (\S+)", neighbor.text).group(1)
    neighbor_as = re.search(r".+ (\d+)$", neighbor.re_search_children(r"remote-as")[0].text).group(1)
    neighbor_entry = (neighbor_ip, neighbor_as)
    neighbor_list.append(neighbor_entry)

print(neighbor_list)

