import unittest
from .binary_tree import TreeNode
import collections


# > 二叉树分治法和前序遍历的区别
# 1. 分治法每个节点只会遍历一次
# 2. 前序遍历的区别是这是自下而上的解法，而前序遍历更像自顶而下的解法，需要一个全局变量记录最小深度
def min_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    elif root.left is None and root.right is not None:
        return min_depth(root.right) + 1
    elif root.left is not None and root.right is None:
        return min_depth(root.left) + 1
    else:
        # 求最大深度的话将下面的min换成max就行了
        return min(min_depth(root.left), min_depth(root.right)) + 1


# 二叉树最小深度用BFS最优，找到第一个叶子节点就等于最小深度
def min_depth_bfs(root: TreeNode) -> int:
    if root is None:
        return 0
    queue = collections.deque([root, None])
    current_depth = 1
    while queue:
        node = queue.popleft()
        # 如果已经遍历完一层
        if node is None:
            current_depth += 1
            if queue:
                queue.append(None)
            continue
        if node.left is None and node.right is None:
            return current_depth
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    raise Exception("Unreachable!")


class Testing(unittest.TestCase):
    TESTCASES = [
        {'binary_tree': "1(2)(3(4)(5))", 'min_depth': 2, 'max_depth': 3},
        {'binary_tree': "1()(2(3))", 'min_depth': 3, 'max_depth': 3},
    ]

    def test_min_depth(self):
        for data in self.TESTCASES:
            root = TreeNode.from_str(data['binary_tree'])
            self.assertEqual(data['min_depth'], min_depth(root))
            self.assertEqual(data['min_depth'], min_depth_bfs(root))
