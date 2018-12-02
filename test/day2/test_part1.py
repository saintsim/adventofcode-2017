#!/usr/bin/env python3

from src.day2 import part1

import unittest


class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        input = [
            '5\t1\t9\t5\n',
            '7\t5\t3\n',
            '2\t4\t6\t8\n'
        ]

        self.assertEqual(18, part1.checksum(input))
