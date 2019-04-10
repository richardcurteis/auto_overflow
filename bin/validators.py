#!/usr/bin/python3

from IPy import IP


def is_valid_ip(ip):
    return IP(ip)


def is_valid_port(port):
    return 0 < port < 65533
