#!/usr/bin/python3

from get_args import input_args
from validators import validate_ip, validate_port
from initial_fuzz import find_crash
from target import Target

def main():
    args = input_args()

    if validate_ip and validate_port:
        args.port = int(args.port)
        target_dict = { 'ip' : args.ip,
                        'port' : args.port,
                        'path' : args.path}
    
        target = Target(target_dict)

        crash_bytes = find_crash(target)
        print(f"Crashed at {str(crash_bytes)} bytes...\n")
    






if __name__ == "__main__":
    main()