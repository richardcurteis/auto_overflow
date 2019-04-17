#!/usr/bin/python3

from get_args import input_args
from fuzzer import Fuzz
from target import Target
import sys
from IPy import IP
from create_pattern import Pattern
import user_input


class Main:

    def __init__(self):
        self.pattern = Pattern()

    def main(self):
        args = input_args()
        self.pattern = Pattern()

        if IP(args.ip) or 'localhost' and (type(args.port) is int and 0 < args.port < 65533):

            target_dict = {'ip': args.ip,
                           'port': args.port,
                           'path': args.path}

            target = Target(target_dict)
            fuzz = Fuzz(target)

            if args.eip:
                fuzz.confirm_eip(args.eip)
                sys.exit()

            fuzz_length = args.len if args.len else 100

            # bytes to crash program
            crash_bytes = fuzz.find_crash(fuzz_length)
            print(f"[*] Program crashed at {crash_bytes} bytes...")

            # Create pattern from crash bytes plus 300 byte padding
            pat = self.get_pattern(crash_bytes)

            # Reset application
            user_input.get_input("DEBUG: User reset debugger...")

            # Send pattern to application to identify EIP overwrite
            fuzz.locate_eip(pat)

            # Get EIP value from user
            eip_query = user_input.get_input("[*] Enter EIP Value")

            # Find position of EIP query in string
            # NOTE: Decodes EIP hex to ascii before passing
            # Reverses result due to little endianness
            offset = self.get_offset(eip_query)

            fuzz.confirm_eip(offset)

        else:
            print("Invalid Arguments")
            sys.exit()

    def get_pattern(self, crash_bytes):
        return self.pattern.create_pattern(crash_bytes + 300)

    def get_offset(self, eip_query):
        clear_text = bytearray.fromhex(eip_query).decode()[::-1]
        return self.pattern.find_offset(clear_text)


if __name__ == "__main__":
    m = Main()
    m.main()
