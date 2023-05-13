import pyeapi
from my_funcs import yaml_read_device, output_printer 


if __name__ == "__main__":
    arista4 = yaml_read_device("arista4.yml")

    connection = pyeapi.client.connect(**arista4)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip route")

    routing_table = output[0]['result']['vrfs']['default']['routes']

    for prefix, route_dict in routing_table.items():
        ip_route = prefix
        route_type = route_dict['routeType']
        via = route_dict['vias'][0]['interface']
        if route_type != "static":
            print(f"\n{ip_route} is a {route_type} route going via {via}")
            print("-" * 20)
        elif route_type == "static":
            next_hop = route_dict['vias'][0]['nexthopAddr']
            print(f"\n{ip_route} is a {route_type} route going via {via} with the next-hope {next_hop}")
            print("-" * 20)

