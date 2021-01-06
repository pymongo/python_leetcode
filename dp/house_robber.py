import unittest
from binary_tree.binary_tree import TreeNode
from typing import List, Tuple


class Solution(unittest):
    # https://www.lintcode.com/problem/work-plan/
    def workPlan(self, low, high):
        n = len(low)
        dp = [0] * (n)
        dp[0] = low[0]
        dp[1] = max(low[0]+low[1], high[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+high[i], dp[i-1]+low[i])
        return dp[n-1]

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
        return pre1

    @staticmethod
    def rob(nums: List[int], first: int, last: int) -> int:
        pre1, pre2 = 0, 0
        for i in range(first, last + 1):
            curr = max(pre1, pre2 + nums[i])
            pre1, pre2 = curr, pre1
        return pre1

    @staticmethod
    def house_rob_2(nums: List[int]) -> int:
        # 和打家劫舍1的区别在于第一家和最后一家相连(环形)
        # TODO 另一种解决环形数组的方法是: 单调栈(Monotonic Stack)，但是似乎这题用不了
        # 新加约束规则就是第一家和最后一家不能同时抢，最后答案就是要么抢第一家和要么不抢两种情况的最大值
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(Solution.rob(nums, 0, n - 2), Solution.rob(nums, 1, n - 1))

    @staticmethod
    def rob_or_not(node: TreeNode) -> Tuple[int, int]:
        # 返回值的[0]表示不抢的收益(正好二进制0也表示不做的意思)，[1]表示抢的收益
        if node is None:
            return 0, 0
        left = Solution.rob_or_not(node.left)
        right = Solution.rob_or_not(node.right)
        # 抢，下家就不能抢了
        rob = node.val + left[0] + right[0]
        # 不抢，下家可抢可不抢，取决于收益大小
        no_rob = max(left[0], left[1]) + max(right[0], right[1])
        return no_rob, rob

    @staticmethod
    def house_rob_3(root: TreeNode):
        return max(Solution.rob_or_not(root))
