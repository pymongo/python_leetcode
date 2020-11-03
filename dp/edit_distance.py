import unittest
from functools import lru_cache


# 编辑距离算法被数据科学家广泛应用，是用作机器翻译和语音识别评价标准的基本算法
class Solution(unittest.TestCase):
    TESTCASES = [
        ("horse", "ros", 3),
        ("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically", 27),
    ]

    def test(self):
        for word1, word2, expected in self.TESTCASES:
            # self.assertEqual(expected, self.f(word1, word2))
            self.assertEqual(expected, self.best_solution_tail_recursive(word1, word2))

    @staticmethod
    def f(A: str, B: str) -> int:
        m, n = len(A), len(B)
        # 其中一个为空
        if m * n == 0:
            return m + n
        # dp[i][j]表示A[:i]至少需要几次操作替换成B[:j]
        # 很容易想到一种情况的状态转移: A[i-1]==B[j-1]时, dp[i][j]==dp[i-1][j-1]，既然各新增的两个字符相等，所以不需要额外的一次操作
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 由于填表时依赖左、下、左下的值，初始化边界情况
        for i in range(m + 1):
            # 需要i次操作才能让A[:i]修改为空串B
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        # 类似Unique Path的初始化和填表方向
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                edit = dp[i - 1][j - 1]
                if A[i - 1] != B[j - 1]:
                    # 如果新比较的两个字符不相同，就需要额外一次将A[i-1]改成B[j-1]的操作
                    edit += 1
                # 需要往A插入选中的B[j-1]
                insert = dp[i - 1][j] + 1
                # 需要从A删掉选中的A[i-1]
                delete = dp[i][j - 1] + 1
                # 改/删/增 三种操作的最小操作数
                dp[i][j] = min(edit, insert, delete)
        return dp[m][n]

    @staticmethod
    def best_solution_tail_recursive(word1: str, word2: str) -> int:
        # 禁用LRU cache删掉递归的变量，牺牲空间提升速度
        @lru_cache(None)
        def dp(n, m):
            if n == 0:
                return m
            if m == 0:
                return n
            if word1[n - 1] == word2[m - 1]:
                return dp(n - 1, m - 1)
            # TODO 尾递归，为何看上去没有memo也能这么快？同理用栈模拟尾递归也是最快的解法
            return min(
                dp(n, m - 1),  # insert
                dp(n - 1, m),  # remove
                dp(n - 1, m - 1)  # replace
            ) + 1

        return dp(len(word1), len(word2))
