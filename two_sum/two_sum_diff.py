"""
要注意target是负数的情况，本题最简单的做法是HashMap记录
如果要求O(1)空间复杂度，有没有哈希表的替代方案? -> 排序+二分搜索
但是这题用同向双指针可以做到O(n)的时间复杂度

注意输入数组是有序的
"""
import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 15, 24], 5, [2, 7]),
        ([1, 1], 0, [1, 1]),
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertListEqual(expected, self.f(nums, target))
            self.assertListEqual(expected, self.hash_solution(nums, target))

    @staticmethod
    def f(nums: List[int], target: int) -> List[int]:
        """
        同向双指针: 由于i往右走的时候nums[j]-nums[i]会变大，所以j也需要往右走
        所以j前进一点，然后i前进一点，这样如此反复地搜索(有点像Sliding Window)，最坏情况也就O(2n)
        """
        size = len(nums)
        # 因为  target=-2, nums[i]=9,nums[j]=7
        # 等同于 target=2, nums[i] - nums[j]
        # 所以target是正是负没关系，i和j对调就行
        abs_target = abs(target)

        # 由于题目提示一定有解，所以数组长度至少为2
        # TODO 同向双指针的模板
        j = 1
        for i in range(size):
            # target=0时，[0,1,2,2]，必须要让j始终在i的右边(i和j要不一样)
            j = max(j, i + 1)

            while j < size and nums[j] - nums[i] < abs_target:
                j += 1
            if j == size:
                break
            if nums[j] - nums[i] == abs_target:
                return [nums[i], nums[j]]

        raise Exception("Unreachable")

    @staticmethod
    def hash_solution(nums: List[int], target: int) -> List[int]:
        m = dict()
        target = abs(target)
        for num in nums:
            if num in m:
                return [m[num], num]
            else:
                m[target + num] = num
        raise Exception("Unreachable")
