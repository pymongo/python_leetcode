"""
https://leetcode.com/problems/find-k-closest-elements/
给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。在A中找与target最接近的k个整数。
返回这k个数并按照与target的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。
"""

import unittest
from typing import List


# 特殊的二分模板，返回target在数组中的相应位置的靠左索引
def binary_search(nums: List[int], target: int, length: int) -> int:
    """
    首先要明确这个二分查找函数的目标:
    目标1. 如果数组中存在target，则返回相应索引
    目标2. 如果数组中不存在target，但target在数组的最小值和最大值之间，则返回靠近target的左边一个元素的索引
    稍微推敲一下，目标1和目标2就不能同时满足
    调用binary_search的函数只能判断返回索引在数组左边、在数组内、在数组外
    目标1和目标2都属于数组内的情况，所以本函数不需要管target是否是数组的某个元素
    """
    start, end = 0, length - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
    # start==end==0
    if start == 0:
        # target小于数组第一个元素
        return -1
    elif start == length - 1:
        # target大于数组最后一个元素
        return length
    else:
        # [1, 2, 4, 5], 3 => 2
        # [1, 2, 4], 3 => 3
        return start


def solution(nums: List[int], target: int, k: int) -> List[int]:
    """
    1. 通过二分法找到target在数组中的位置
    """
    length = len(nums)
    position = binary_search(nums, target, length)
    if position == -1:
        return nums[:k]
    if position == length:
        return nums[length - k:]
    result = []
    left: int
    right: int
    if nums[position] == target:
        result.append(nums[position])
        left = position - 1
        right = position + 1
    else:
        left = position
        right = position + 1
    while right - left + 1 <= k:
        if left == -1 and right < length:
            result += nums[right:k]
            return result
        elif right == length and left > 0:
            result += nums[:left]
            return result
            # result.append(nums[left])
            # left -= 1
            # if right - left + 1 == k:
            #     return result
            # result.append(nums[left])
            # left -= 1
        else:
            if abs(nums[left]-target) < abs(nums[right]-target):
                result.append(nums[left])
                result.append(nums[right])
            else:
                result.append(nums[right])
                result.append(nums[left])
            left -= 1
            right += 1
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3], 2, 3, [2, 1, 3]),
        ([1, 4, 6, 8], 3, 3, [4, 1, 6]),
    ]

    def test_binary_search(self):
        print(binary_search([1, 2, 4], target=3, length=3))

    def test(self):
        for nums, target, k, expected in self.TEST_CASES:
            self.assertEqual(expected, solution(nums, target, k))
