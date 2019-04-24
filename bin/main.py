#!/usr/bin/python3

from get_args import input_args
from target import Target
import sys
from IPy import IP
from enum_target import Enum


class Main:

    def main(self):
        args = input_args()

        if IP(args.ip) or 'localhost' and (type(args.port) is int and 0 < args.port <= 65533):

            target_dict = {'ip': args.ip,
                           'port': args.port,
                           'path': args.path,
                           'enumerated': False}

            target = Target(target_dict)

            if args.enum:
                enum = Enum()
                # Will return a modified 'target' dictionary
                target = enum.enumerate(args, target)
            else:
                if target.enumerated:
                    pass
                else:
                    pass
            pass
                # pwn module here

            sys.exit()

        else:
            print("Invalid Arguments")
            sys.exit()


if __name__ == "__main__":
    m = Main()
    m.main()
