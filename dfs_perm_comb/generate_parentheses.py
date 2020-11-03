import unittest
from typing import List


class Solution(unittest.TestCase):
    TESTCASES = [
        (3, [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]),
    ]

    def test(self):
        for n, expected in self.TESTCASES:
            self.assertEqual(expected, self.generate_parenthesis(n))

    @staticmethod
    def generate_parenthesis(n: int) -> List[str]:
        res = []

        def dfs(s: List[str], left_remain: int, right_remain: int):
            if left_remain == 0 and right_remain == 0:
                res.append(''.join(s))
                return
            if left_remain > 0:
                s.append('(')
                dfs(s, left_remain - 1, right_remain)
                s.pop()
            if right_remain > left_remain:
                s.append(')')
                dfs(s, left_remain, right_remain - 1)
                s.pop()

        dfs([], n, n)
        return res
