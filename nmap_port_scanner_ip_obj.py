import socket
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

print(r"""
 ____  _       _                               _     _     ____
/ ___|(_)_ __ | |__   ___ ___  _ __ ___  ___  | |   | |   |  _ \
\___ \| | '_ \| '_ \ / __/ _ \| '_ ` _ \/ __| | |   | |   | |_) |
 ___) | | | | | | | | (_| (_) | | | | | \__ \ | |___| |___|  __/
|____/|_|_| |_|_| |_|\___\___/|_| |_| |_|___/ |_____|_____|_|

""")
print("\n****************************************************************")
print("\n* Copyright of Sinhcoms LLP, 2021                              *")
print("\n* https://www.sinhcoms.com                                     *")
print("\n* https://instagram.com/cicada330.one                          *")
print("\n* https://www.github.com/Sinhcoms-LLP                          *")
print("\n****************************************************************")

open_ports = []
# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

# Basic socket port scanning
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            # If the following line runs then then it was successful in connecting to the port.
            open_ports.append(port)

    except:
        pass
for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")
