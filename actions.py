#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import numpy
import os
import sys
import pprint
import platform
import nslookup


def block_info():
    """
    Command lib version
    """
    print("Python", platform.python_version())
    print("numpy", numpy.__version__)
    sys.exit(0)


def usage(msg: str):
    """
    Command usage
    """
    print(f"{msg}")
    print(f"Usage : {os.path.basename(__file__)} IPAddress Subnetmask")
    sys.exit(1)


@functools.lru_cache(maxsize=128)
def ipaddr_to_bin(num: str, t: int) -> list:
    """
    Receives an IP address as a character string,
    converts it to a decimal number received as
    an argument for each octet, and returns it as a list.
    """
    if num.count(".") != 3:
        usage("invalid arguments")

    ctype = "b" if t == 2 else "x"
    fill = 8 if ctype == "b" else 2
    try:
        ipaddr = [format(int(i), ctype).zfill(fill) for i in num.split(".")]
    except ValueError:
        ipaddr = None

    return ipaddr


def calc_network_address(*iplist):
    """
    Calculate network address and standard output
    """
    L = [".", ".", ".", "\n"]
    print("Network Address : ", end="")
    for i in range(4):
        print(numpy.bitwise_and(int(iplist[0][i]), int(iplist[1][i])), end=L[i])


def calc_broad_cast_address(*iplist):
    """
    Calculate broadcast address and standard output
    """
    L = [".", ".", ".", "\n"]
    print("BroadCast Address : ", end="")
    tmp_addr = []
    for i in range(4):
        if iplist[1][i] != "11111111":
            for j in range(8):
                if iplist[0][i][j] == "0" and iplist[1][i][j] == "0":
                    tmp_addr.append("1")
                else:
                    tmp_addr.append(iplist[0][i][j])
            else:
                print(int("".join(tmp_addr), 2), end=L[i])
        else:
            print(int(iplist[0][i], 2), end=L[i])


def calc_host_nums(netmask: str) -> int:
    """
    Calculates the number of possible IP addresses and the number
    of hosts and returns an int type number.
    """
    return 2 ** sum([i.count("0") for i in netmask])


def opt_parse(args: list) -> tuple:
    """
    Parse options received from CLI and return in array
    Subnet mask / cider notation is also performed without function
    """
    if len(args) >= 1:
        pass
    elif platform.system() == "Darwin":
        # print("mac")
        pass
    else:
        usage("invalid arguments")

    if "-i" in args or "--interactive" in args:
        ip, subnet = map(str, input().split())
    elif "-m" in args:
        nslookup.foward_lookup_name(args[2])
        sys.exit(0)
    elif "-b" in args:
        block_info()
    elif "." not in args[2] or "/" in args[2]:
        ip = args[1]
        subnet = args[2].replace("/", "", 2)
        subnet = "".join(["1" for i in range(int(subnet))])
        subnet = subnet + "".join(["0" for i in range(32 - len(subnet))])
        subnet = (
            str(int(subnet[0:8], 2))
            + "."
            + str(int(subnet[8:16], 2))
            + "."
            + str(int(subnet[16:24], 2))
            + "."
            + str(int(subnet[24:32], 2))
        )
    else:
        ip = args[1]
        subnet = args[2]

    return args[1], subnet


def calc_ip_class_type(ipaddr: str) -> str:
    return (
        "C"
        if ipaddr.split(".")[0] == "192"
        else "B"
        if ipaddr.split(".")[0] == "172"
        else "A"
        if ipaddr.split(".")[0] == "10"
        else None
    )


def main(args: list):

    ipaddr, netmask = opt_parse(args)

    hnums = calc_host_nums(ipaddr_to_bin(netmask, 2))

    ip_info = f"""
IP Address Bin/Hex : {ipaddr_to_bin(ipaddr, 2)} {ipaddr_to_bin(ipaddr, 16)}
SubnetMask Bin/Hex : {ipaddr_to_bin(netmask, 2)} {ipaddr_to_bin(netmask, 16)}
Class              : {calc_ip_class_type(ipaddr)}
IP Address         : {ipaddr}
SubnetMask         : {netmask} (cidr:{sum([bin(int(x)).count("1") for x in netmask.split(".")])})
IP/Host nums       : {hnums} / {hnums-2}
    """
    print(ip_info)

    calc_network_address(ipaddr.split("."), netmask.split("."))
    calc_broad_cast_address(ipaddr_to_bin(ipaddr, 2), ipaddr_to_bin(netmask, 2))


if __name__ == "__main__":
    args = sys.argv if len(sys.argv) >= 1 else usage("Invalid args")
    main(args)
