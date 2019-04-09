#!/usr/bin/python3

from IPy import IP

def is_valid_ip(ip):
    return IP(ip)

def is_valid_port(port):
    return int(port) and (port > 0 and port < 65533)