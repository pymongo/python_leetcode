import unittest
from typing import List


# 这题与combination_sum很相似
def k_sum_2(nums: List[int], k: int, target: int) -> List[List[int]]:
    size = len(nums)
    if size == 0:
        return []
    results = []
    # 题目给定n个不同的正整数，所以不需要去重
    nums = sorted(nums)
    dfs(target, k, nums, 0, size, [], results)
    return results


def dfs(
    target: int,
    k: int,
    nums: List[int],
    nums_start: int,
    size: int,
    combination: List[int],
    results: List[List[int]]
) -> None:
    if k == 0:
        if target == 0:
            results.append(combination.copy())
        return
    for i in range(nums_start, size):
        residue = target - nums[i]
        if residue < 0:
            break
        combination.append(nums[i])
        dfs(target - nums[i], k - 1, nums, i + 1, size, combination, results)
        combination.pop()


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3, 4], 2, 5, [[1, 4], [2, 3]]),
        ([1, 3, 4, 6], 3, 8, [[1, 3, 4]]),
    ]

    def test(self):
        for nums, k, target, results in self.TEST_CASES:
            self.assertCountEqual(results, k_sum_2(nums, k, target))
