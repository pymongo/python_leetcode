import unittest
from typing import List


# 注意candidates内的元素可以重复使用
# 我的思路是不断reduce candidates和target，转化成更简单的类似two-sum的问题
# 实际上这题就是1-sum, 2-sum, ... ,k-sum = target的问题，其中k=target // min(nums)
def dfs_helper(nums: List[int], target: int) -> List[List[int]]:
    # 去重并排序
    nums = sorted(list(set(nums)))
    size = len(nums)
    results = []
    dfs(nums, target, 0, size, [], results)
    return results


# BFS不容易实现target的reduce，不建议折腾BFS写法，背熟这个模板即可
def dfs(nums: List[int], target: int, nums_start: int, size: int, combination: List[int], results: List[List[int]]):
    if target == 0:
        results.append(combination.copy())
        return
    for i in range(nums_start, size):
        residue = target - nums[i]
        if residue < 0:
            # 因为数组是升序，往后都不可能匹配到
            break
        combination.append(nums[i])
        dfs(nums, residue, i, size, combination, results)
        # 将combination回溯到还没.append(nums[i])的状态，以便每趟for循环开始时nums都一样
        combination.pop()


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 3, 6, 7], 7, [[7], [2, 2, 3]]),
        ([1], 3, [[1, 1, 1]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ]

    def test_dfs(self):
        for nums, target, combination in self.TEST_CASES:
            self.assertCountEqual(combination, dfs_helper(nums, target))
