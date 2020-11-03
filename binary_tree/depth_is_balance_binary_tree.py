import unittest
from .binary_tree import TreeNode


def helper(root: TreeNode) -> bool:
    return divide_conquer(root)[0]


# > 二叉树分治法和前序遍历的区别
# 1. 分治法会有返回值，而且当前节点的返回值与其左子树的返回值和右子树的返回值有关
# 这题很适合用分治法，返回值是(是否平衡,深度)
# 而当前节点是否平衡与 左子树高度 和 右子树高度信息有关，所以用分治法效率比前序遍历要高
def divide_conquer(root: TreeNode) -> (bool, int):
    if root is None:
        # 空树也是平衡二叉树
        return True, 0
    left_subtree_is_balanced, left_subtree_height = divide_conquer(root.left)

    if not left_subtree_is_balanced:
        # 此时返回值中左子树的高度已经没有意义了，只要有一个False往上传染，最终返回值会是False
        return False, 0
    right_subtree_is_balanced, right_subtree_height = divide_conquer(root.right)

    if not right_subtree_is_balanced:
        return False, 0
    root_is_balanced = abs(left_subtree_height - right_subtree_height) <= 1

    if not root_is_balanced:
        return False, 0
    root_height = max(left_subtree_height, right_subtree_height) + 1
    return True, root_height


class Testing(unittest.TestCase):
    TESTCASES = [
        ("1(2)(3)", True),
        ("1()(2(3)(4))", False),
    ]

    def test_list_all_root_to_leaf_paths(self):
        for binary_tree, is_balanced in self.TESTCASES:
            root = TreeNode.from_str(binary_tree)
            self.assertEqual(is_balanced, helper(root))
