from ncclient import manager
from getpass import getpass
from pprint import pprint

#using a content manager
with manager.connect(
    host = "srx2.lasthop.io",
    #host = "cisco3.lasthop.io",
    port = 830, #netconf port
    username = "pyclass",
    password = getpass(),
    hostkey_verify = False, #turn off SSH hostkey verification - check if appropiate!
    allow_agent = False, #not to use ssh agent
    look_for_keys = False #not to use automatically for SSH keys
) as netconf_manager:
    
    #call server capabilities
    pprint(netconf_manager.server_capabilities.__dict__)

