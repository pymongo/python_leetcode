# https://leetcode.com/problems/string-to-integer-atoi/
import unittest
import re


class Solution(unittest.TestCase):
    TEST_CASES = [
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("3.1415926", 3),
    ]

    def test_re(self):
        for s, integer in self.TEST_CASES:
            print(s)
            self.assertEqual(integer, self.regular_expression_solution(s))

    @staticmethod
    def regular_expression_solution(s: str) -> int:
        i32_max = 2147483647
        i32_min = -2147483648
        s = s.lstrip()
        # ^[+\-]?表示只能以 0个或1个 +或-符号开头，过滤掉"words and 987"的"words and "
        pattern = re.compile(r'^[+\-]?\d+')
        match_res = pattern.search(s)
        if match_res is None:
            return 0
        num = int(match_res.group())
        return max(min(num, i32_max), i32_min)
