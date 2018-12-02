#!/usr/bin/env python3


def captcha_solution():
    total = 0
    with open('input', 'r') as file:
        sequence = file.read()
        sequence_length = len(sequence)
        next_item_index = int(int(sequence_length)/2)
        for index, item in enumerate(sequence):
            if item == sequence[(index+next_item_index) % sequence_length]:
                total += int(item)
    return total


print('Result: ' + str(captcha_solution()))
