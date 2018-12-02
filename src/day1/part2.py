#!/usr/bin/env python3


def captcha_solution(sequence):
    total = 0
    sequence_length = len(sequence)
    next_item_index = int(int(sequence_length)/2)
    for index, item in enumerate(sequence):
        if item == sequence[(index+next_item_index) % sequence_length]:
            total += int(item)
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        sequence = file.read()
        print('Result: ' + str(captcha_solution(sequence)))