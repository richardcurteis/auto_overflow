#!/usr/bin/python3

from get_args import input_args
from initial_fuzz import find_crash
from target import Target
import sys
from IPy import IP


def main():
    args = input_args()

    if IP(args.ip) and 0 < args.port < 65533:
        try:
            args.port = int(args.port)
        except TypeError:
            print(f"[!] Invalid Port {args.port}. Must be type integer")
        finally:
            sys.exit()

        target_dict = { 'ip' : args.ip,
                        'port' : args.port,
                        'path' : args.path}
    
        target = Target(target_dict)

        crash_bytes = find_crash(target)
        print(f"Crashed at {str(crash_bytes)} bytes...\n")


if __name__ == "__main__":
    main()