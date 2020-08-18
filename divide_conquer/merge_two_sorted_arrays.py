"""
https://leetcode.com/problems/merge-sorted-array/
"""

import unittest
from typing import List, Tuple


# https://www.lintcode.com/problem/merge-two-sorted-arrays/
# lintcode特有题，跟leetcode原版的区别是开辟一个新数组去返回
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
    while ptr1 < size1:
        result.append(nums1[ptr1])
        ptr1 += 1
    while ptr2 < size2:
        result.append(nums2[ptr2])
        ptr2 += 1
    return result

class Solution:
    @staticmethod
    def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        if n == 0:
            return []
        interval = 1
        while interval < n:
            for i in range(0, n-interval, interval*2):
                merge_two_sorted_arrays(arrays[i], arrays[i+interval])
            interval *= 2

        return arrays[0]


# https://www.lintcode.com/problem/merge-sorted-array/
# 与leetcode的merge-two-sorted-arrays一题基本一样，为了保证In-place还是要从后往前填值
# 参考内存从地址[0,2]复制到地址[1,3]也是从后往前复制避免正序复制时指针遍历[1,2]时刚写入的新数据会被覆盖掉
def merge_nums2_to_nums1(nums1: List[int], m: int, nums2: List[int], n):
    ptr1, ptr2 = m - 1, n - 1
    # 从后往前赋值
    idx = m + n - 1
    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] > nums2[ptr2]:
            nums1[idx] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[idx] = nums2[ptr2]
            ptr2 -= 1
        idx -= 1
    while ptr1 >= 0:
        nums1[idx] = nums1[ptr1]
        ptr1 -= 1
        idx -= 1
    while ptr2 >= 0:
        nums1[idx] = nums2[ptr2]
        ptr2 -= 1
        idx -= 1


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[List[int], List[int], List[int]]] = [
        ([], [1], [1]),
        ([2], [1], [1, 2]),
        ([1, 2, 3], [2, 5, 6], [1, 2, 2, 3, 5, 6]),
    ]

    TEST_CASES_2 = [
        ([2, 0], 1, [1], 1, [1, 2]),
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([0], 0, [1], 1, [1]),
    ]

    def test(self):
        for nums1, nums2, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, merge_two_sorted_arrays(nums1, nums2))

    def test_2(self):
        for nums1, m, nums2, n, expected in self.TEST_CASES_2:
            merge_nums2_to_nums1(nums1, m, nums2, n)
            self.assertEqual(expected, nums1)
