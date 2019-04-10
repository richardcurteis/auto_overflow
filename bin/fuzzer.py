#!/usr/bin/python3

from time import sleep
from send_request import Send


class Fuzz:

    def __init__(self, target):
        self.TARGET = target

    def find_crash(self, fuzz_len):

        buffer = "A" * fuzz_len
        s = Send(self.TARGET)

        while True:
            try:
                s.send_payload(buffer)
                sleep(1)
                buffer = buffer + "A" * fuzz_len
            except:
                return len(buffer)


