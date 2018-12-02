#!/usr/bin/env python3

from src.day2 import part2

import unittest


class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        input = [
            '5\t9\t2\t8\n',
            '9\t4\t7\t3\n',
            '3\t8\t6\t5\n'
        ]

        self.assertEqual(9, part2.checksum(input))
