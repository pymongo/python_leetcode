"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
给n个整数的山脉数组，即先增后减的序列，找到山顶(最大值)
TODO 二分法解决的几类问题
- [x] 有序数组的二分搜索: 34(二分搜索第一个和最后一个), 704(经典二分搜索)
- [x] 山脉数组(mountain array)类问题: 852、(941)、1095
- [ ] 旋转排序数组: 33, 81, 153, 154
- [ ] 分割数组的最大值: 410
- [ ] 转变数组后最接近目标值的数组和: 1300
- [ ] 平方根: 69(牛顿连续均值求平方根?)
- [ ] 寻找重复数: 287
- [ ] 爱吃香蕉的珂珂: 875
"""

import unittest
from typing import List


def peak_index_brute_force(nums: List[int]) -> int:
    i = 0
    while nums[i] < nums[i + 1]:
        i += 1
    return i


def peak_index(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        middle = start + (end - start) // 2
        if nums[middle] < nums[middle + 1]:
            # middle满足递增(上山坡)条件，所以山顶会在[middle+1,end]之间
            start = middle + 1
        else:
            # middle不满足递增条件，所以山顶会在[start,middle]之间
            end = middle
    return start


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2),
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
    ]

    def test_peak_index_brute(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, peak_index_brute_force(nums))

    def test_peak_index(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, peak_index(nums))
