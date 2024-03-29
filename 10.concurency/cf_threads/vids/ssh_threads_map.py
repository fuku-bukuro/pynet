import time
from concurrent.futures import ThreadPoolExecutor 
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    return net_connect.find_prompt()



if __name__ == "__main__":

    start_time = datetime.now()
    max_threads = 4

    # use context manager to gracefully cleanup the pool
    with ThreadPoolExecutor(max_threads) as pool:
        results_generator = pool.map(ssh_conn, device_list)

        # Results generator 
        for result in results_generator:
            print(result)
        
        end_time = datetime.now()
        print(end_time - start_time)


