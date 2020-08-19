import unittest
from typing import List


class Solution(unittest):
    # 如果当前这家被打劫，临近的两家都会收到报警信号锁上大门，所以相当于需要在i+1家休息再去打劫i+2
    # 搜素树的决策: 是否当前这家
    @staticmethod
    def house_rob_1(nums: List[int]) -> int:
        pre1, pre2 = 0, 0
        # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        for num in nums:
            # 当前的最大收益=max(选择打劫上一家所以本轮休息，上一家休息这家打劫)
            curr = max(pre1, pre2 + num)
            # pre1, pre2类似斐波那契数列那样前移，此时pre1=curr表示第i家已被打劫
            pre1, pre2 = curr, pre1
        return max(pre1, pre2)
