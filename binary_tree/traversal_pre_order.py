from .binary_tree import TreeNode
import unittest
import collections
from typing import List, Optional


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
# 莫尼斯遍历不需要借助队列或栈的空间，与前序遍历不同的是莫里斯遍历每个节点只会访问一次
def pre_order_iterative(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    # 因为栈有FILO的特性，所以满足前序遍历的DFS要求
    stack = collections.deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        # 前序遍历能保证取出一个节点，该节点的值马上能写到result中，所以当前节点出栈读完值后，压入右节点和左节点就好，但是中序遍历就不同，遍历时val可能不会写入result，回溯时才会读val
        result.append(node.val)
        # 优化空间: 对None做判断避免None值入栈又出栈浪费效率
        stack.append(node.right)
        stack.append(node.left)
    return result


# 230. Kth Smallest Element in a BST
def bst_kth_smallest(root: TreeNode, k: int) -> int:
    stack = collections.deque()
    curr_node = root
    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = stack.pop()
        k -= 1
        if k == 0:
            return curr_node.val
        curr_node = curr_node.right


# 迭代版的前序和中序遍历用的不是一套模板
def in_order_iterative(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    # stack表示从根节点到当前节点的路径上的所有节点
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


# Reverse-Pre-Order' s output = reverse(Post-Order)
def post_order_iterative_1(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    stack = collections.deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        # "逆"前序遍历(根右左)再逆序等于后续遍历，每次将结果往前追加等于逆序
        result.insert(0, node.val)
        stack.append(node.left)
        stack.append(node.right)
    return result


# 正统的后续遍历思维的迭代法，基于中序遍历版本稍作修改
def post_order_iterative_2(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    stack = collections.deque()
    curr_node = root
    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            # 判断当前节点的左子树是否存在，若存在则持续往深处遍历左子树，若不存在就转向右子树
            if curr_node.left:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        # 走到这里时只可能是最底层且未记录的节点
        curr_node = stack.pop()
        result.append(curr_node.val)
        # 若栈不为空且当前节点是栈顶元素的左节点，说明已记录栈顶元素左节点的值
        if stack and stack[-1].left is curr_node:
            # 则转为遍历栈顶节点的右子树
            curr_node = stack[-1].right
        else:
            # 栈顶元素没有左子树和右子树，则curr_node设为None让栈顶元素出栈
            curr_node = None
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

    def test_post_order_iterative(self):
        for data in self.TEST_CASES:
            root = TreeNode.from_str(data['binary_tree'])
            self.assertEqual(data['post_order'], post_order_iterative_1(root))
            self.assertEqual(data['post_order'], post_order_iterative_2(root))
