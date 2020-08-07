import unittest

from typing import List
import math


# 给你一个数组, i,j是数组内任意两个小标，让你数i<j且nums[i]==nums[j]一共有几对
class Solution:
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # key: num, value: count of num
        pairs_count = 0
        num_count = dict()
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        # 其实不用管相同数字的先后顺序，例如num出现了value次，那么就有组合数C(value, 2)个pairs
        for value in num_count.values():
            if value == 1:
                continue
            # math.comb是Python 3.8新增API，我本地的PyCharm貌似还查不到这个API
            # noinspection PyUnresolvedReferences
            # pairs_count += math.comb(value, 2)
            pairs_count += (value * (value - 1) // 2)
        return pairs_count


class Testing(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(4, solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
        self.assertEqual(6, solution.numIdenticalPairs([1, 1, 1, 1]))
