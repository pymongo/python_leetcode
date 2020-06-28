"""
https://leetcode.com/problems/maximum-subarray/
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
import unittest
from typing import List, Tuple
from mydbg import dbg

MIN_INT = -(2 ** 8)


class Solution:
    @staticmethod
    def brute_force(nums: List[int]) -> int:
        size: int = len(nums)
        max_sum: int = nums[0]
        for i in range(size):
            temp_sum = nums[i]
            for j in range(i + 1, size):
                temp_sum += nums[j]
                if max(temp_sum, nums[j]) > max_sum:
                    max_sum = max(temp_sum, nums[j])
        return max_sum

    @staticmethod
    def merge_sort(nums: List[int]) -> int:
        dbg(nums)
        size = len(nums)
        if size == 1:
            return nums[0]
        # 这里left和right指的是数组的左右指针
        left, right = 0, len(nums)
        # 递归退出条件: 数组长度为1
        mid = (left+right) // 2
        dbg((left, mid, right))
        left_sum = Solution.merge_sort(nums[left:mid])
        right_sum = Solution.merge_sort(nums[mid:right])
        return max(left_sum, right_sum, left_sum+right_sum)


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[List[int], int]] = [
        ([-1, 0, -2], 0),
        ([-2, 1], 1),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
    ]

    def test_brute_force(self):
        for input_array, expected in self.TEST_CASES[:]:
            print(input_array, expected)
            self.assertEqual(expected, Solution.brute_force(input_array))

    def test_merge_sort(self):
        for input_array, expected in self.TEST_CASES[:]:
            print(input_array, expected)
            self.assertEqual(expected, Solution.merge_sort(input_array))
