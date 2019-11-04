import os
import pytest
import sys
import actions
import nslookup

def test_block_inf():
    with pytest.raises(SystemExit) as exc:
        actions.block_info()
    assert exc.value.code == 0


def test_usage():
    with pytest.raises(SystemExit) as exc:
        actions.usage("test error message")
    assert exc.value.code == 1


def test_calc_host_nums():
    assert actions.calc_host_nums("11111111111111111111111111111111") == 1
    assert actions.calc_host_nums("11111111111111111111111111110000") == 16
    assert actions.calc_host_nums("11111111111111111111111100000000") == 256
    assert actions.calc_host_nums("11111111111111111111000000000000") == 4096
    assert actions.calc_host_nums("11111111111111110000000000000000") == 65536
    assert actions.calc_host_nums("11111111111100000000000000000000") == 1048576


def test_calc_ip_class_type():
    assert actions.calc_ip_class_type("10.168.1.0") == "A"
    assert actions.calc_ip_class_type("10.255.122.0") == "A"
    assert actions.calc_ip_class_type("172.168.1.0") == "B"
    assert actions.calc_ip_class_type("172.0.1.255") == "B"
    assert actions.calc_ip_class_type("192.168.1.0") == "C"
    assert actions.calc_ip_class_type("192.0.1.0") == "C"
    assert actions.calc_ip_class_type("111.111.111.111") == None


def test_foward_lookup_name():
    assert nslookup.foward_lookup_name("google.com") == None
    assert nslookup.foward_lookup_name("exmaple.v4.com") == None
