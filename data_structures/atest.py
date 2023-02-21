#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import yaml
from pprint import pprint

filename = input("enter file name: ")
with open(filename) as f:
    #yaml_out = yaml.safe_load(f)
    for dic in yaml.safe_load(f):
        with Netmiko(**dic) as net_con:
            print(net_con.find_prompt())

