# for python 2/3 compatibily
from __future__ import unicode_literals, print_function
# jinja stuff
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
#env.loader = FileSystemLoader('.')
env.loader = FileSystemLoader("./templates/")
#env.loader = FileSystemLoader([".",'./templates/'])

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "10.20.30.1"
}


template = env.get_template("bgp_config.j2")
output = template.render(**my_vars)

print(output)

