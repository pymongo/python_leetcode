import unittest
from typing import List


# TODO 本题最快解法是「贪心+二分插入」的nlogn时间复杂度方法
# 接龙型动态规划经典题LIS，先找出接龙规则
# 动态规划不适合记录所有具体方案，但是可以持续更新一个最优方案(例如最长回文子串)
# TODO 如果本题要求返回具体的最优方案，则需要额外一个「前继节点」数组prev[j]去记录dp[i]的最优值是从哪一个dp[j]算过来的
# TODO ...而且不能用max，要用if找到最优方案更新时的i,j，去更新prev[j]
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([5, 4, 1, 2, 3], 3),
        ([4, 2, 4, 5, 3, 7], 4),
    ]

    def test_dp_solution(self):
        for nums, max_len in self.TEST_CASES:
            self.assertEqual(max_len, self.dp_solution(nums))

    @staticmethod
    def dp_solution(nums: List[int]) -> int:
        # 接龙型动态规划的状态表示
        # state: dp[i]表示以第i个数结尾的LIS是多长，所以这题不是前缀型(dp[i]表示前i的字符)
        # function: for j in range(0,i): if nums[j]<nums[i]: dp[i]=max(dp[i], dp[j]+1)
        # init: dp[0..n] = 1
        # answer: max(dp)
        size = len(nums)
        if size == 0:
            return 0
        dp = [1] * size
        max_len = 1

        for i in range(1, size):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])

        return max_len
