import unittest
from typing import List


# 有两个互为anagram的数组(anagram的定义请看valid_anagram一题)
# 请你找出A的每个元素在B中的索引，如有重复元素则返回任意一个索引
# 例如A=[12,28],B=[28,12]，因为A[0]=B[1],A[1]=B[0]，所以返回[1,0]
class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        b_map = dict()
        size = 0
        for i, num in enumerate(B):
            b_map[num] = i
            size += 1
        for i in range(size):
            # 这是我的小技巧, 直接In-Place修改A, 优化性能
            A[i] = b_map[A[i]]
        return A


class Testing(unittest.TestCase):
    TESTCASES = [
        ([12, 28, 46, 32, 50], [50, 12, 32, 46, 28], [1, 4, 3, 2, 0]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [4, 3, 2, 1, 0]),
    ]

    def test_anagram(self):
        solution = Solution()
        for A, B, mapping in self.TESTCASES:
            self.assertEqual(mapping, solution.anagramMappings(A, B))
