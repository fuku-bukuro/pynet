#!/usr/bin/evn python
import yaml
# transform data to the YAML format
my_data = {
    'device_name': 'rtr1',
    'ip_addr': '10.1.1.1',
    'username': 'admin',
    'password': 'foo',
}

some_list = list(range(10))
my_data['some_list'] = some_list
my_data['null_value'] = None
my_data['a_bool'] = False

filename = 'outfile.yml'

with open(filename, 'wt') as f:
    yaml.dump(my_data, f, indent = 4)

# Print to stdout as Python representation
print("Python")
print("#" * 10)
pprint(my_data)
print()
print("JSON")
print("#" * 10)
print(json.dumps(my_data)) """ dumps aka dump string"""
