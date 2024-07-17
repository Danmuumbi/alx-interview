#!/usr/bin/python3

import sys
import signal

def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key in sorted(dict_sc.keys()):
        if dict_sc[key] != 0:
            print("{}: {}".format(key, dict_sc[key]))

def signal_handler(sig, frame):
    print_msg(dict_sc, total_file_size)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        if len(parsed_line) < 2:
            continue
        try:
            file_size = int(parsed_line[-1])
            status_code = parsed_line[-2]
        except ValueError:
            continue

        total_file_size += file_size
        if status_code in dict_sc:
            dict_sc[status_code] += 1

        counter += 1
        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0
finally:
    print_msg(dict_sc, total_file_size)
