"""
https://lintcode.com/problem/search-in-a-big-sorted-array/description?_from=ladder&&fromId=161
https://jiuzhang.com/solution/search-in-a-big-sorted-array/
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
    first = nums.get(0)
    if first == target:
        return 0
    if first > target:
        return -1
    end = 1
    # 还能用到倍增法的情况: Exponential Backoff网络请求失败, x秒后重连(第一次重连在2秒，第二次4秒...)
    # 用倍增法找到右边界，这里其实隐含地用到了get(end)越界时，会返回2147483647的特性
    while nums.get(end) < target:
        end *= 2
    start = end // 2
    while start <= end:
        mid = start + (end - start) // 2
        mid_val = nums.get(mid)
        if mid_val > target:
            end = mid - 1
        elif mid_val < target:
            # 隐含地用到了get(end)越界时，会返回2147483647的特性
            start = mid + 1
        else:
            # FIXME 这里不是正统(orthodox)的二分法
            while nums.get(mid - 1) == target:
                mid -= 1
            return mid
    return -1

# 一定要搞清楚题目要求的是二分法找出第一个位置、最后位置、还是任意位置(classic binary search)，这三种找到目标的「代码是不一样的」
def binary_search_first_of_target_solution(nums: ArrayReader, target: int) -> int:
    first = nums.get(0)
    if first == target:
        return 0
    if first > target:
        return -1
    end = 1
    # 用倍增法找到右边界，这里其实隐含地用到了get(end)越界时，会返回2147483647的特性
    while nums.get(end) < target:
        end *= 2
    start = end // 2
    # find first_position的二分的while条件是 start + 1 < end
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums.get(mid) < target:
            start = mid
        else:
            end = mid
    if nums.get(start) == target:
        return start
    if nums.get(end) == target:
        return end
    return -1


def binary_search_first_of_target_template(nums: List[int], target: int):
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        middle = start + (end - start) // 2
        if nums[middle] < target:
            start = middle
        else:
            end = middle
        # 如果是二分搜索最后一个，除了start和end的赋值语句互换，if语句也要颠倒
        # if nums[middle] > target:
        #     end = middle
        # else:
        #     start = middle

    # 如果是二分搜索最后一个
    # if nums[end] == target要写在前面
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
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
