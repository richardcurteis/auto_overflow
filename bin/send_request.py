#!/usr/bin/python3

import socket
import sys

class Send:

    def __init__(self, target):
        self.ip = target.ip
        self.port = target.port
        self.path = target.path

    def send_payload(self, payload):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((self.ip, self.port))
            s.recv(1024)

            s.send((self.path + payload))
            s.close()
        except Exception as e:
            print(f"Exception In send: {e}")
            sys.exit()


