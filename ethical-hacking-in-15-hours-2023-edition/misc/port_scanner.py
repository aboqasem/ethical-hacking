#!/usr/bin/env python3

import sys
import socket
from datetime import datetime

if len(sys.argv) != 2:
    print(f'Syntax: {sys.argv[0]} <hostname>')
    exit(1)

hostname = sys.argv[1]
try:
    host = socket.gethostbyname(hostname)
except socket.gaierror:
    print(f"Hostname could not be resolved: {hostname}")
    exit(1)
except socket.error:
    print(f"Could not connect to hostname: {hostname}")
    exit(1)

print("-" * 50)
print(f"Scanning: {host}")
print(f"Time: {datetime.now()}")
print("-" * 50)

socket.setdefaulttimeout(1)
for port in range(50, 85):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"Connecting to {host}:{port}")
        res = s.connect_ex((host, port))
    except KeyboardInterrupt:
        print("Interrupted")
        exit(1)
    finally:
        print(f"Closing connection on {host}:{port}")
        s.close()

    if res == 0:
        print(f"OPEN PORT: {port}")

    print()
    
