from typing import List


# 给一个数组的各个数添上正负号，使得整体和等于trarget
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        令设为正号部分为P，设为负号部分为N
                          sum(P) - sum(N) = target
        sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                               2 * sum(P) = target + sum(nums)
        所以本题转为416. Partition Equal Subset Sum问题
        不过本题要求的是方案总数而不是可行性或最值
        0-1背包问题的大小为(target+sum(nums))//2
        """
        sum_nums = sum(nums)
        if sum_nums < target:
            return 0
        total = sum_nums + target
        if total % 2 == 1:
            return 0
        half = total // 2
        dp = [0] * (half + 1)
        dp[0] = 1
        for num in nums:
            for i in range(half, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[half]
