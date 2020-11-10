"""
这题输入用例是二叉树，需要构思一种创建二叉树的方式才能构建单元测试
TODO 先不写单元测试，等leetcode做到pretty print二叉树以及创建二叉树的相关题目时再补充单元测试
BFS的三种辅助数据结构: 1. 单个队列
BFS的三种辅助数据结构: 2. 双队列
BFS的三种辅助数据结构: 3. DummyNode(哨兵节点)
简单讲解下DummyNode解法，例如队列: 1#23, #表示空指针，1是第一层树，23是第二层

二叉树的BFS可以借助单队列+DummyNode，但是图的BFS就复杂多了
二叉树可以看做是一种特殊的图
二叉树中进行 BFS 和图中进行 BFS 最大的区别就是二叉树中无需使用 HashSet（C++: unordered_map, Python: dict) 来存储访问过的节点（丢进过 queue 里的节点）
因为二叉树这种数据结构，上下层关系分明，没有环（circle），所以不可能出现一个节点的儿子的儿子是自己的情况。
但是在图中，一个节点的邻居的邻居就可能是自己了。

有很多种方法可以存储一个图，最常用的莫过于：
1.邻接矩阵
2.邻接表
而邻接矩阵因为耗费空间过大，我们通常在工程中都是使用邻接表作为图的存储结构
"""
import unittest
import collections
from .binary_tree import TreeNode
from typing import List


# 那么二叉树的经典遍历pre-order, in-order, after-order就只能用递归吗?
# 这题还能用双队列遍历，一个是curr_queue，一个是next_queue，有点像不断往前拓展滚动的感觉，老的queue就会被垃圾回收掉
# 双队列 1. new一个next_queue，将当前queue中能展开的子树扔到新的next_queue
# 双队列 2. 遍历完curr_queue后，curr_queue指向next_queue
def level_order(root: TreeNode):
    if not root:
        return []
    # Queue内部有锁，性能不如deque
    # deque实际上是双向队列(可以从左边或右边入队/出队)，但是我们当做单向队列用
    q = collections.deque([root])
    result = []
    # 队列不为空时
    while q:
        current_level_values = []
        # 每次都要重新去队列长度
        for _ in range(len(q)):
            # pop是最右边的出队，用于标准队列FIFO
            node = q.popleft()
            current_level_values.append(node.val)
            # 将遍历当层二叉树节点的所有子树移到队尾，留给下一轮遍历(拓展成下一层的节点)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(current_level_values)
    return result


def level_order_dummy_head_queue(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    result = []
    curr_level = []
    q = collections.deque([root, None])
    # dummy_head的好处——少一层for循环，性能更好
    while q:
        node = q.popleft()
        if node is None:
            result.append(curr_level.copy())
            curr_level.clear()
            # DummyHead相当于该层结尾的分割线，又把分割线扔到最后了
            if q:
                q.append(None)
            continue
        curr_level.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result


# 自下而上的层级遍历，跟普通层级遍历一样，只是逆序插入insert(0)即可
def level_order_2_leaf_to_root(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    result = []
    curr_level = []
    q = collections.deque([root, None])
    while q:
        node = q.popleft()
        if node is None:
            result.insert(0, curr_level.copy())
            curr_level.clear()
            if q:
                q.append(None)
            continue
        curr_level.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("1(2)(3)", [[1], [2, 3]]),
        ("1()(2(3))", [[1], [2], [3]]),
    ]

    def test_level_order_dummy_head_queue(self):
        for binary_tree, expected in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            self.assertEqual(expected, level_order_dummy_head_queue(root))
