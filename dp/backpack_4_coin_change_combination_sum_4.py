import unittest
import sys
from typing import List


class Solution(unittest.TestCase):
    def test_coin_change_feasibility(self):
        TEST_CASES = [
            (10, True)
        ]
        for num, feasibility in TEST_CASES:
            self.assertEqual(feasibility, self.coin_change_feasibility(num))

    # 求完全背包的可行性问题的，类似的题还有word_break
    @staticmethod
    def can_divide_by_3_and_7(num: int) -> str:
        """
        验证是否存在一对整数a和b，使得3a+7b=x
        ```
        dp = [False] * (num + 1)
        dp[0] = True
        for value in (3, 7):
            for i in range(value, num + 1):
                dp[i] = dp[i] or dp[i - value]
        return dp[num]
        ```
        """
        # for i in range(x // 7, -1, -1):
        #     if (x-7*i) % 3 == 0:
        #         return "YES"
        # return "NO"
        max_7 = num // 7
        # 由3组成的部分
        part_3 = num - 7 * max_7
        while part_3 <= num:
            if part_3 % 3 == 0:
                return "YES"
            part_3 += 7
        return "NO"
