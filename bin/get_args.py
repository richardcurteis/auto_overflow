#!/usr/bin/python3

import argparse

def input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-ip',
                        type=str,
                        required=True)

    parser.add_argument('-port',
                        type=str,
                        required=True)

    parser.add_argument('-path',
                        type=str,
                        required=True,
                        default='/')

    return parser.parse_args()