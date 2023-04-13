#!/usr/bin/python3
""" 
This script that reads stdin line by line and computes metrics
steps:
1) read from the stdin for line in stdin, 
2) check if format is , else skip
3) Declare a counter variable that increments, 
4) check if the counter is 10,
calculate
5) Declare a dictionary for storing the status codes
6) Declare a variable to store the file size
7) Every time a line is read, check if key is availale in dict
8) update file size
9) print file size
10)if !key || !value, continue else print status code
"""

import re
import sys


sts_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 405: 0, 500: 0}
stdin = sys.stdin
counter = 0
total_file_size = 0

try:
    for line in stdin:
        output = line.split()
        if int(output[-2]) in sts_dict.keys() and len(output) == 9:
            counter += 1
            sts_dict[int(output[-2])] += 1
            total_file_size += int(output[-1])
        if counter % 10 == 0:
            print('File size: {}'.format(total_file_size))
            for key, value in sts_dict.items():
                if value:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt as error:
    print('File size: {}'.format(total_file_size))
    for key, value in sts_dict.items():
        print("{}: {}".format(key, value))
