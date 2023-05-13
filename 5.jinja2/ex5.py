from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("./templates/")


my_vars = {
    "timezone": "PST",
    "timezone_offset": "-8 0",
    "timezone_dst": "PDT",
    "ntp_server1": "130.126.24.24",
    "ntp_server2": "152.2.21.1"
}

template_file = env.get_template("cisco3_config.j2")
output = template_file.render(**my_vars)
print(output)
