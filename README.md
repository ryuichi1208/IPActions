![Py](https://img.shields.io/badge/Python-3.6%2F3.7-blue)
![Lisence](https://img.shields.io/github/license/ryuichi1208/py-dep-kun)
![CI](https://github.com/ryuichi1208/Actions/workflows/Python%20application/badge.svg)

## Project Title

![logs](https://github.com/ryuichi1208/Actions/blob/master/image/actions_log.png)

## Description

IPActions is a tool for calculating network addresses and broadcast addresses from specified IP addresses.

## Features

* Network class calculation
* Network address calculation
* Broadcast address calculation
* Calculate the number of possible hosts

## Tutorial

``` bash
# IP addresses => network addresses / broadcast addresses
$ python3 actions.py 192.168.1.0 /24

IP Address Bin/Hex : ['11000000', '10101000', '00000001', '00000000'] ['c0', 'a8', '01', '00']
SubnetMask Bin/Hex : ['11111111', '11111111', '11111111', '00000000'] ['ff', 'ff', 'ff', '00']
Class              : C
IP Address         : 192.168.1.0
SubnetMask         : 255.255.255.0 (cidr:24)
IP/Host nums       : 256 / 254

Network Address : 192.168.1.0
BroadCast Address : 192.168.1.255
```

## Requirement

```
OS
 => MacOS or Linux(CentOS)
python version
 => 3.8
python packages
 => See requirements.txt
```

## Installation

``` bash
$ git clone https://github.com/ryuichi1208/Actions.git && cd Actions
$ make test && sudo make install
```

## Authors

* [ryuichi1208](https://github.com/ryuichi1208)

## References

* [What's New in Python](https://docs.python.org/ja/3.8/whatsnew/index.html)

## License

* [Apache License 2.0](https://github.com/ryuichi1208/Actions/blob/master/LICENSE)
