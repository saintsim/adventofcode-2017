#!/usr/bin/env python3


def captcha_solution():
    total = 0
    with open('input', 'r') as file:
        sequence = file.read()
        sequence_length = len(sequence)
        for index, item in enumerate(sequence):
            if item == sequence[(index+1) % sequence_length]:
                total += int(item)
    return total


print('Result: ' + str(captcha_solution()))
