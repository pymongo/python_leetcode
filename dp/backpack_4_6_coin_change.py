import unittest
import sys
from typing import List


# 完全背包问题: 一个物品可以选一次或多次
class Solution(unittest.TestCase):
    def test_coin_change_min_items(self):
        test_cases = [
            # 11=5+5+1, 用尽可能少的硬币凑出11
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
        ]
        for coins, amount, expected in test_cases:
            self.assertEqual(expected, self.coin_change_min_items(coins, amount))

    @staticmethod
    def coin_change_min_items(coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1

    def test_coin_change_2_plans_count(self):
        test_cases = [
            (5, [1, 2, 5], 4),
            (3, [2], 0),
            (10, [10], 1),
        ]
        for amount, coins, plans_count in test_cases:
            self.assertEqual(plans_count, self.coin_change_2_plans_count(amount, coins))

    @staticmethod
    def coin_change_2_plans_count(amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

    @staticmethod
    def combination_sum_4(amount: int, coins: List[int]) -> int:
        """
        注意面试官可能会问这个算法能不能解决nums中有负数的情况，答案是不能
        和coin_change_2区别在于外层for循环是遍历dp数组的下标
        TODO 可以先背结论: dp数组下标->coins的遍历顺序能得到更多的方案数，会把[1,2]和[2,1]当作组合数的两种方案
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] += dp[i - coin]
        return dp[amount]

    def test_coin_change_feasibility(self):
        test_cases = [
            (10, True)
        ]
        for num, feasibility in test_cases:
            self.assertEqual(feasibility, self.coin_change_feasibility(num))

    @staticmethod
    def coin_change_feasibility(num: int) -> bool:
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
