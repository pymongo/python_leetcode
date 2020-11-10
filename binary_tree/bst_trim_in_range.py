import unittest
from .binary_tree import TreeNode
from typing import Optional


# 改定一个范围[lower,upper]，将BST超过范围的节点全都删掉
class Solution(unittest.TestCase):
    TEST_CASES = [
        ("1(0)(2)", 1, 2, "1()(2)"),
        # 返回的结果不一定是根节点，需要手动溯源，但是leetcode会自动找到根
        # ("3(0()(2(1)))(4)", 1, 2, "3(2(1))"),
    ]

    def test(self):
        for input_bst, lower, upper, output_bst in self.TEST_CASES:
            input_bst = TreeNode.from_str(input_bst)
            output = self.f(input_bst, lower, upper)
            self.assertEqual(output_bst, output.__str__())

    @staticmethod
    def f(root: TreeNode, lower: int, upper: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > upper:
            # 根结点的右子树的所有结点只会更大，说明根结点及其右子树都应该剪掉，因此直接返回左子树的修剪结果
            return Solution.f(root.left, lower, upper)
        if root.val < lower:
            return Solution.f(root.right, lower, upper)

        # 如果root.val满足条件，则检查左右子树
        # 如果根结点没问题，则递归地修剪左子结点和右子结点
        root.left = Solution.f(root.left, lower, upper)
        root.right = Solution.f(root.right, lower, upper)
        return root
