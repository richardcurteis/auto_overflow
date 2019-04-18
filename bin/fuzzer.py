#!/usr/bin/python3

from time import sleep
from send_request import Send
from create_pattern import Pattern


class Fuzz:

    def __init__(self, target):
        self.s = Send(target)

    def find_crash(self, fuzz_len):

        buffer = "A" * fuzz_len

        while True:
            try:
                self.s.send_payload(buffer)
                sleep(1)
                buffer = buffer + "A" * fuzz_len
            except:
                return len(buffer)

    def locate_eip(self, pattern='', length=0):
        if length > 0:
            pat = Pattern()
            pattern = pat.create_pattern(length)
        try:
            self.s.send_payload(pattern)
        except Exception as e:
            print(str(e))
            print("Program crashed...\n")

    def send_payload(self, payload):
        try:
            self.s.send_payload(payload)
        except Exception as e:
            print(str(e))
            print("Program crashed...\n")

    def is_target_up(self):
        while True:
            try:
                self.s.send_payload('A')
                print('[!] Target back up. Continuing...\n')
                return True
            except:
                sleep(1)
                pass
