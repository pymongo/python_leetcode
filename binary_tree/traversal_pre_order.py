from .binary_tree import TreeNode
import unittest
import collections
from typing import List


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


# 230. Kth Smallest Element in a BST
def bst_kth_smallest(root: TreeNode, k: int) -> int:
    """
    TODO 优化方法
    用一个HashMap<TreeNode, Integer>记录每个节点的子树的节点个数
    利用快速选择的算法，确定第k小的数在哪一个子树中，时间复杂度为O(h)
    例如求k=20小的元素，root.left有15个，root算一个，那么等同于求root.right中第4小的元素
    """
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


def post_order_iterative_3(root: TreeNode) -> List[int]:
    """
    1、如果根节点非空，将根节点加入到栈中。
    2、如果栈不空，取栈顶元素（暂时不弹出），
      a.如果（左子树已访问过或者左子树为空），且（右子树已访问过或右子树为空），则弹出栈顶节点，将其值加入数组，
      b.如果左子树不为空，且未访问过，则将左子节点加入栈中，并标左子树已访问过。
      c.如果右子树不为空，且未访问过，则将右子节点加入栈中，并标右子树已访问过。
    3、重复第二步，直到栈空。
    """
    result = []
    stack = []
    prev, curr = None, root

    if not root:
        return result

    # 通过维护curr前继节点的后序遍历
    stack.append(root)
    while len(stack) > 0:
        curr = stack[-1]
        if not prev or prev.left == curr or prev.right == curr:
            # traverse down the tree
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
        elif curr.left == prev:
            # traverse up the tree from the left
            if curr.right:
                stack.append(curr.right)
        else:
            # traverse up the tree from the right
            result.append(curr.val)
            stack.pop()
        prev = curr

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
