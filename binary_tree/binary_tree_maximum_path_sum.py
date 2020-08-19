import unittest
from .binary_tree import TreeNode


class Solution(unittest.TestCase):
    def test(self):
        test_cases = [
            ("1(2)(3)", 6),
        ]
        for tree, max_path_sum in test_cases:
            self.assertEqual(max_path_sum, self.maxPathSum(TreeNode.from_str(tree)))

    @staticmethod
    def maxPathSum(root: TreeNode) -> int:
        max_path = float('-inf')

        # 后序遍历寻找路径
        def find_max(node: TreeNode) -> int:
            nonlocal max_path
            if node is None:
                return 0
            # 只有当左右子树贡献值大于0时才会被选中
            left = max(find_max(node.left), 0)
            right = max(find_max(node.right), 0)
            # 先判断当前左-中-右路径是不是最长的
            max_path = max(max_path, left + node.val + right)
            # 由于往上的路径只能是从左往上或从右往上，所以选一个最大的
            return node.val + max(left, right)

        find_max(root)
        return max_path
