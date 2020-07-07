"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
https://www.lintcode.com/problem/first-position-of-target/description
"""

import unittest
from typing import List


def bsearch(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    start, end = 0, length - 1

    while start <= end:
        middle = start + (end - start) // 2
        print(start, middle, end)
        if nums[middle] > target:
            end = middle - 1
        elif nums[middle] < target:
            start = middle + 1
        else:
            start, end = middle, middle
            while end < length-1 and nums[end+1] == nums[start]:
                end += 1
            return [start, end]
    return [-1, -1]


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertEqual(expected, bsearch(nums, target))
