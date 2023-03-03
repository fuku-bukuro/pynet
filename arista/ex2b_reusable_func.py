import pyeapi
from my_funcs import device_def, output_printer 


arista4 = device_def("arista4.yml")

connection = pyeapi.client.connect(**arista4)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

output_printer(output)

