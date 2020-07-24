from .binary_tree import TreeNode
import unittest
import collections
from typing import List


def pre_order_recursive_helper(root: TreeNode) -> List[int]:
    result = []
    pre_order_recursive(root, result)
    return result


def pre_order_recursive(root: TreeNode, result: List[int]):
    if root is None:
        return
    # pre-order、in-order、post-order的唯一区别就是改变下面三行的顺序
    result.append(root.val)
    pre_order_recursive(root.left, result)
    pre_order_recursive(root.right, result)


def pre_order_iterative(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    # 因为栈有FILO的特性，所以满足先序遍历的DFS要求
    stack = collections.deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        # pre-order、in-order、post-order的唯一区别就是改变下面三行的顺序
        result.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        {'binary_tree': "1()(2(3))", 'pre_order': [1, 2, 3], 'in_order': [1, 3, 2], 'post_order': [3, 2, 1]}
    ]

    def test_pre_order_iterative(self):
        for data in self.TEST_CASES:
            root = TreeNode.from_str(data['binary_tree'])
            pre_order = pre_order_iterative(root)
            self.assertEqual(data['pre_order'], pre_order)
