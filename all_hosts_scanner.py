import nmap

def scan_all_hosts(network):
    nm = nmap.PortScanner()
    print(f"Scanning network: {network}")
    nm.scan(hosts=network, arguments='-sn')  
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print(f"Host: {host} is {status}")

if __name__ == "__main__":
    network = input("Enter the network to scan (e.g., 192.168.1.0/24): ")
    scan_all_hosts(network)
