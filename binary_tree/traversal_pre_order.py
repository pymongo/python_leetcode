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


# 栈遍历的升级版是: 「莫里斯遍历+线索二叉树」
# 莫尼斯遍历不需要借助队列或栈的空间，与先序遍历不同的是莫里斯遍历每个节点只会访问一次
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
        # 前序遍历能保证取出一个节点，该节点的值马上能写到result中，所以当前节点出栈读完值后，压入右节点和左节点就好，但是中序遍历就不同，遍历时val可能不会写入result，回溯时才会读val
        result.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return result


# 迭代版的前序和中序遍历用的不是一套模板
def in_order_iterative(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    stack = collections.deque()
    curr_node = root
    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = stack.pop()
        result.append(curr_node.val)
        curr_node = curr_node.right
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        {'binary_tree': "1()(2(3))", 'pre_order': [1, 2, 3], 'in_order': [1, 3, 2], 'post_order': [3, 2, 1]},
        {'binary_tree': "3(9)(20(15)(7))",
         'pre_order': [3, 9, 20, 15, 7],
         'in_order': [9, 3, 15, 20, 7],
         'post_order': [9, 15, 7, 20, 3]},
    ]

    def test_pre_order_iterative(self):
        for data in self.TEST_CASES:
            root = TreeNode.from_str(data['binary_tree'])
            pre_order = pre_order_iterative(root)
            self.assertEqual(data['pre_order'], pre_order)

    def test_in_order_iterative(self):
        for data in self.TEST_CASES:
            root = TreeNode.from_str(data['binary_tree'])
            pre_order = in_order_iterative(root)
            self.assertEqual(data['in_order'], pre_order)
