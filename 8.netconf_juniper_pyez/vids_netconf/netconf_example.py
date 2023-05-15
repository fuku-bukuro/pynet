import ipdb
from ncclient import manager
from getpass import getpass
from pprint import pprint
#from ncclilent.xml_ import new_ele

conn = manager.connect(
    host = "srx2.lasthop.io",
    username = "pyclass",
    password = getpass(),
    device_params = {"name": "junos"},
    hostkey_verify = False,
    allow_agent = False,
    look_for_keys = False,
    port = 830,
    timeout = 60,
)

#drop us in the python debugger
#use 'n' to run the next step when in debugger
#use 'l' to list what was executd already/where you are with the execution
ipdb.set_trace()
config = conn.get_config(source = "running")
config_xml = config.data_xml
pprint(config_xml)
