from .binary_tree import TreeNode
import unittest
from typing import Optional


# 与二叉树公共祖先分治法中自下而上的递归不同，这是自顶向下的递归(二分法)
def bst_lca_recursive(root: TreeNode, a: TreeNode, b: TreeNode) -> TreeNode:
    # BST的最近公共祖先一定是node.val在a.val和b.val之间
    if root.val > a.val and root.val > b.val:
        # a和b在root的左子树，每次都能排除掉"一半"，只有当bst是满二叉树/平衡二叉树时，才能达到二分法的时间复杂度
        return bst_lca_recursive(root.left, a, b)
    if root.val < a.val and root.val < b.val:
        return bst_lca_recursive(root.right, a, b)
    return root


def bst_lca_iterative(root: TreeNode, a: TreeNode, b: TreeNode) -> TreeNode:
    while root:
        # 这个if..elif..else是不是跟二分法很像?
        if root.val > a.val and root.val > b.val:
            root = root.left
        elif root.val < a.val and root.val < b.val:
            root = root.right
        else:
            return root


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("4(3)(5)", 3, 5, 4)
    ]

    def test_lca(self):
        for binary_tree, a, b, common_ancestor in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            self.assertEqual(common_ancestor, bst_lca_iterative(root, TreeNode(a), TreeNode(b)).val)
