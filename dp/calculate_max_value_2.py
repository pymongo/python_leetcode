import unittest


class Solution(unittest.TestCase):
    @staticmethod
    def calc_max_value_1(s: str) -> int:
        """
        只能从左到右两两地加括号
        输入: s = "01231"
        解释:
         ((((0 + 1) + 2) * 3) + 1) = 10我们得到了最大值 10
        """
        n = len(s)
        if n == 0:
            return 0
        # 运算符靠左的数会一直被更新, lhs/rhs命名风格参考Rust的重载运算符
        lhs = int(s[0])
        for i in range(1, n):
            rhs = int(s[0])
            # 如果左右两边是1，必用加法，其余情况用乘法
            if lhs <= 1 or rhs <= 1:
                lhs = lhs + rhs
            else:
                lhs = lhs * rhs
        return lhs

    @staticmethod
    def calc_max_value_2(s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = int(s[i])
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for mid in range(i, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][mid] + dp[mid + 1][j],
                        dp[i][mid] * dp[mid + 1][j]
                    )
        return dp[0][n - 1]
