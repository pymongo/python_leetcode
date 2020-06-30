"""
https://www.lintcode.com/problem/kth-largest-element/
https://leetcode.com/problems/kth-largest-element-in-an-array/
quick select算法
找到n个无序元素中的第K大元素
O(n)时间复杂度
这里不能用打擂台比最大值的方式去模拟，这里求的是第K大

如果调用内置库，两行就搞定：
nums.sort()
return nums[len(nums)-k]
"""

import unittest
from typing import List


def quick_select(nums: List[int], k: int) -> int:
    size = len(nums)
    quick_sort_in_place(nums, 0, size - 1)
    print("after sort", nums)
    return -1


def quick_sort_in_place(nums: List[int], left, right):
    if left >= right:
        return
    middle = (left + right) // 2
    pivot = nums[middle]
    while left <= right:
        while left <= right and nums[left] <= pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    quick_sort_in_place(nums, left, middle-1)
    quick_sort_in_place(nums, middle+1, right)



class Test(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 4, 2], 1, 4),
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    def test_quick_select(self):
        for nums, k, expected in self.TEST_CASES[:]:
            print(nums)
            self.assertEqual(expected, quick_select(nums, k))
