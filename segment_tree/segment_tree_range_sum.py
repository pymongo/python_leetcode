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


class SegmentTreeTreeNodeImpl:
    def __init__(self, nums: List[int]):
        n = len(nums)
        assert n > 0
        self.root = self.build_tree(nums, n)
        print(self.root.pretty())

    def build_tree(self, nums: List[int], n: int) -> TreeNode:
        if n == 1:
            return TreeNode(nums[0])
        node = TreeNode(0)
        # 尽量让左子树多一点
        half_n = (n + 1) // 2
        node.left = self.build_tree(nums[:half_n], half_n)
        node.right = self.build_tree(nums[half_n:], n - half_n)
        node.val = node.left.val + node.right.val
        return node


# 类似堆使用数组来操作，满二叉树使用数组操作的代码会很简单
# 由于往上缺乏使用二叉树实现的线段树的例子(让我临摹)，所以还是先背熟用数组实现的线段树吧
class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * 2 * self.n
        self.nums = nums
        self._build_tree()

    def _build_tree(self):
        """
        nums=[0,1,2,3,4,5]
        self.tree=  index(sum)
        1(15)
        /   \
            2(14)
                /\
        3(1)  4(5) 9(5)
        ...
        tree[6:]=[0,1,2,3,4,5]
        注意偶数索引的在左子树
        """
        n = self.n
        for i, j in zip(range(n, 2 * n), range(n)):
            self.tree[i] = self.nums[j]
        for i in range(n - 1, 0, -1):
            # 注意这种不是完全二叉树，是空间优化过的写法，左子树的编号是2*i，不要联想到堆是2*i+1
            # TODO 注意tree[0]是DummyNode，真正的根是tree[1]
            left = 2 * i
            right = left + 1
            self.tree[i] = self.tree[left] + self.tree[right]

    def update(self, i: int, val: int):
        pos = i + self.n
        self.tree[pos] = val
        while pos > 0:
            left, right = pos, pos
            if pos % 2 == 0:
                # 叶子节点中偶数索引的在左子树
                right = pos + 1
            else:
                left = pos - 1
            parent_pos = pos // 2
            self.tree[parent_pos] = self.tree[left] + self.tree[right]
            pos = parent_pos

    # noinspection PyPep8Naming
    def sumRange(self, i: int, j: int) -> int:
        i += self.n
        j += self.n
        sum_range = 0
        while i <= j:
            if i % 2 == 1:
                # 如果左指针指向一个右节点，就不能直接上到父节点，因为父节点是左右子节点的和
                # 这里只有一个右节点，左节点不在范围内(越界)
                # 于是把这个落单的右节点加上，
                sum_range += self.tree[i]
                # 左指针移动到右边相连的树上
                i += 1
            if j % 2 == 0:
                # 如果右指针指向一个左节点，就把这个落单的左节点单独加上，
                sum_range += self.tree[j]
                # 右指针移动到左边相邻的那棵树上
                j -= 1
            # 左右指针移动到父节点，然后收缩边界(shrink)
            i //= 2
            j //= 2
        return sum_range


class TestSegmentTree(unittest.TestCase):
    def test_build_tree(self):
        # tree = SegmentTreeTreeNodeImpl([0, 1, 2, 3, 4, 5])
        # tree = SegmentTreeTreeNodeImpl([0, 1, 2, 3, 4, 5, 6])
        tree = SegmentTree([0, 1, 2, 3, 4, 5])
        tree.sumRange(1, 5)
        # print(tree.tree)
