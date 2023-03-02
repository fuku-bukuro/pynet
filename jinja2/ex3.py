from __future__ import print_function, unicode_literals
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("./templates/")


vars = {
    "vrf_name": "pink",
    "rd_number": "100:1",
#    "ipv4": True,
#    "ipv6": True
}

template = env.get_template("ex3.j2")
output = template.render(**vars)
print(output)

