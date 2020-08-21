from typing import List


# 寻找数组中的连续子数组里等差数列的个数
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        count = 0
        for i in range(2, n):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                count += dp[i]
        return count
