from pprint import pprint
import re

output = """Protocol Address Age Hardware Addr Type Interface
Internet 10.220.88.1 67 0062.ec29.70fe ARPA Gi0/0/0
Internet 10.220.88.20 29 c89c.1dea.0eb6 ARPA Gi0/0/0
Internet 10.220.88.22 - a093.5141.b780 ARPA Gi0/0/0
Internet 10.220.88.37 104 0001.00ff.0001 ARPA Gi0/0/0
Internet 10.220.88.38 161 0002.00ff.0001 ARPA Gi0/0/0"""

output_list = output.splitlines()

final_list = list()
for line in output_list[1:]:
    dick = re.search(r"^Internet (?P<ip_addr>\S+) \S+ (?P<mac_addr>\S+) \S+ (?P<interface>\S+)$", line).groupdict()
    final_list.append(dick)

pprint(final_list)

