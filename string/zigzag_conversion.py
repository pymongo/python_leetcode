"""
https://leetcode.com/problems/zigzag-conversion/
"""
from typing import List, Tuple
from mydbg import dbg
import unittest


def solution(s: str, rows: int) -> str:

    return ""


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[str, int, str]] = [
        ("LEETCODEISHIRING", 3, "LCIRETOESIIGEDHN")
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[2], solution(case[0], case[1]))
