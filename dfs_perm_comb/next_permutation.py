import unittest
from typing import List


class Solution(unittest.TestCase):
    TESTCASES = [
        ([1, 5, 1], [5, 1, 1]),
        ([1, 3, 2], [2, 1, 3]),
        ([1, 3, 2, 3], [1, 3, 3, 2]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
    ]

    def test(self):
        for nums, next_nums in self.TESTCASES:
            self.assertListEqual(next_nums, self.next_permutation(nums))

    # 该题跟C++ STL的next_permutation函数完全一样
    # https://imageslr.github.io/2020/01/29/leetcode-36.html#%E8%A7%A3%E6%B3%95%E4%B8%80%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%8E%92%E5%88%97
    @staticmethod
    def next_permutation(nums: List[int]) -> List[int]:
        # leetcode要求是In-Place，lintcode要求返回数组，我这里就原地修改数组后返回原数组
        n = len(nums)
        if n < 2:
            return nums

        # 1. 我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。
        # 2. 我们还希望下一个数增加的幅度尽可能的小
        # 因此只需要将后面的「大数j」与前面的「小数i」交换

        # j表示需要换到前面的大数
        i, j = n - 2, n - 1

        # 找到第一对递增的i和j，最终停下来时i的位置就是大数要换到的位置
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        # i停下来时，i的位置是大数要替换到的位置，[j,len(nums))必为降序，于是从后往前找一个大于i当前位置的数替换过去，
        # 就能实现下一个数增加的幅度尽可能的小
        if i >= 0:
            k = n - 1
            # 为什么要用=号?
            # [1,5,1]
            #  ^   ^
            #  i   k
            # 这种情况下，nums[i]和nums[k]相等，不换后不满足让下一个排列「变大」的要求
            while nums[k] <= nums[i]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        # nums完全逆序或[1,3,2] -> [2,3,1]之后要把[j,end)部分逆序成[2, 1, 3]
        # 逆置 [j,end)，使其升序，让下一个数增加的幅度尽可能的小
        left, right = j, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


