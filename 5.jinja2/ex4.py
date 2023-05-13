from __future__ import print_function, unicode_literals
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("./templates/")

vrfs = {
    "white": "100:1",
    "blue": "200:1",
    "red": "300:1",
    "green": "400:1",
    "yellow": "500:1"
}
vars = {
    "vrfs": vrfs,
    "ipv4": True,
    "ipv6": True
}

template = env.get_template("ex4.j2")
output = template.render(**vars)
print(output)

