import sys
import socket

def scan_ports(target_ip):
    open_ports = []
    ports_to_check = [21, 22, 23, 25, 53, 80, 110, 143, 443, 587, 3306, 8080]  # Ports courants
    print(f"Scanning {target_ip}...")
    
    for port in ports_to_check:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout de 1 seconde
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scan.py <IP>")
        sys.exit(1)

    ip = sys.argv[1]
    open_ports = scan_ports(ip)

    if open_ports:
        print(f"Ports ouverts sur {ip} : {', '.join(map(str, open_ports))}")
    else:
        print(f"Aucun port ouvert trouvé sur {ip}.")
