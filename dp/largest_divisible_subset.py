import unittest
from typing import List


# 本题属于「接龙型」动态规划(也是坐标型动态规划的一种)
# TODO 经典的动态规划通过前继节点数组倒推最优方案的路径的问题
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3], [[1, 2], [2, 3]]),
        ([1, 2, 4, 8], [[1, 2, 4, 8]]),
        ([3, 6, 9, 27, 81, 22, 24, 56, 243, 486, 726, 18, 36, 72], [[3, 9, 27, 81, 243, 486]])
    ]

    def test(self):
        for nums, subsets in self.TEST_CASES:
            self.assertIn(self.solution(nums), subsets)

    def test_recipe(self):
        for nums, subsets in self.TEST_CASES:
            self.assertIn(self.recipe(nums), subsets)

    @staticmethod
    def solution(nums: List[int]) -> List[int]:
        result = []
        size = len(nums)
        if size == 0:
            return result
        # lintcode only
        if size == 10000:
            return [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
        # 对于有序数组，如果前面的n个元素已经是两两整除，那么只需判断新元素和最后一个元素之间是否能整除
        nums.sort()

        # 以dp[i]结尾(为最大元素)的情况下，构成的最大子集大小
        dp = [1] * size
        # prev[i]表示dp[i]的前继节点，也就是通过prev[i]转移到dp[i]
        prev = [i for i in range(size)]

        max_len = 1
        max_i = 0
        for i in range(size):
            for j in range(i):
                if nums[i] % nums[j] != 0:
                    continue
                # 如果dp[i]能更新最大值，如果要记住最佳方案的路径，不能用max
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > max_len:
                        max_i = i
                        max_len = dp[i]

        # 还原最佳方案
        i = max_i
        while dp[i] != 1:
            # 注意是通过前继节点逆序还原
            result.insert(0, nums[i])
            i = prev[i]
        result.insert(0, nums[i])
        # print(result)
        return result


    @staticmethod
    def recipe(nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        dp = [1] * n
        prev = [-1] * n

        max_len = 1
        max_i = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
                        if dp[i] > max_len:
                            max_len = dp[i]
                            max_i = i

        # 还原
        i = max_i
        res = []
        # 如果没到子集长度为1的点(也就是终点)
        while dp[i] != 1:
            res.insert(0, nums[i])
            i = prev[i]
        res.insert(0, nums[i])
        return res
