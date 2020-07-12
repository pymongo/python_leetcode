"""
|26|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|[Python](https://github.com/pymongo/rust_leetcode/blob/master/src/bitwise/remove_duplicates_from_sorted_array.py)|exclusive_or|
对于有序数组而言，从左到右的两两「异或」 如果异或的结果等于0，则找到第一个重复元素
而题目要求找的是无重复的个数，而且要挪动数组
"""
import unittest
from typing import List


def xor_iter(nums: List[int]) -> int:
    length = len(nums)
    if length <= 1:
        return length
    last_unique_index = 1
    for i in range(1, length):
        # 这里想多了，参考官方题解不需要用异或
        # if nums[i] ^ nums[i - 1] == 0:
        if nums[i] == nums[i - 1]:
            continue
        nums[last_unique_index] = nums[i]
        last_unique_index += 1
    return last_unique_index


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([], 0, []),
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
    ]

    def test_xor_iter(self):
        for nums, unique_len, expected in self.TEST_CASES:
            output = xor_iter(nums)
            self.assertEqual(unique_len, output)
            self.assertEqual(expected, nums[:unique_len])
