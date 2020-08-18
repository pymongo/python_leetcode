import unittest


class Solution(unittest.TestCase):

    @staticmethod
    def coin_exchange_2_plans_count():
        pass

    def test_coin_exchange_feasibility(self):
        test_cases = [
            (10, True)
        ]
        for num, expected in test_cases:
            self.assertEqual(expected, self.coin_exchange_feasibility(num))

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

        for i in range(1, num + 1):
            for value in (3, 7):
                if i - value < 0:
                    # 例如不能兑换处2块
                    continue
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
