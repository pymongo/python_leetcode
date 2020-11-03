"""
本题类似find_in_mountain_array，不过山脉数组就一种先递增后递减的情况，而旋转排序数组复杂不少
可以画柱状图或散点图去理解
rotated sorted array其实就两段斜率为正的线段，值较高的线段会出现在前面
注意这题不会出现重复元素，而本题的follow up可能会有重复元素
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


def binary_search(nums: List[int], start: int, end: int, target: int) -> int:
    # peak_index的解法不能用start + 1 < end的二分模板，因为很可能peak_index=last, start=peak_index+1 最后判断nums[start]==target时会越界
    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] < target:
            start = middle + 1
        elif nums[middle] > target:
            end = middle - 1
        else:
            return middle
    return -1


# 不知道为什么find_peak_index之后二分查找[1, 3]中的3容易越界(因为第二个二分区间是3)
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
    # 如果数组内没找到山峰，那么山峰只可能是第一个元素
    return 0


def peak_index_solution(nums: List[int], target: int) -> int:
    size = len(nums)
    if size == 0:
        return -1
    peak_index = find_peak_index(nums, size)
    last = size - 1
    if nums[0] <= target <= nums[peak_index]:
        return binary_search(nums, 0, peak_index, target)
    # elif nums[peak_index+1] <= target <= nums[last]:
    else:
        # if peak_index == last:
        #     return -1
        return binary_search(nums, peak_index + 1, last, target)


# 153. Find Minimum in Rotated Sorted Array 一题的解法
# Your submission beats 98.00% Submissions!
def find_minimum_value_in_rotated_sorted_array(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        middle = start + (end - start) // 2
        # 比较中间和右边
        if nums[middle] < nums[end]:
            end = middle
        else:
            # [3,4,5,1,2], nums[middle]=5, start需要前移, nums[middle]已经是最大值了，所以要start前移到middle+1的位置
            # 如果不知道二分的边界变化，找一个例子代入进去试试就好
            # 大于等于或小于等于的二分分支可以start=middle+1或end=middle-1
            start = middle + 1
    return nums[start]


def get_min_index(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        middle = start + (end - start) // 2
        if nums[middle] < nums[end]:
            end = middle
        else:
            start = middle + 1
    return start


def min_index_solution(nums: List[int], target: int) -> int:
    size = len(nums)
    if size == 0:
        return -1
    min_index = get_min_index(nums)
    # 与peak_index解法相反，min_index解法要先搜索右半部分
    # TODO 总结来说，要优先搜索min_index不会减1 或 peak_index不会加1 的区域
    if nums[min_index] <= target <= nums[-1]:
        # 如果先搜索[0, min_index-1]区域，遇上[1],1的输入用例会min_index-1=-1
        return binary_search(nums, min_index, size - 1, target)
    else:
        return binary_search(nums, 0, min_index - 1, target)


class Testing(unittest.TestCase):
    TESTCASES = [
        ([1], 1, 0),
        ([1, 3], 0, -1),
        ([4, 5, 1, 2, 3], 1, 2),
        ([4, 5, 1, 2, 3], 0, -1),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ]

    def test_best_solution(self):
        for nums, target, expected in self.TESTCASES:
            self.assertEqual(expected, search_in_rotated_sorted_array(nums, target))

    def test_peak_index_solution(self):
        for nums, target, expected in self.TESTCASES:
            self.assertEqual(expected, peak_index_solution(nums, target))

    def test_min_index_solution(self):
        for nums, target, expected in self.TESTCASES:
            self.assertEqual(expected, min_index_solution(nums, target))

    def test_binary_search(self):
        print(binary_search([3, 1, 1], 0, 2, 3))
