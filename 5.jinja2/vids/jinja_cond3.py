from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(['.', './templates/'])

my_vars = {
    "bgp_peer1": True,
    "peer_ip": "10.20.30.92",
    "bgp_policy": False,
}

template = env.get_template('bgp_config2.j2')
output = template.render(**my_vars)
print(output)

