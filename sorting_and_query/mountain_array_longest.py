"""
https://leetcode.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode/
"""
import unittest
from typing import List

# 先从左到右找到第一个山脉数组的上山点，然后再往后搜索
def longest_mountain_in_array(nums: List[int]) -> int:
    length = len(nums)
    max_len = 0
    i = 1
    while i < length:
        if nums[i] <= nums[i-1]:
            i += 1
            continue
        # 下面这种写法也行，不过效率不如continue
        # while i < length and nums[i] <= nums[i - 1]:
        #     i += 1

        start = i - 1
        while i < length and nums[i] > nums[i-1]:
            i += 1
        while i < length and nums[i] < nums[i-1]:
            i += 1
            # 由于不知道何时到达边界，所以下坡时每遍历一次就计算一下最大值
            max_len = max(max_len, i - start)
    return max_len


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([7, 4, 8], 0),
        ([5, 4, 3, 2, 1], 0),
        ([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0], 11),
        ([2, 2, 2], 0),
        ([2, 1, 4, 7, 3, 2, 5], 5),
    ]

    def testing(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, longest_mountain_in_array(nums))
