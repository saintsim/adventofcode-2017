#!/usr/bin/env python3


def checksum(spreadsheet):
    checksum = 0
    for row in spreadsheet:
        cells = list(map(int, row.split()))
        checksum += max(cells)-min(cells)
    return checksum


if __name__ == '__main__':
    with open('input', 'r') as file:
        spreadsheet = file.readlines()
        print('Result: ' + str(checksum(spreadsheet)))
