"""
https://leetcode.com/problems/reverse-string/
"""
import unittest
from typing import List


def reverse_string(s: List[str]):
    # size = len(s)
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


class Testing(unittest.TestCase):
    TESTCASES = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"])
    ]

    def test(self):
        for string, expected in self.TESTCASES:
            reverse_string(string)
            self.assertEqual(expected, string)
