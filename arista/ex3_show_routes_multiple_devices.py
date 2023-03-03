import pyeapi
from my_funcs import yaml_read_devices, output_printer 
from getpass import getpass

if __name__ == "__main__":
    arista_devices = yaml_read_devices("arista_devices.yml")
    password = getpass()
    
    for device, device_dict in arista_devices.items():
        device_dict['password'] = password    
        connection = pyeapi.client.connect(**device_dict)
        device_node = pyeapi.client.Node(connection)
        output = device_node.enable("show ip route")

        routing_table = output[0]['result']['vrfs']['default']['routes']
        filling = "=" * 20
        print('\n\n'+filling+f"{device}"+filling+'\n')
        for prefix, route_dict in routing_table.items():
            ip_route = prefix
            route_type = route_dict['routeType']
            via = route_dict['vias'][0]['interface']
            if route_type != "static":
                print(f"{ip_route} is a {route_type} route going via {via}")
                #print("-" * 20)
            elif route_type == "static":
                next_hop = route_dict['vias'][0]['nexthopAddr']
                print(f"{ip_route} is a {route_type} route going via {via} with the next-hope {next_hop}")
                #print("-" * 20)

