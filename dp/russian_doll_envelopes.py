import unittest
from typing import List
import bisect


class Solution(unittest.TestCase):
    TEST_CASES = [
        # ([2,3] => [5,4] => [6,7])
        ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    ]

    def test(self):
        for arr, longest in self.TEST_CASES:
            self.assertEqual(longest, self.f(arr))

    @staticmethod
    def f(arr: List[List[int]]) -> int:
        # 信封长度W正序，如果W相同，则按信封宽度H「逆序」
        # 为什么H要逆序呢？由于套娃要求长度和宽度更大，所以长度同为2的信封只能选一个
        # 贪心思想: 既然长度都为2的信封都为2，那我需要选宽度更大的信封才能装下前一个信封
        # 于是这题转为LIS问题
        arr.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums: List[int]) -> int:
            dp = []
            for num in nums:
                idx = bisect.bisect_left(dp, num)
                if idx == len(dp):
                    dp.append(num)
                else:
                    dp[idx] = num
            return len(dp)
        return lis([each[1] for each in arr])
