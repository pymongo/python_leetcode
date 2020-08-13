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
import heapq
from typing import List


class Solution(unittest.TestCase):
    @staticmethod
    def kth_smallest(k_small: int, nums: List[int]) -> int:
        size = len(nums)

        def kth_biggest(start: int, end: int, k: int) -> int:
            if start >= end:
                return nums[start]

            left, right = start, end
            pivot = nums[left + (right - left) // 2]
            while left <= right:
                while left <= right and nums[left] > pivot:
                    left += 1
                while left <= right and nums[right] < pivot:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            print(nums)
            print(start, right, left, end)

            # S R L E
            if start + k - 1 <= right:
                return kth_biggest(start, right, k)
            elif left + k - 1 <= end:
                return kth_biggest(left, end, k - (left - start + 1))
            else:
                return nums[left]

        # 求第k小的数等于求第size-k+1大的数
        return kth_biggest(0, size - 1, size - k_small + 1)


# Runtime: 96 ms, faster than 32.09%
def quick_select(nums: List[int], left: int, right: int, k: int) -> int:
    if left == right:
        return nums[left]

    # 使用i, j的目的是让第二步比较第k大的元素会落在哪个区间，而比较区间需要用到初始的left,right值
    i, j = left, right
    pivot = nums[(left + right) // 2]

    while i <= j:
        # 倒序排列，让大的元素在前面，方便找第k大
        while i <= j and nums[i] > pivot:
            i += 1
        # 倒序排列，让大的元素在前面，方便找第k大
        while i <= j and nums[j] < pivot:
            j -= 1

        if i <= j:
            # [1, 3, 4, 2] 测试用例
            # 第一遍快速排序后变成 [4, 3, 1, 2]，此时left=left=0, right=j=1
            # nums=[4],left=0,right=1时，这里会额外地交换一次
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    # 如果i==j时跳出循环，则j和i中间会有一个元素
    # 此时从左到右分别是 left j [some] i right

    if left + k - 1 <= j:
        # 第k大元素落在了pivot的左边区间(因为是倒序排列，所以是较大区间)
        return quick_select(nums, left, j, k)
    elif left + k - 1 >= i:
        # 第k大元素落在了pivot的右边区间，较大值中被排除了i-left项
        return quick_select(nums, i, right, k - (i - left))
    else:
        # 第k大元素恰好是j和i中间的元素
        return nums[j + 1]


# https://docs.python.org/3.8/library/heapq.html
def kth_largest_min_heap(nums: List[int], k: int) -> int:
    # return heapq.nlargest(k, nums)[k-1]
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        # 维护好最大的前k个数
        heapq.heappushpop(min_heap, num)
    return min_heap[0]


# 如果元素有偶数个，则返回右中位数
def median(nums: List[int]) -> int:
    size = len(nums)
    kth = size // 2

    def quick_select_inner(left: int, right: int, k: int) -> int:
        if left == right:
            return nums[left]

        start, end = left, right
        pivot = nums[start + (end - start) // 2]
        # 倒序快排
        while start <= end:
            while start <= end and nums[start] > pivot:
                start += 1
            while start <= end and nums[end] < pivot:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # 如果start=end时跳出循环，则end和start中间会有一个元素
        # 此时从左到右分别是 left end [some] start right
        if left + k - 1 <= end:
            # kth在pivot的左边区域
            return quick_select_inner(left, end, k)
        elif right + k - 1 >= start:
            # kth在pivot的右边区域
            return quick_select_inner(start, right, left + k - start)
        else:
            # k刚好是end和start之间的元素
            return nums[end + 1]

    return quick_select_inner(0, size - 1, kth)


class Test(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 4, 2], 1, 4),
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    def test_quick_select(self):
        for nums, k, expected in self.TEST_CASES[:]:
            print(nums)
            self.assertEqual(expected, quick_select(nums, 0, len(nums) - 1, k))

    def find_median(self):
        pass
