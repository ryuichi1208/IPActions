#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import numpy
import os
import sys
import pprint
import platform


def usage(msg: str):
    """
    エラー関連(とりあえず全部ここ？)
    """
    print(f"{msg}")
    print(f"Usage : {os.path.basename(__file__)} IPAddress Subnetmask")
    sys.exit(1)


@functools.lru_cache(maxsize=128)
def ipaddr_to_bin(num: str, t:int) -> list:
    """
    IPアドレスの各オクテットを指定された進数へ変換する
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
    ネットワークアドレスを計算する
    """
    L = [".", ".", ".", "\n"]
    print("Network Address : ", end="")
    for i in range(4):
        print(numpy.bitwise_and(int(iplist[0][i]), int(iplist[1][i])), end=L[i])


def calc_broad_cast_address(*iplist):
    """
    ブロードキャストアドレスを計算する
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


def calc_host_nums(netmask):
    """
    アドレス数とホスト数を算出
    """
    return 2 ** sum([i.count("0") for i in netmask])


def opt_parse(args: list) -> tuple:
    """
    オプション解析処理
    """
    if len(args) == 3:
        pass
    elif platform.system() == "Darwin":
        print("mac")
    else:
        usage("invalid arguments")

    return args[1], args[2]


def calc_ip_class_type(ipaddr):
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
    args = sys.argv
    main(args)
