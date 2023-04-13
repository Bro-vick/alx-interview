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

def parseLogs():


    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines 
        & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                fileSize += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        report(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        report(fileSize, statusCodes)
        raise


def report(fileSize, statusCodes):
    """
    This function Prints generated report to standard output
    Args:
        fileSize (int): This is the total log size after
        every 10 successfully read line
        statusCodes (dict): The dictionary of status codes and counts
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseLogs()
