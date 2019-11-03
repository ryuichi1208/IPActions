import os
import sys
import socket


def foward_lookup_name(hostname: str) -> str:
    try:
        ipaddr = socket.gethostbyname(hostname)
        print(ipaddr)
    except socket.gaierror:
        print("Not found arg hostname")

if __name__ == "__maine__":
    pass
