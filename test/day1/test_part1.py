#!/usr/bin/env python3

from src.day1 import part1

import unittest


class TestCaptchaSolution(unittest.TestCase):
    def test_captcha_solution(self):
        cases = [
            (['1', '1', '2', '2'], 3),
            (['1', '1', '1', '1'], 4),
            (['1', '2', '3', '4'], 0),
            (['9', '1', '2', '1', '2', '1', '2', '9'], 9)
        ]

        for case in cases:
            self.assertEqual(case[1], part1.captcha_solution(case[0]))
