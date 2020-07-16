"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
https://www.lintcode.com/problem/first-position-of-target/description
"""

import unittest
from typing import List


# 主要有三种思路
# 1. 写两个函数，一个二分地找第一个，一个二分地找最后一个
# 2. 像我这样的笨方法，找到以后逐个「中心扩散」
# 3. 仿照步骤2，但是中心扩散时使用二分
def binary_search_first_and_last(nums: List[int], target: int) -> List[int]:
    size = len(nums) - 1
    start, end = 0, size

    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] > target:
            end = middle - 1
        elif nums[middle] < target:
            start = middle + 1
        else:
            start, end = middle, middle
            # FIXME 这里不是正统(orthodox)的二分法
            while start > 0 and nums[start - 1] == target:
                start -= 1
            while end < size and nums[end + 1] == target:
                end += 1
            return [start, end]
    return [-1, -1]


def binary_search_last(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    # 搜索first和last不会死循环的二分模板
    while start + 1 < end:
        middle = start + (end - start) // 2
        if nums[middle] > target:
            end = middle - 1
        elif nums[middle] < target:
            start = middle + 1
        else:
            # 如果是二分搜索相同值的第一个(first)，只需要两处改动
            # 1. start=middle => end=middle
            # 2. if nums[start] 放在 if nums[end]的上面
            start = middle
    if nums[end] == target:
        return end
    if nums[start] == target:
        return start
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([2, 2, 2], 2, [0, 2]),
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASES:
            print(nums, target)
            self.assertEqual(expected, binary_search_first_and_last(nums, target))
