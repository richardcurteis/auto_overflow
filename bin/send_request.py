#!/usr/bin/python3

import socket


class Send:

    def __init__(self, target):
        self.ip = target.ip
        self.port = target.port
        self.path = target.path

    def send_payload(self, payload):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((self.ip, self.port))
        s.recv(1024)

        s.send((self.path + payload).encode())
        s.close()


