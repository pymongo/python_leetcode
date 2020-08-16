import unittest


class Solution(unittest.TestCase):
    TEST_CASES = [
        ("ABCE", "CBCE", 2),
    ]

    def test(self):
        for A, B, max_len in self.TEST_CASES:
            self.assertEqual(max_len, self.f(A, B))

    @staticmethod
    def f(A: str, B: str) -> int:
        # 最长公共子串严格来说不算DP，DP的必要特征是大问题可以变成稍小一点的问题，而且可以用递归实现
        # 滚动数组就足以让额外空间优化到O(n)，不要研究一维DP数组，倒着遍历那种，容易写错
        m, n = len(A), len(B)
        if m == 0 or n == 0:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    temp_len = dp[i - 1][j - 1] + 1
                    dp[i][j] = temp_len
                    if temp_len > max_len:
                        max_len = temp_len
                else:
                    # 只要当前两个字母不相等，就不可能在这取到最大值
                    # 置0的好处让后面通过dp[i-1][j-1]找到这里时，直接知道这里字母不相等，要从下一个字母去累加长度
                    dp[i][j] = 0
        return max_len
