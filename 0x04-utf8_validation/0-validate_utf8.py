#!/usr/bin/python3

"""
A method that determines if a given data set represents a valid
UTF-8 encoding.
"""

def validUTF8(data):
    # Loop through each byte in the data list
    i = 0
    while i < len(data):
        # Get the current byte
        current_byte = data[i]
        
        # If the byte starts with '0', it's a single-byte character
        if current_byte >> 7 == 0:
            i += 1
            continue
        # If the byte starts with '110', it's a 2-byte character
        elif current_byte >> 5 == 0b110:
            # Check that we have enough bytes for a 2-byte character
            if i + 1 >= len(data) or data[i+1] >> 6 != 0b10:
                return False
            i += 2
        # If the byte starts with '1110', it's a 3-byte character
        elif current_byte >> 4 == 0b1110:
            # Check that we have enough bytes for a 3-byte character
            if i + 2 >= len(data) or data[i+1] >> 6 != 0b10 or data[i+2] >> 6 != 0b10:
                return False
            i += 3
        # If the byte starts with '11110', it's a 4-byte character
        elif current_byte >> 3 == 0b11110:
            # Check that we have enough bytes for a 4-byte character
            if i + 3 >= len(data) or data[i+1] >> 6 != 0b10 or data[i+2] >> 6 != 0b10 or data[i+3] >> 6 != 0b10:
                return False
            i += 4
        else:
            # Invalid byte format
            return False
    return True

