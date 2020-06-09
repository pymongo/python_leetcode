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
from pprint import pprint as p


def bubble_sort(nums: List[int]) -> List[int]:
    """
    平均O(n^2)，最好O(n)，最坏O(n^2)；稳定排序
    Worst Case: 入参是反序的
    """
    length: int = len(nums)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def selection_sort(nums: List[int]) -> List[int]:
    """
    遍历n-1次，第一次遍历找到最小值与索引0进行互换，第二次遍历找到次小值......
    选择排序比冒泡蠢在，当前遍历没有利用上次遍历的结果，而冒泡排序遍历时不断将更大的数换到后面，所以冒泡排序最后的几次遍历耗时很短
    平均/最好/最坏都是O(n^2)；不稳定排序
    """
    length: int = len(nums)
    min_index: int
    for i in range(length - 1):
        min_index = i
        for j in range(i, length):
            if nums[i] > nums[j]:
                min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def binary_search(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    middle: int
    while left < right and right > 1:
        # 如果middle是(left+right)//2
        # 遇到([1, 2, 3], 4)的测试用例时会陷入死循环(left, right = 1, 2)
        middle = (left + right + 1) // 2
        print(f"left, right = {left}, {right}")
        print(f"middle = {middle}")
        if nums[middle] == target:
            print("nums[middle] == target")
            return middle
        elif nums[middle] > target:
            print("nums[middle] > target")
            right = middle
        else:
            print("nums[middle] < target")
            left = middle
    print(f"left, right = {left}, {right}")
    return left


def insertion_sort(nums: List[int]) -> List[int]:
    """
    插入排序类型斗地主发牌时，将新的牌插入到已经有序的手牌中
    优化算法是通过binary_search找到插入的索引
    由于二分/折半查找只是减少了比较的次数，插入元素时元素的移动也耗费O(n)的时间，所以时间复杂度跟冒泡排序一样
    平均O(n^2)，最好O(n)，最坏O(n^2)；稳定排序
    Worst Case: 入参是反序的
    """
    length: int = len(nums)
    current_num: int
    for i in range(1, length):
        print()
        p('==' * 10)
        p((nums[:i], nums[i]))
        binary_search_index = binary_search(nums[:i], nums[i])
        p(f"binary_search_index, i = {binary_search_index}, {i}")
        if binary_search_index < i and nums[binary_search_index] > nums[i]:
            current_num = nums[i]
            # 将比nums[i]更大的元素往右移一格
            for j in range(i, binary_search_index, -1):
                nums[j], nums[j-1] = nums[j-1], nums[j]
            nums[binary_search_index] = current_num
        # List[int]不需要pretty print
        p(nums)
        p('==' * 10)
        print()
    return nums


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5])
    ]
    BINARY_SEARCH_CASES = [
        {
            "input": ([1, 2, 3], 0),
            "expected": 0
        },
        {
            "input": ([1, 2, 3], 1),
            "expected": 0
        },
        {
            "input": ([1, 2, 3], 2),
            "expected": 1
        },
        {
            "input": ([1, 2, 3], 3),
            "expected": 2
        },
        {
            "input": ([1, 2, 3], 4),
            "expected": 2
        },
    ]

    def test_bubble_sort(self):
        for case in self.TEST_CASES[:]:
            # assertEqual(Expected, Actual)
            # rust的assert_eq!比较直观，不限定左边还是右边放期待值，assert_eq!(Left, Right)
            self.assertEqual(case[1], bubble_sort(case[0]))

    def test_selection_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], selection_sort(case[0]))

    def test_binary_search(self):
        for case in self.BINARY_SEARCH_CASES[:]:
            self.assertEqual(case["expected"], binary_search(*case["input"]))

    def test_insertion_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], insertion_sort(case[0]))
