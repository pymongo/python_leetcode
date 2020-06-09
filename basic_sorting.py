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
    「堆排序」是选择排序的更高效算法
    """
    length: int = len(nums)
    min_index: int
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def heap_sort_dfs(nums: List[int], length: int, i: int):
    """
    【完全二叉树】从上到下，从左到右生成的二叉树
    【数据结构-堆】1. 是个完全二叉树 2. 父节点的数值比子节点大
    【heapify】将一个完全二叉树按堆的规则进行重排
    1. 用数组模拟完全二叉树，从上到下从左到右地编号，假设节点的索引为i，有如下规律
    1.1 i的父节点索引parent=(i-1)/2
    1.2 i的左子节点索引c1=2*i+1
    1.3 i的右子节点索引c2=2*i+2
    2. 如何进行heapify
    从左到右开始遍历倒数第二层(k-1)层的子节点，每个子节点做一次3数最大值的运算，再把当前节点和当前节点的子节点的最大值做交换
    对O(n)级别个非叶子节点进行堆调整操作O(logn)，时间复杂度O(nlogn)；
    之后每一次堆调整操作确定一个数的次序，时间复杂度O(nlogn)。合起来时间复杂度O(nlogn)
    平均/最好/最坏都是O(nlogn)；不稳定排序
    """
    def heapify(nums: List[int], length: int, i: int):
        """
        调整完全二叉树，使二叉树满足堆的第二个条件(父节点的数值比子节点大)
        """
        last_node: int = length-1
        last_node_parent: int = (last_node-1)//2
        for i in range(last_node_parent, -1, -1):
            children_left: int = 2*i+1
            children_right: int = 2*i+1
            max_index: int = i
            if children_left < length and nums[children_left] > nums[max_index]:
                max_index = children_left
            if children_right < length and nums[children_right] > nums[max_index]:
                max_index = children_right
            if max_index != i:
                nums[i], nums[max_index] = nums[max_index], nums[i]
                # min_index节点发生了值变动，重新/再次检查下min_index作为的父节点是否满足堆的条件
                heapify(nums, length, max_index)


def binary_search(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    middle: int
    while left < right and right > 1:
        # 如果middle是(left+right) // 2
        # 遇到([1, 2, 3], 4)的测试用例时会陷入死循环(left, right = 1, 2)
        middle = (left + right) // 2
        print(f"left, right = {left}, {right}")
        print(f"middle = {middle}")
        if nums[middle] == target:
            print("nums[middle] == target")
            return middle
        elif nums[middle] > target:
            print("nums[middle] > target")
            right = min(middle, right-1)
        else:
            print("nums[middle] < target")
            left = max(middle, left+1)
    print(f"left, right = {left}, {right}")
    # 一般的二分查找找不到是返回return -1
    # 这里我想模仿Rust的二分查找，无论找不找得到，都返回一个应当插入位置的索引
    if nums[left] > target:
        return left
    else:
        return right


def insertion_sort(nums: List[int]) -> List[int]:
    """
    插入排序类型斗地主发牌时，将新的牌插入到已经有序的手牌中
    优化算法是通过binary_search找到插入的索引
    「希尔排序」是插入排序的更高效算法
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
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            nums[binary_search_index] = current_num
        # List[int]不需要pretty print
        p(nums)
        p('==' * 10)
        print()
    return nums


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([5, 3, 4, 2], [2, 3, 4, 5]),
        ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5]),
        ([4, 10, 3, 5, 1, 2], [1, 2, 3, 4, 5, 10])
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

    def test_heap_sort_dfs(self):
        for case in self.TEST_CASES[:]:
            nums = case[0][:]
            heap_sort_dfs(nums, len(nums), 0)
            self.assertEqual(case[1], nums)

    def test_binary_search(self):
        for case in self.BINARY_SEARCH_CASES[:]:
            self.assertEqual(case["expected"], binary_search(*case["input"]))

    def test_insertion_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], insertion_sort(case[0]))
