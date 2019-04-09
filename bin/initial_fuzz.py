#!/usr/bin/python3

from time import sleep
from send_request import Send
import sys

def find_crash(target):

    buffer = "A" * 100
    s = Send(target)
    
    while True:
        try:
            s.send_payload(buffer)
            sleep(1)
            buffer = buffer + "A" * 100
        except Exception as e:
            print("Exception: " + str(e))
            return len(buffer)