import unittest
from .binary_tree import TreeNode


# 二分法
def bst_closest_1(root: TreeNode, target: float) -> int:
    # 上边界
    upper = root
    # 下边界
    lower = root
    while root:
        if root.val > target:
            upper = root
            root = root.left
        elif root.val < target:
            lower = root
            root = root.right
        else:
            return root.val
    if abs(upper.val - target) > abs(lower.val - target):
        return lower.val
    else:
        return upper.val


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([5, 4, 9, 2, None, 8, 10], 6.124780, 5),
        ([3, 2, 4, 1, None, None, None], 4.142857, 4),
    ]

    def test_bst_closest_1(self):
        for binary_tree, target, expected in self.TEST_CASES:
            root = TreeNode.from_list(binary_tree)
            print(root)
            self.assertEqual(expected, bst_closest_1(root, target))
