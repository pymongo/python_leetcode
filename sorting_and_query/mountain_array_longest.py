"""
https://leetcode.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode/
"""
import unittest
from typing import List


# 先从左到右找到第一个山脉数组的上山点，然后再往后搜索
def longest_mountain_in_array(nums: List[int]) -> int:
    max_len = 0
    # 初始状态
    start = -1  # 左边的山脚(上山点)
    is_increasing = False
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            if start == -1:
                start = i-1
            # 如果是先递减后递增，则需要更新 上山点 和 最大长度
            if not is_increasing:
                # 如果是初始状态，则不需要更新最大长度
                if start != -1:
                    max_len = max(max_len, i - start)
                start = i-1
            is_increasing = True
        elif nums[i] < nums[i-1]:
            is_increasing = False
        else:
            # 遇到前后两个值相等的情况，需要重新搜索上山点
            start = -1
            is_increasing = False
            pass

    #
    # size = len(nums)
    # if size < 3:
    #     return 0
    # i, max_len = 1, 0
    # while i < size:
    #     # 如果不满足递增条件，则继续往后搜索「上山点」
    #     while i < size and nums[i] <= nums[i - 1]:
    #         i += 1
    #     # 上山点
    #     start = i - 1
    #     # print(start)
    #     # 寻找山峰
    #     while i < size and nums[i] > nums[i - 1]:
    #         i += 1
    #     # 寻找下山底
    #     while i < size and nums[i] < nums[i - 1]:
    #         i += 1
    #     end = i - 1
    #     max_len = max(max_len, end - start + 1)
    #
    #     # 如果往后搜索也不可能找到更大的山脉，则跳出循环
    #     if size - i < max_len:
    #         break
    return max_len


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([2, 2, 2], 0),
        ([2, 1, 4, 7, 3, 2, 5], 5),
    ]

    def testing(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, longest_mountain_in_array(nums))
