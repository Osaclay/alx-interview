#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that checks if a given data set represents a valid
    UTF-8 encoding.
    """
    num_bytes = 0

    check_1 = 1 << 7
    check_2 = 1 << 6

    for i in data:

        check_byte = 1 << 7

        if num_bytes == 0:

            while check_byte & i:
                num_bytes += 1
                check_byte = check_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (i & check_1 and not (i & check_2)):
                    return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
