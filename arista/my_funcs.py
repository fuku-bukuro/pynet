import yaml
from getpass import getpass


def yaml_read_device(file_name):
    with open(file_name) as f:
        password = getpass()
        device = yaml.safe_load(f.read())
        device['password'] = password
    return device

def yaml_read_devices(file_name):
    with open(file_name) as f:
        device_list = yaml.safe_load(f.read())
        #for device, device_dict in device_list.items():
        #    password = getpass()
        #    device_dict['password'] = password
    #return device, device_dict
    return device_list

def output_printer(output):
    arp_list = output[0]['result']['ipV4Neighbors']
    final = "\n" 
    for arp_entry in arp_list:
        mac_address = arp_entry['hwAddress']
        ip_address = arp_entry['address']
        final += f"{ip_address} ---> {mac_address}\n"
    print()
    print("-" * 40)
    print(final)
    print("-" * 40)
    print()

