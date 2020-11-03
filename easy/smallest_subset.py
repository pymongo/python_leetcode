import unittest
from typing import List


class Solution(unittest.TestCase):
    TESTCASES = [
        # 从数组中找一个长度最小的子集, 使得子集的和大于数组其余部分的和
        # 思路: 逆序排序数组，遍历直到已访问的数字和大于half_sum，返回已遍历的元素个数
        ([2, 1, 2], 2)
    ]

    def test(self):
        for nums, n in self.TESTCASES:
            self.assertEqual(n, self.f(nums))

    @staticmethod
    def f(nums: List[int]) -> int:
        nums.sort(reverse=True)
        size = len(nums)
        half_sum = sum(nums) // 2

        res = nums[0]
        res_size = 1
        for i in range(1, size):
            if res > half_sum:
                return res_size
            res += nums[i]
            res_size += 1
        raise Exception("Unreachable")
