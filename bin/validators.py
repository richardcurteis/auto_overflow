#!/usr/bin/python3

from IPy import IP

def validate_ip(ip):
    return IP(ip)

def validate_port(port):
    return int(port)