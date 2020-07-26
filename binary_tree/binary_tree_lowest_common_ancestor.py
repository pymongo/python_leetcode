from .binary_tree import TreeNode
import unittest
from typing import Optional


def lca_helper(root: TreeNode, a: TreeNode, b: TreeNode) -> Optional[TreeNode]:
    return lca(root, a, b)[0]


# 适合用二叉树分治法
def lca(root: TreeNode, a: TreeNode, b: TreeNode):
    if root is None:
        return None, False, False

    left_common_ancestor, left_is_ancestor_of_a, left_is_ancestor_of_b = lca(root.left, a, b)
    if left_is_ancestor_of_a and left_is_ancestor_of_b:
        return left_common_ancestor, True, True

    right_common_ancestor, right_is_ancestor_of_a, right_is_ancestor_of_b = lca(root.right, a, b)
    if right_is_ancestor_of_a and right_is_ancestor_of_b:
        return right_common_ancestor, True, True

    # 根据左右子树分治的结果，得到当前节点是不是a或b的祖先节点
    root_is_ancestor_of_a = left_is_ancestor_of_a or right_is_ancestor_of_a
    root_is_ancestor_of_b = left_is_ancestor_of_b or right_is_ancestor_of_b
    if root_is_ancestor_of_a and root_is_ancestor_of_b:
        return root, True, True
    if root.val == a.val:
        root_is_ancestor_of_a = True
    if root.val == b.val:
        root_is_ancestor_of_b = True
    return root, root_is_ancestor_of_a, root_is_ancestor_of_b
