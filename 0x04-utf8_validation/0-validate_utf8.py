#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    num_bytes_to_check = 0

    first_byte_mask = 1 << 7
    continuation_byte_mask = 1 << 6

    for num in data:

        current_byte_mask = 1 << 7

        if num_bytes_to_check == 0:

            while current_byte_mask & num:
                num_bytes_to_check += 1
                current_byte_mask = current_byte_mask >> 1

            if num_bytes_to_check == 0:
                continue

            if num_bytes_to_check == 1 or num_bytes_to_check > 4:
                return False

        else:
            if not (num & first_byte_mask and not (num & continuation_byte_mask)):
                return False

        num_bytes_to_check -= 1

    if num_bytes_to_check == 0:
        return True

    return False
