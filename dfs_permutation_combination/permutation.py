"""
# TODO 求排列组合方案总数的算法

## 使用scipy.special.perm/comb
from scipy.special import comb, perm

## 排列方案总数就是阶乘，组合数计算的话看Unique Paths这题，注意溢出

TODO 本题相当于让你impl内置库: itertools.permutations
"""
import unittest
import random
import itertools
from typing import List


def my_permutation(nums: List[int]) -> List[List[int]]:
    results = []
    size = len(nums)
    permutation_visited = [False] * size
    dfs([], permutation_visited, 0, size, nums, results)
    return results


def dfs(
    permutation: List[int],
    permutation_visited: List[int],
    permutation_size: int,
    size: int,
    nums: List[int],
    results: List[List[int]]
):
    if permutation_size == size:
        results.append(permutation.copy())
        return

    for i in range(size):
        if permutation_visited[i]:
            continue
        permutation.append(nums[i])
        permutation_visited[i] = True

        dfs(permutation, permutation_visited, permutation_size + 1, size, nums, results)

        permutation.pop()
        permutation_visited[i] = False


class Testing(unittest.TestCase):
    TEST_CASES = [
        [1, 2, 3]
    ]

    def test(self):
        for nums in self.TEST_CASES:
            correct_answer = list(map(lambda x: list(x), itertools.permutations(nums)))
            self.assertCountEqual(correct_answer, my_permutation(nums))
