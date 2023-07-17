#!/usr/bin/python3

import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split()
    if len(parts) >= 7:
        status_code = parts[-2]
        file_size = int(parts[-1])
        return status_code, file_size
    return None, None

if __name__ == "__main__":
    total_size = 0
    status_codes = {
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
        count = 0
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code and file_size:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            count += 1
            if count == 10:
                print_stats(total_size, status_codes)
                count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
