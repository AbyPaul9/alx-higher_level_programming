#!/usr/bin/python3
""" script that count request by web request status """


import sys
import re


file_size = 0
status_count = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}


def incrementErrorStatusCount(prmString):
    """ increment request number """
    global file_size, status_count
    try:
        data = re.split("(.*) (.*) ([0-9]*)$", prmString)
        if len(data) == 5:
            if data[-3].isnumeric():
                errorCode = int(data[-3])
            file_size += (int(data[-2]))
        if len(data) == 5 and checkValidity(errorCode) is True:
            status_count[errorCode] += 1

    except:
        pass


def checkValidity(prmErrorCode):
    """ check error code validity """
    global status_count
    if prmErrorCode in status_count:
        return True
    return False


def printStatistics():
    """ print statistics """
    global file_size, status_count
    print("File size: {:d}".format(file_size))
    for errorCode, count in sorted(status_count.items()):
        if status_count[errorCode]:
            print("{:d}: {:d}".format(errorCode, count))


try:
    for index, line in enumerate(sys.stdin):
        incrementErrorStatusCount(line)
        if (index + 1) % 10 == 0:
            printStatistics()
except KeyboardInterrupt:
    pass
finally:
    printStatistics()
