"""
https://leetcode.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode/
"""
import unittest
from typing import List
import enum


# 单调性
class Monotonic(enum.Enum):
    DECREASING = 0
    INCREASING = 1
    NONE = 2


# 先从左到右找到第一个山脉数组的上山点，然后再往后搜索
def longest_mountain_in_array(nums: List[int]) -> int:
    length = len(nums)
    monotonic: 'Monotonic' = Monotonic.NONE
    max_len = 0
    # 初始状态
    start = -1  # 左边的山脚(上山点)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            if monotonic == Monotonic.DECREASING:
                # 如果是从单调递减变为单调递增
                max_len = max(max_len, i - start + 1)
                if length - i < max_len:
                    break
            start = i - 1
            monotonic = Monotonic.INCREASING
        elif nums[i] < nums[i - 1]:
            monotonic = Monotonic.DECREASING
        else:
            # 遇到前后两个值相等的情况，需要重新搜索上山点
            start = -1
            monotonic = Monotonic.NONE
    return max_len


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0], 11),
        ([2, 2, 2], 0),
        ([2, 1, 4, 7, 3, 2, 5], 5),
    ]

    def testing(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, longest_mountain_in_array(nums))
