import socket
import threading

ip = input("Enter IP: ")

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    result = s.connect_ex((ip, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "Unknown"

        print(f"{ip}:{port} OPEN {service}")

    s.close()


for port in range(1, 1025):  # keep range small
    t = threading.Thread(target=scan, args=(port,))
    t.start()