#!/usr/bin/python3


class Target:
    def __init__(self, target):
        self.ip = target['ip']
        self.port = target['port']
        self.path = target['path']
        self.enumerated = target['enumerated']