"""
https://www.lintcode.com/problem/triangle-count/description?_from=ladder&&fromId=161
输入一个排序数组，请问从数组中取3个值能组成多少个不同的三角形
由于数组是有序的，满足nums[a] + nums[b] > nums[c]即可，转换成两数之和大于类型问题
这题有点像three sum，和三数之和类似，遍历时可变的双指针要在等式的左边，而固定不变的target放等式右边
"""

import unittest
from typing import List


def triangle_count(nums: List[int]) -> int:
    size = len(nums)
    last = size - 1
    if size < 3:
        return -1
    count = 0
    for a in range(size - 2):
        c = last
        for b in range(a+1, size-1):
            if nums[a] + nums[b] > nums[c]:
                print(a,b,c)
                count += 1
            while nums[a] + nums[b] > nums[c-1]:
                c -= 1
                count += 1
    return count


class Testing(unittest.TestCase):
    TEST_CASES = [
        # (3,4,6), (3,6,7), (4,6,7)
        ([3, 4, 6, 7], 3),
        ([4, 4, 4, 4], 4),
    ]

    def test_triangle_count(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, triangle_count(nums))
