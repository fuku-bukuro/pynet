import yaml
from netmiko import Netmiko
from os import path
from ciscoconfparse import CiscoConfParse

#filename = input('your yaml list of devices please: ')

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    output = yaml.safe_load(f)

cisco4 = output["cisco4"]
with Netmiko(**cisco4) as net_con:
    parse = CiscoConfParse(net_con.send_command("show run").splitlines())

for obj in parse.find_objects(r"^interface"):
    if obj.re_search_children(r"^\sip address"):
        ip = (obj.re_search_children(r"^\sip address")[0].text).strip()
        print("Interface Line: {}".format(obj.text))
        print("IP address Line: {}".format(ip))

