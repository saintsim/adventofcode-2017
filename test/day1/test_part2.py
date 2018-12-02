#!/usr/bin/env python3

from src.day1 import part2

import unittest


class TestCaptchaSolution(unittest.TestCase):
    def test_captcha_solution(self):
        cases = [
            (['1', '2', '1', '2'], 6),
            (['1', '2', '2', '1'], 0),
            (['1', '2', '3', '4', '2', '5'], 4),
            (['1', '2', '3', '1', '2', '3'], 12),
            (['1', '2', '1', '3', '1', '4', '1', '5'], 4)
        ]

        for case in cases:
            self.assertEqual(case[1], part2.captcha_solution(case[0]))
