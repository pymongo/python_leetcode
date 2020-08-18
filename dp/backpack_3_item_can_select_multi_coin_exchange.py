import unittest
from typing import List


# 完全背包问题: 一个物品可以选一次或多次
class Solution(unittest.TestCase):
    def test_coin_exchange_min_items(self):
        test_cases = [
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
        ]

    def test_coin_exchange_2_plans_count(self):
        test_cases = [
            (5, [1, 2, 5], 4),
            (3, [2], 0),
            (10, [10], 1),
        ]
        for amount, coins, plans_count in test_cases:
            self.assertEqual(plans_count, self.coin_exchange_2_plans_count(amount, coins))

    @staticmethod
    def coin_exchange_2_plans_count(amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

    def test_coin_exchange_feasibility(self):
        test_cases = [
            (10, True)
        ]
        for num, feasibility in test_cases:
            self.assertEqual(feasibility, self.coin_exchange_feasibility(num))

    @staticmethod
    def coin_exchange_feasibility(num: int) -> bool:
        """
        lintcode_749
        可以将本题理解成`零钱兑换-求可行性`问题, 可行性(feasibility)
        纸币只有面值3和7两种，问你能不能找零num元
        但是这题最佳做法不是DP，而是用朴素的数学数论规律，参考can_divide_by_3_and_7
        """
        dp = [False] * (num + 1)
        dp[0] = True

        for value in (3, 7):
            for i in range(value, num + 1):
                dp[i] = dp[i] or dp[i - value]
        return dp[num]

    @staticmethod
    def can_divide_by_3_and_7(num: int) -> str:
        """
        验证是否存在一对整数a和b，使得3a+7b=x
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
