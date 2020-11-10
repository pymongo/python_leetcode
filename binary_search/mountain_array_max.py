"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
https://lintcode.com/problem/maximum-number-in-mountain-sequence/description?_from=ladder&&fromId=161
给n个整数的山脉数组，即先增后减的序列，找到山顶(最大值)
具有「单调性」特征的数据结构可以考虑使用二分法
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


# 二分目标: find_last递增，退出时start就是最后一个递增
def peak_index(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        middle = start + (end - start) // 2
        if nums[middle] < nums[middle + 1]:
            # middle满足递增(上山坡)条件，所以山顶会在[middle+1,end]之间(右半区间一定有解)
            start = middle + 1
        else:
            # middle不满足递增条件，所以山顶会在[start,middle]之间
            end = middle
    return start


# 另一种思路，找到第一个开始递减的元素，也就是山峰
# 为什么没有三分、四分法？判断答案落入哪一个区间耗费更多时间
def find_first_desc(nums: List[int]) -> int:
    """
    Round 1:
    1 2 4 8 6 3
    ^         ^
    mid=nums[(0+5)//2]=4
    4 > 8 False => start=mid+1

    Round 2:
    1 2 4 8 6 3
          ^   ^
    6 > 3 True => end=mid

    Round 3:
    1 2 4 8 6 3
          ^ ^
    6 > 3 True => end=mid

    Round 4:
    1 2 4 8 6 3
          ^
    8 > 6 True => end=mid => start==end => break
    """
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] > nums[mid + 1]:
            # mid已经递减了，往左边区间继续搜索
            end = mid
        else:
            start = mid + 1
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
