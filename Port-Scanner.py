import socket
import threading
from queue import Queue

print_lock = threading.Lock()

def scan_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                sock.send(b"HEAD / HTTP/1.1\r\nHost: google.com\r\n\r\n")
                banner = sock.recv(100).decode(errors="ignore").strip()
            except:
                banner = "No banner"
            with print_lock:
                print(f"[+] Port {port} is open | Banner: {banner}")
        sock.close()
    except:
        pass

def threader():
    while True:
        port = q.get()
        scan_port(target_ip, port, timeout)
        q.task_done()

# Get user input
target_ip = input("Enter IP to scan: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))
timeout = float(input("Timeout per port (seconds): "))

# Queue for threading
q = Queue()
for _ in range(100):  # 100 threads
    t = threading.Thread(target=threader, daemon=True)
    t.start()

print(f"\n🔍 Scanning {target_ip} from port {start_port} to {end_port}...\n")
for port in range(start_port, end_port + 1):
    q.put(port)

q.join()
print("\n✅ Scan complete.")
