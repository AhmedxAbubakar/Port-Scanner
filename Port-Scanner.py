import socket

def scan_ports(ip, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()

target_ip = input("Enter IP to scan: ")
port_range = range(20, 1025)
scan_ports(target_ip, port_range)
