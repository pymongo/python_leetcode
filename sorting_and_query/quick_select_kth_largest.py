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
