#!/usr/bin/env python3


def checksum_for_row(cells):
    for idx, val in enumerate(cells):
        for other_idx, other_val in enumerate(cells):
            if idx == other_idx:
                continue
            if val % other_val == 0:
                return int(val / other_val)


def checksum(spreadsheet):
    checksum = 0
    for row in spreadsheet:
        cells = list(map(int, row.split()))
        checksum += checksum_for_row(cells)

    return checksum


if __name__ == '__main__':
    with open('input', 'r') as file:
        spreadsheet = file.readlines()
        print('Result: ' + str(checksum(spreadsheet)))
