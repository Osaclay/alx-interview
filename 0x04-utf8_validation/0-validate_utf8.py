#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes_to_check = 0

    for num in data:
        byte = num & 255  # Keep only the 8 least significant bits
        if num_bytes_to_check == 0:
            if byte >> 7 == 0:
                continue  # Single byte character (0xxxxxxx format)
            elif byte >> 5 == 6:
                num_bytes_to_check = 1  # Two bytes character (110xxxxx format)
            elif byte >> 4 == 14:
                num_bytes_to_check = 2  # Three bytes character (1110xxxx format)
            elif byte >> 3 == 30:
                num_bytes_to_check = 3  # Four bytes character (11110xxx format)
            else:
                return False  # Invalid byte

        else:
            if byte >> 6 != 2:
                return False  # Following bytes must be of the format 10xxxxxx
            num_bytes_to_check -= 1

    return num_bytes_to_check == 0

if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
