import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        (["10", "0001", "111001", "1", "0"], 5, 3, 4),
    ]

    def test(self):
        for strs, m, n, expected in self.TEST_CASES:
            self.assertEqual(expected, self.f(strs, m, n))

    @staticmethod
    def f(strs: List[str], m: int, n: int) -> int:
        """
        由于物品字符串中只有0和1，而且只能选一次，所以变成二维背包容量的背包问题，例如选了字符串"01"后，0背包和1背包的容量都+1
        @param strs: 物品列表
        @param m: 0背包的容量
        @param n: 1背包的容量
        @return: 最多能放多少个不同的物品
        """
        if not strs:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            ones, zeros = 0, 0
            for char in s:
                if char == '1':
                    ones += 1
                else:
                    zeros += 1

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]
