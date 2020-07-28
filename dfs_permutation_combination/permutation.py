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


# 时间复杂度=方案总数*构造/保存/遍历方案的耗时: O(n! * n), 例如复制找到的其中一个答案到答案集就耗时O(n)
def dfs(
    permutation: List[int],
    permutation_visited: List[bool],
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

        # 为什么这里permutation_size不用复原?
        # 因为int类型在传参时都是Copy过去的，不会影响这里的int
        permutation.pop()
        permutation_visited[i] = False


def str_permutation(s: str) -> List[str]:
    results = []
    chars = list(s)
    size = len(chars)
    permutation_visited = [False] * size
    dfs_str([], permutation_visited, 0, size, chars, results)
    return results


def dfs_str(
    permutation: List[str],
    permutation_visited: List[bool],
    permutation_size: int,
    size: int,
    chars: List[str],
    results: List[str]
):
    if permutation_size == size:
        candidate = "".join(permutation)
        # TODO 去重的方法太笨了吧
        if candidate not in results:
            results.append(candidate)
        return

    for i in range(size):
        if permutation_visited[i]:
            continue
        permutation.append(chars[i])
        permutation_visited[i] = True

        dfs_str(permutation, permutation_visited, permutation_size + 1, size, chars, results)

        permutation.pop()
        permutation_visited[i] = False


class Testing(unittest.TestCase):
    TEST_CASES = [
        [1, 2, 3]
    ]

    STR_PERMUTATION_2_CASES = [
        ("abb", ["abb", "bab", "bba"]),
        ("aabb", ["aabb", "abab", "baba", "bbaa", "abba", "baab"]),
    ]

    def test(self):
        for nums in self.TEST_CASES:
            correct_answer = list(map(lambda x: list(x), itertools.permutations(nums)))
            self.assertCountEqual(correct_answer, my_permutation(nums))

    def test_str_permutation_2(self):
        for s, expected in self.STR_PERMUTATION_2_CASES:
            self.assertCountEqual(expected, str_permutation(s))
