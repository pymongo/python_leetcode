import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([2, 3, 6, 7], 7, [[7], [2, 2, 3]]),
        ([1], 3, [[1, 1, 1]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ]

    def test_dfs(self):
        for nums, target, combination in self.TEST_CASES:
            self.assertCountEqual(combination, self.f(nums, target))

    @staticmethod
    def f(nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        cur, res = [], []

        def dfs(start: int, _target: int):
            if _target == 0:
                res.append(cur.copy())
                return
            for i in range(start, n):
                if nums[i] > _target:
                    return
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(i, _target - nums[i])
                # 如果是combination_sum_2这题，元素不能重复使用，就把start=i改成i+1就行了
                # dfs(i, _target - nums[i])
                cur.pop()

        dfs(0, target)
        return res
