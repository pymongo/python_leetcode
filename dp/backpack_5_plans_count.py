import unittest
from typing import List


class Solution:
    @staticmethod
    def dp_solution(nums: List[int], target: int) -> int:
        # dp[j]的状态表示组成容量为j一共有几种方案
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num - 1, -1):
                # 0-1背包问题基本都可以用这套模板，核心是状态的表示和状态转移的递推关系
                dp[j] += dp[j - num]
        return dp[target]

    @staticmethod
    def dfs_solution(nums: List[int], target: int) -> int:
        # 如果是求具体方案的话，才适合用DFS
        # FIXME 时间紧迫，暂时放弃DFS
        size = len(nums)
        nums = sorted(nums)
        plans_count = 0
        #
        # def dfs(start: int, target_num: int):
        #     if target_num == target:
        #         plans_count[0] += 1
        #         return
        #     for i in range(start, size):
        #         next_target = target_num + nums[i]
        #         if next_target > target:
        #             return
        #         dfs(i, next_target)

        for i in range(size):
            curr = nums[i]
            for j in range(i + 1, size):
                # 还是得DFS，因为下一个数可以 选 或 不选
                next_curr = curr + nums[j]
                if next_curr > target:
                    break
                elif next_curr == target:
                    plans_count += 1
                    break
                else:
                    curr = next_curr
        return plans_count


class Testing(unittest.TestCase):
    TESTCASES = [
        ([1, 2, 3, 3, 7], 7, 2)
    ]

    def test_dp_solution(self):
        for nums, target, plans_count in self.TESTCASES:
            self.assertEqual(plans_count, Solution.dp_solution(nums, target))

    def test_dfs_solution(self):
        for nums, target, plans_count in self.TESTCASES:
            self.assertEqual(plans_count, Solution.dfs_solution(nums, target))
