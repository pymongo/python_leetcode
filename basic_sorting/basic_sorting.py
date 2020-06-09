"""
Relative Problems
- https://lintcode.com/problem/sort-integers
- https://lintcode.com/problem/sort-integers-ii
- https://leetcode.com/problems/sort-an-array/
"""
import unittest
from typing import List


def bubble_sort(nums: List[int]):
    length: int = len(nums)
    for i in range(length-1):
        for j in range(i, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5])
    ]

    def test_bubble_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(bubble_sort(case[0]), case[1])




