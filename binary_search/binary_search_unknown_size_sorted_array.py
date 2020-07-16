"""
https://www.lintcode.com/problem/search-in-a-big-sorted-array/description?_from=ladder&&fromId=161
"""

import unittest
from typing import List
import random


class ArrayReader:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def get(self, index: int):
        if index >= len(self.nums):
            return 2147483647
        return self.nums[index]


def search_in_unknown_size(nums: ArrayReader, target: int) -> int:
    end, last_end = 1, 0
    # 用倍增法找到右边界
    while nums.get(end) < target:
        last_end = end
        end *= 2
    start = last_end
    while start <= end:
        mid = start + (end - start) // 2
        mid_val = nums.get(mid)
        if mid_val > target:
            end = mid - 1
        elif mid_val < target:
            start = mid + 1
        else:
            return mid
    return -1

I32_MAX = 2 ** 31 - 1


class Testing(unittest.TestCase):
    TEST_CASE = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASE:
            nums += [I32_MAX] * random.randint(10, 100)
            array_reader = ArrayReader(nums)
            self.assertEqual(expected, search_in_unknown_size(array_reader, target))
