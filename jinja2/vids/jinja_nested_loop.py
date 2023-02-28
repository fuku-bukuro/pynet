from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(['.', './templates/'])

base_intf = "GigabitEthernet0/"
intf_list = list()

for slot in range(1,4):
    for intf in range(1,25):
        intf_name = f"{base_intf}{slot}/{intf}"
        intf_list.append(intf_name)

my_vars = {
"intf_list": intf_list}

template = env.get_template("intf_config4.j2")
with open("interface_config.cfg", "w") as f:
    output = template.render(**my_vars)
    f.write(output)


