"""
In-place重排数组，使得正负交替出现
1. 统计正负数个数，如果正数更多则第一位是正数
"""
import unittest
from typing import List


# |144|[interleaving_positive_and_negative_numbers]
def partition_positive_and_negative(nums):
    positive_count = 0
    negative_count = 0
    size = len(nums)
    for i in range(size):
        if nums[i] > 0:
            positive_count += 1
        elif nums[i] < 0:
            negative_count += 1
    divide_positive_and_negative(nums, size, positive_count > negative_count)
    interleave(nums, size, positive_count == negative_count)


# 分离正数和负数
def divide_positive_and_negative(nums, size, first_positive):
    flag = 1 if first_positive else -1
    left, right = 0, size - 1
    while left <= right:
        while left <= right and nums[left] * flag > 0:
            left += 1
        while left <= right and nums[right] * flag < 0:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


def interleave(nums, size, positive_and_negative_same_len):
    left, right = 1, size - 1
    if positive_and_negative_same_len:
        # 如果正负数量相同，则负数的指针指向倒数第二个
        right = size - 2
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 2
        right -= 2


class Testing(unittest.TestCase):
    TEST_CASES = [
        [-1, -2, -3, 4, 5, 6]
    ]

    def test(self):
        for nums in self.TEST_CASES:
            partition_positive_and_negative(nums)
            is_positive = nums[0] > 0
            for num in nums:
                self.assertEqual(num > 0, is_positive)
                is_positive = not is_positive
