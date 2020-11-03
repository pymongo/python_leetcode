from .binary_tree import TreeNode
from typing import Optional
import unittest


# 请问一个有N个节点的二叉树，一共有几个subtree?
# 答案是N个(以某个节点为根，把它往下的所有节点囊括进去)
def subtree_max_sum(root: TreeNode) -> (int, int, Optional[TreeNode]):
    if root.left is None and root.right is None:
        return root.val, root.val, root
    elif root.left is not None and root.right is None:
        left_sum, left_max_sum, left_max_sum_node = subtree_max_sum(root.left)
        curr_sum = left_sum + root.val
        # 因为只有唯一解，不用考虑=0的情况
        if curr_sum > left_max_sum:
            return curr_sum, curr_sum, root
        else:
            return curr_sum, left_max_sum, left_max_sum_node
    elif root.right is not None and root.left is None:
        right_sum, right_max_sum, right_max_sum_node = subtree_max_sum(root.right)
        curr_sum = right_sum + root.val
        if curr_sum > right_max_sum:
            return curr_sum, curr_sum, root
        else:
            return curr_sum, right_max_sum, right_max_sum_node
    else:
        left_sum, left_max_sum, left_max_sum_node = subtree_max_sum(root.left)
        right_sum, right_max_sum, right_max_sum_node = subtree_max_sum(root.right)
        # 注意子树的和=当前节点的值+左子树和右子树所有节点的和
        curr_sum = root.val + left_sum + right_sum
        if curr_sum > left_sum and curr_sum > right_sum:
            return curr_sum, curr_sum, root
        if left_max_sum > right_max_sum:
            return curr_sum, left_max_sum, left_max_sum_node
        else:
            return curr_sum, right_max_sum, right_max_sum_node


def subtree_min_sum(root: TreeNode) -> (int, int, Optional[TreeNode]):
    if root.left is None and root.right is None:
        return root.val, root.val, root
    elif root.left is not None and root.right is None:
        left_sum, left_min_sum, left_min_sum_node = subtree_min_sum(root.left)
        curr_sum = left_sum + root.val
        # 因为只有唯一解，不用考虑=0的情况
        if curr_sum < left_min_sum:
            return curr_sum, curr_sum, root
        else:
            return curr_sum, left_min_sum, left_min_sum_node
    elif root.right is not None and root.left is None:
        right_sum, right_min_sum, right_min_sum_node = subtree_min_sum(root.right)
        curr_sum = right_sum + root.val
        if curr_sum < right_min_sum:
            return curr_sum, curr_sum, root
        else:
            return curr_sum, right_min_sum, right_min_sum_node
    else:
        left_sum, left_min_sum, left_min_sum_node = subtree_min_sum(root.left)
        right_sum, right_min_sum, right_min_sum_node = subtree_min_sum(root.right)
        # 注意子树的和=当前节点的值+左子树和右子树所有节点的和
        curr_sum = root.val + left_sum + right_sum
        if curr_sum < left_sum and curr_sum < right_sum:
            return curr_sum, curr_sum, root
        if left_min_sum < right_min_sum:
            return curr_sum, left_min_sum, left_min_sum_node
        else:
            return curr_sum, right_min_sum, right_min_sum_node


class Testing(unittest.TestCase):
    TESTCASES = [
        ("1(-5(0)(3))(2(-4)(-5))", TreeNode(3))
    ]

    def test_subtree_max_sum(self):
        for binary_tree, expected in self.TESTCASES:
            root = TreeNode.from_str(binary_tree)
            subtree_node = subtree_max_sum(root)[2]
            self.assertEqual(expected.to_str(), subtree_node.to_str())

    def test_subtree_min_sum(self):
        binary_tree = TreeNode.from_str("1(-5(1)(2))(2(-4)(-5))")
        self.assertEqual(binary_tree.to_str(), subtree_min_sum(binary_tree)[2].to_str())
