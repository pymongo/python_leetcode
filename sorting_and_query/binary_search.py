import unittest
from copy import deepcopy


def solution(nums, target):
    size = len(nums)
    left, right = 0, size-1
    while left <= right:
        # FIXME 面试官可能会问，(left+right)//2会有什么问题
        # left+right可能会i32/u32溢出，解决办法是写成 middle = start + (end - start) / 2
        # 实际上i32数组如果有2**31个元素，那么要占用4*4G的内存
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle-1
        elif nums[middle] < target:
            left = middle+1
        else:
            return middle
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1)
    ]

    def test(self):
        for nums, target, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, solution(nums, target))
