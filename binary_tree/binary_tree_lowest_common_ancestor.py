from .binary_tree import TreeNode
import unittest
from typing import Optional


def lca_helper(root: TreeNode, a: TreeNode, b: TreeNode) -> Optional[TreeNode]:
    return lca(root, a, b)[0]


# 适合用二叉树分治法, 非递归解法用两个Hash存储p和q的祖先，如果出现重复则为最近公共祖先，迭代写法面试官都不一定能看得懂
def lca(root: TreeNode, a: TreeNode, b: TreeNode) -> (bool, bool, Optional[TreeNode]):
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


class LCA2:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        # 每个节点除了左右儿子指针以外，还包含一个父亲指针parent，指向自己的父亲
        self.parent = None


def lca2(root: LCA2, a: LCA2, b: LCA2):
    a_parents = set()
    a_curr_parent = a
    while a_curr_parent is not None:
        a_parents.add(a_curr_parent)
        a_curr_parent = a_curr_parent.parent
    b_curr_parent = b
    while b_curr_parent is not None:
        if b_curr_parent in a_parents:
            return b_curr_parent
        b_curr_parent = b_curr_parent.parent
    return None


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("4(3)(7(5)(6))", 3, 5, 4)
    ]

    def test_lca(self):
        for binary_tree, a, b, common_ancestor in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            self.assertEqual(common_ancestor, lca_helper(root, TreeNode(a), TreeNode(b)).val)
