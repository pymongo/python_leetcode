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
