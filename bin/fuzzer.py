#!/usr/bin/python3

from time import sleep
from send_request import Send


class Fuzz:

    def __init__(self, target):
        self.TARGET = target

    def find_crash(self):

        buffer = "A" * 100
        s = Send(self.TARGET)

        while True:
            try:
                s.send_payload(buffer)
                sleep(1)
                buffer = buffer + "A" * 100
            except TypeError:
                return len(buffer)


