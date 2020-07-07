"""
https://leetcode.com/problems/merge-sorted-array/
"""

import unittest
from typing import List, Tuple


def merge_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    size1, size2 = len(nums1), len(nums2)
    result: List[int] = []
    ptr1, ptr2 = 0, 0

    # https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
    while ptr1 < size1 and ptr2 < size2:
        if nums1[ptr1] <= nums2[ptr2]:
            result.append(nums1[ptr1])
            ptr1 += 1
        else:
            result.append(nums2[ptr2])
            ptr2 += 1
    result = result + nums1[ptr1:] + nums2[ptr2:]
    return result


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[List[int], List[int], List[int]]] = [
        ([1, 2, 3], [2, 5, 6], [1, 2, 2, 3, 5, 6]),
        ([2], [1], [1, 2]),
        ([], [1], [1]),
    ]

    def test(self):
        for nums1, nums2, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, merge_two_sorted_arrays(nums1, nums2))
