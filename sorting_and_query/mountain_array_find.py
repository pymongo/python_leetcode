"""
早上11点
https://leetcode.com/problems/find-in-mountain-array/
实现针对山脉数组这种数据结构的find方法
我的思路与理解:
先找到山脉数组的peak_index
分别对nums[0:peak_index]和nums[peak_index+1:len-1].reverse()做一次二分搜索
"""

import unittest
from typing import List


# class MountainArray:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def get(self, index: int) -> int:
#         return self.nums[index]
#
#     def length(self) -> int:
#         return len(self.nums)


def get_peak_index(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        middle = start + (end - start) // 2
        if nums[middle] < nums[middle + 1]:
            start = middle + 1
        else:
            end = middle
    return start


def binary_search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] > target:
            end = middle - 1
        elif nums[middle] < target:
            start = middle + 1
        else:
            return middle
    return -1


def find_in_mountain_array(nums: List[int], target: int) -> int:
    length = len(nums)
    peak_index = get_peak_index(nums)
    bsearch_left = binary_search(nums[0:peak_index], target)
    if bsearch_left > -1:
        return bsearch_left
    bsearch_right = binary_search(nums[peak_index+1:length][::-1], target)
    if bsearch_right > -1:
        return bsearch_right
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3, 4, 5, 3, 1], 3, 2),
        ([0, 1, 2, 4, 2, 1], 3, -1),
    ]

    def test_find_in_mountain_array(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertEqual(expected, find_in_mountain_array(nums, target))
