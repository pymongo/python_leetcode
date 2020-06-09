"""
## Relative Problems
- [冒泡/选择/插入](https://lintcode.com/problem/sort-integers)
- https://lintcode.com/problem/sort-integers-ii
- https://leetcode.com/problems/sort-an-array/

## Reference:
https://www.jianshu.com/p/bbbab7fa77a2
"""
import unittest
from typing import List


def bubble_sort(nums: List[int]):
    """
    平均O(n^2)，最好O(n)，最坏O(n^2)；稳定排序
    Worst Case: 入参是反序的
    """
    length: int = len(nums)
    for i in range(length-1):
        for j in range(i+1, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def selection_sort(nums: List[int]):
    """
    遍历n-1次，第一次遍历找到最小值与索引0进行互换，第二次遍历找到次小值......
    选择排序比冒泡蠢在，当前遍历没有利用上次遍历的结果，而冒泡排序遍历时不断将更大的数换到后面，所以冒泡排序最后的几次遍历耗时很短
    平均/最好/最坏都是O(n^2)；不稳定排序
    """
    length: int = len(nums)
    min_index: int
    for i in range(length-1):
        min_index = i
        for j in range(i, length):
            if nums[i] > nums[j]:
                min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5])
    ]

    def test_bubble_sort(self):
        for case in self.TEST_CASES[:]:
            # assertEqual(Expected, Actual)
            # rust的assert_eq!比较直观，不限定左边还是右边放期待值，assert_eq!(Left, Right)
            self.assertEqual(case[1], bubble_sort(case[0]))

    def test_selection_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], selection_sort(case[0]))



