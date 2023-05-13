from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.', './templates/'])

my_vars = {"primary_ip": True}

template = env.get_template("intf_config1.j2")
output = template.render(**my_vars)
print(output)

