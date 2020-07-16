"""
本题类似find_in_mountain_array，不过山脉数组就一种先递增后递减的情况，而旋转排序数组复杂不少
"""

from typing import List
import unittest


# leetcode上的最佳解答
def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    size = len(nums)
    last = size - 1
    start, end = 0, last
    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] == target:
            return middle
        # 因为nums是有序数组循环移位后的数组
        # nums[0] <= nums[middle]表示[0,middle]是有序的
        if nums[0] <= nums[middle]:
            if nums[0] <= target < nums[middle]:
                # target在[0,middle]之间
                end = middle - 1
            else:
                start = middle + 1
        else:
            if nums[middle] < target <= nums[last]:
                # target在peak_index的右半部分
                start = middle + 1
            else:
                end = middle - 1
    return -1


def find_peak_index(nums: List[int], size: int) -> int:
    start, end = 0, size - 1
    if nums[start] <= nums[end]:
        return end
    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] > nums[middle + 1]:
            return middle
        elif nums[start] <= nums[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return 0


def my_solution(nums: List[int], target: int) -> int:
    size = len(nums)
    if size == 0:
        return -1
    peak_index = find_peak_index(nums, size)
    return -1


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([4, 5, 1, 2, 3], 1, 2),
        ([4, 5, 1, 2, 3], 0, -1),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ]

    def test_best_solution(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertEqual(expected, search_in_rotated_sorted_array(nums, target))

    def test_my_solution(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertEqual(expected, my_solution(nums, target))
