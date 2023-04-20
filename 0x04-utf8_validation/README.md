# UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer


## Algorithm

In UTF-8 encoding, characters can be represented using 1 to 4 bytes, depending on the character's Unicode code point. Here's a detailed explanation of how the implementation checks for valid UTF-8 byte formats:

For single-byte characters:

UTF-8 single-byte characters start with a '0' as the most significant bit (MSB). So, we check if the MSB of the current byte is '0' by shifting the byte 7 bits to the right and comparing with 0: current_byte >> 7 == 0. If it's '0', then the byte is a valid single-byte character and we move on to the next byte.
For two-byte characters:

UTF-8 two-byte characters start with '110' as the first three bits. So, we check if the first three bits of the current byte are '110' by shifting the byte 5 bits to the right and comparing with 0b110: current_byte >> 5 == 0b110.
Next, we check if we have enough bytes for a two-byte character by checking if the next byte (i+1) starts with '10' as the first two bits, which is indicated by data[i+1] >> 6 == 0b10.
If both conditions are true, then the current byte and the next byte together form a valid two-byte character, and we move on to the byte after the next byte (i+2).
For three-byte characters:

UTF-8 three-byte characters start with '1110' as the first four bits. So, we check if the first four bits of the current byte are '1110' by shifting the byte 4 bits to the right and comparing with 0b1110: current_byte >> 4 == 0b1110.
Next, we check if we have enough bytes for a three-byte character by checking if the next two bytes (i+1, i+2) start with '10' as the first two bits, which is indicated by data[i+1] >> 6 == 0b10 and data[i+2] >> 6 == 0b10.
If all three conditions are true, then the current byte and the next two bytes together form a valid three-byte character, and we move on to the byte after the last next byte (i+3).
For four-byte characters:

UTF-8 four-byte characters start with '11110' as the first five bits. So, we check if the first five bits of the current byte are '11110' by shifting the byte 3 bits to the right and comparing with 0b11110: current_byte >> 3 == 0b11110.
Next, we check if we have enough bytes for a four-byte character by checking if the next three bytes (i+1, i+2, i+3) start with '10' as the first two bits, which is indicated by data[i+1] >> 6 == 0b10, data[i+2] >> 6 == 0b10, and data[i+3] >> 6 == 0b10.
If all four conditions are true, then the current byte and the next three bytes together form a valid four-byte character, and we move on to the byte after the last next byte (i+4).
If none of the above cases match, then the current byte and its subsequent bytes do not form a valid UTF-8 character sequence, and we return False immediately as it is not a valid UTF-8 encoding.

After checking each byte, if we have not encountered any invalid character sequences and have reached the end of the data without any issues, then we return True, indicating that the entire data set represents a valid UTF-8 encoding.
It's important to note that in this implementation, we only consider the 8 least significant bits of each integer in the input list, as mentioned in the problem statement. Also, the implementation assumes that the input data set is a list of integers, where each integer represents 1 byte of data. If the input data set is in a different format, appropriate conversions may need to be applied before using this implementation.
