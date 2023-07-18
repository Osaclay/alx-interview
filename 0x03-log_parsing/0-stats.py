#!/usr/bin/python3

import sys


def print_msg(status_code_counts, total_file_size):
    """
    Method to print
    Args:
        status_code_counts: dictionary of status code counts
        total_file_size: total file size
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_code_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
status_code = 0
line_counter = 0
status_code_counts = {"200": 0,
                     "301": 0,
                     "400": 0,
                     "401": 0,
                     "403": 0,
                     "404": 0,
                     "405": 0,
                     "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                status_code = parsed_line[1]  # status code

                if status_code in status_code_counts.keys():
                    status_code_counts[status_code] += 1

            if line_counter == 10:
                print_msg(status_code_counts, total_file_size)
                line_counter = 0

finally:
    print_msg(status_code_counts, total_file_size)

