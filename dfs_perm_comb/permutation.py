"""
# TODO 求排列组合方案总数的算法

## 使用(Python3.8+)math.perm/comb 或 scipy.special.perm/comb
from scipy.special import comb, perm

## 排列方案总数就是阶乘，组合数计算的话看Unique Paths这题，注意溢出

TODO 本题相当于让你impl内置库: itertools.permutations
"""
import unittest
import itertools
import collections
from typing import List


class Solution(unittest.TestCase):
    def test_kth_permutation(self):
        TEST_CASES = [
            (3, 3, "213"),
            (4, 9, "2314"),
            (9, 214267, "635749128"),
        ]
        for n, k, permutation in TEST_CASES:
            self.assertEqual(permutation, self.kth_permutation(n, k))

    # 这种解法铁定超时，因为没有批量批量地去数
    # 更好的方案——用next_permutation的函数迭代k次
    def kth_permutation(self, n: int, k: int) -> str:
        used = [False] * (n + 1)
        curr = []
        # 构造阶乘数组，类似快速选择算法的剪枝过程，可以根据当前递归的层级推出可以剪枝叶子节点的数量
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        self.k = k

        def kth_permutation_dfs():
            depth = len(curr)
            if depth == n:
                return

            # 当前递归深度中，能排除的叶子节点数量
            leaf_cnt = factorial[n - 1 - depth]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if leaf_cnt < self.k:
                    self.k -= leaf_cnt
                    continue
                curr.append(i)
                used[i] = True
                kth_permutation_dfs()

                # 注意这里要加return，因为我们保证每次追加的数一定是正确的，不需要回溯
                return

        kth_permutation_dfs()
        return ''.join(iter(map(lambda num: str(num), curr)))


def my_permutation(nums: List[int]) -> List[List[int]]:
    results = []
    nums = sorted(nums)
    size = len(nums)
    used = [False] * size
    dfs([], used, 0, size, nums, results)
    return results


# 时间复杂度=方案总数*构造/保存/遍历方案的耗时: O(n! * n), 例如复制找到的其中一个答案到答案集就耗时O(n)
def dfs(
    permutation: List[int],
    used: List[bool],
    permutation_size: int,
    size: int,
    nums: List[int],
    results: List[List[int]]
):
    if permutation_size == size:
        results.append(permutation.copy())
        return

    for i in range(size):
        if used[i]:
            continue

        # 去重，解决Permutation II这题
        # used[i-1]=false表示回退的过程中刚刚被撤销的选择
        # 例如 [1,1,2], 遍历第一个1时也能选中112，但是从第一个1回退到根(空数组)再到1时，此时的1已被选过，不能继续展开，否则会出现重复解
        # 例如: a', a", b
        # 不能 x => a"->a'->b
        # 不能跳过第一个a'去选第二个a"
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue

        permutation.append(nums[i])
        used[i] = True

        dfs(permutation, used, permutation_size + 1, size, nums, results)

        # 为什么这里permutation_size不用复原?
        # 因为int类型在传参时都是Copy过去的，不会影响这里的int
        permutation.pop()
        used[i] = False


# https://lintcode.com/problem/string-permutation/
def str_permutation(s: str) -> List[str]:
    results = []
    chars = sorted(list(s))
    size = len(chars)
    permutation_visited = [False] * size
    dfs_str([], permutation_visited, 0, size, chars, results)
    return results


def dfs_str(
    permutation: List[str],
    used: List[bool],
    permutation_size: int,
    size: int,
    chars: List[str],
    results: List[str]
):
    if permutation_size == size:
        candidate = "".join(permutation)
        results.append(candidate)
        return

    for i in range(size):
        if used[i]:
            continue
        # used[i-1]=false表示回退的过程中刚刚被撤销的选择
        # 例如 [1,1,2], 遍历第一个1时也能选中112，但是从第一个1回退到根(空数组)再到1时，此时的1已被选过，不能继续展开，否则会出现重复解
        if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
            continue
        permutation.append(chars[i])
        used[i] = True

        dfs_str(permutation, used, permutation_size + 1, size, chars, results)

        permutation.pop()
        used[i] = False


# BFS的性能不如DFS
def permute_bfs(nums: List[int]) -> List[List[int]]:
    if len(nums) < 2:
        return [nums]
    queue = collections.deque()
    n = len(nums)
    # used = [[0] * n for _ in range(n)]
    res = []
    # depth = 0
    for start in range(n):
        queue.append([nums[start]])
        while queue:
            if queue[0] == n:
                break
            curr = queue.popleft()
            for j in range(n):
                if nums[j] not in curr:
                    curr.append(nums[j])
                    if len(curr) == n:
                        res.append(curr.copy())
                    queue.append(curr.copy())
                    curr.pop()
    return res


class Testing(unittest.TestCase):
    TEST_CASES = [
        [1, 2, 3]
    ]

    STR_PERMUTATION_2_CASES = [
        # 答案需要去重
        ("abb", ["abb", "bab", "bba"]),
        ("aabb", ["aabb", "abab", "baba", "bbaa", "abba", "baab"]),
    ]

    def test(self):
        for nums in self.TEST_CASES:
            correct_answer = list(map(lambda x: list(x), itertools.permutations(nums)))
            self.assertCountEqual(correct_answer, my_permutation(nums))

    def test_permute_bfs(self):
        for nums in self.TEST_CASES:
            correct_answer = list(map(lambda x: list(x), itertools.permutations(nums)))
            self.assertCountEqual(correct_answer, permute_bfs(nums))

    def test_str_permutation_2(self):
        for s, expected in self.STR_PERMUTATION_2_CASES:
            self.assertCountEqual(expected, str_permutation(s))
