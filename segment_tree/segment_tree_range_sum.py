"""
# 线段树-区间和
对于离线数据(静态数据)，求区间和主要有两种方法:
1. 普通的数组: 查询O(n)，更新O(1)
2. 前缀和数组: 查询O(1)，更新O(n)

线段树不仅能处理离线数据，而且非常适用于维护可变/动态数据

线段树-区间和的应用: 火币的币币交易网页右侧的订单买卖深度十档以及深度图

那么可以猜测线段树的查询和更新操作的时间复杂度都是O(logn)

静态区间和数据用前缀和，动态区间和数据用线段树；静态排序数据用快排，动态排序数据用堆

# 构建线段树
例如: nums=[0,1,2,3,4,5]
构建树的过程会像这样:
Round 1:
先中间切一刀
n = len(nums)
root = TreeNode(sum(nums))
root.left = TreeNode(sum(nums[:n//2]))
root.right = TreeNode(sum(nums[n//2:]))
 15
/ \
2 12
然后就左右子树分别递归呗
"""
import unittest
from typing import List
from binary_tree.binary_tree import TreeNode


class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        assert n > 0
        self.root = self.build_tree(nums, n)
        print(self.root.pretty())

    def build_tree(self, nums: List[int], n: int) -> TreeNode:
        if n == 1:
            return TreeNode(nums[0])
        node = TreeNode(sum(nums))
        # 尽量让左子树多一点
        half_n = (n + 1) // 2
        node.left = self.build_tree(nums[:half_n], half_n)
        node.right = self.build_tree(nums[half_n:], n - half_n)
        return node

    def update(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass


class TestSegmentTree(unittest.TestCase):
    def test_build_tree(self):
        tree = SegmentTree([1, 3, 5, 7, 9, 11])
