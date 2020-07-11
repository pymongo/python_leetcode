"""
https://leetcode.com/problems/move-zeroes/
sort_color一题的简单版，将所有0移到右边
难以处理的是，不能改变原数组的大小顺序，与sort_color不同的是，需要3个元素之间互换，0移到最后，curr的左移，最后的值交换过来后再移到curr
如果当前元素是非0的，那么它的正确位置只可能是当前位置或更前面的位置
"""

import unittest
from typing import List


def move_zeros_slow_fast_two_pointers(nums: List[int]) -> None:
    length = len(nums)
    fast = 0
    # 快慢双指针，慢指针停在最后一个非0元素
    # 快指针遍历到头后，慢指针到数组结尾就全是0
    slow = 0
    while fast < length:
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    while slow < length:
        nums[slow] = 0
        slow += 1


class Testing(unittest.TestCase):
    """
    0 1 0 3 12
    ^ ^
    1 0 0 3 12

    """
    TEST_CASES = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 0, 3, 1], [3, 1, 0, 0, 0])
    ]

    def test_move_zeros(self):
        for nums, expected in self.TEST_CASES:
            move_zeros_slow_fast_two_pointers(nums)
            self.assertEqual(expected, nums)
