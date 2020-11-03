"""
https://leetcode.com/problems/move-zeroes/
sort_color一题的简单版，将所有0移到右边
难以处理的是，不能改变原数组的大小顺序，与sort_color不同的是，需要3个元素之间互换，0移到最后，curr的左移，最后的值交换过来后再移到curr

"""

import unittest
from typing import List


def move_zeros_slow_fast_two_pointers(nums: List[int]) -> None:
    length = len(nums)
    fast = 0
    # 快慢双指针，慢指针停在最后一个非0元素
    slow = 0
    while fast < length:
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    # 快指针遍历到头后(说明非0元素已经挪动完成)，将从慢指针往后的所有元素设为0
    while slow < length:
        nums[slow] = 0
        slow += 1


# https://leetcode-cn.com/problems/move-zeroes/solution/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/
def move_zeros_quick_sort_partition(nums: List[int]) -> None:
    curr, last_non_zero_found_at = 0, 0
    while curr < len(nums):
        # 如果当前元素是非0的，那么它的正确位置只可能是当前位置或更前面的位置
        if nums[curr] != 0:
            nums[last_non_zero_found_at], nums[curr] = nums[curr], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1
        curr += 1


# leetcode 27. Remove Element
# 这题跟move_zeros完全一样，或者说move_zeros就是target=0的remove_element
# In-Place, 将num=target的挪到数组末尾，然后返回数组前半部分不等于target的元素个数
def remove_element(nums: List[int], target: int) -> int:
    not_eq_target = 0
    for curr in range(len(nums)):
        if nums[curr] != target:
            nums[curr], nums[not_eq_target] = nums[not_eq_target], nums[curr]
            not_eq_target += 1
    return not_eq_target + 1


# leetcode 26. Remove Duplicates from Sorted Array, 还是一样，把Unique的挪到前面，重复的扔到数组后面 用不上两两异或
def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    unique_ptr = 0
    for curr in range(len(nums)):
        if nums[curr] != nums[unique_ptr]:
            # 这里不同的是，unique_ptr要先加后互换
            # 如果不是先加后互换会变成[1,1,2] -> [2,1,1]
            unique_ptr += 1
            nums[curr], nums[unique_ptr] = nums[unique_ptr], nums[curr]
    return unique_ptr


def remove_duplicates_from_sorted_array_2(nums: List[int]) -> int:
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
    TESTCASES = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 0, 3, 1], [3, 1, 0, 0, 0])
    ]

    def test_move_zeros_slow_fast_two_pointers(self):
        for nums, expected in self.TESTCASES:
            move_zeros_slow_fast_two_pointers(nums)
            self.assertEqual(expected, nums)

    def test_move_zeros_quick_sort_partition(self):
        for nums, expected in self.TESTCASES:
            move_zeros_quick_sort_partition(nums)
            self.assertEqual(expected, nums)
