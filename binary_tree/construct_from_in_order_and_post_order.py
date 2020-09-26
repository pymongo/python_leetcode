import unittest
from .binary_tree import TreeNode
from typing import List, Dict, Optional


class Solution(unittest.TestCase):
    @staticmethod
    def build_tree(in_order: List[int], post_order: List[int]) -> TreeNode:
        # HashMap加速查找pre_order中的根节点在in_order的索引位置
        in_order_map: Dict[int, int] = {}
        in_order_len = 0
        for i, val in enumerate(in_order):
            in_order_map[val] = i
            in_order_len += 1

        def dfs(post_order_start: int, post_order_end: int, in_order_start: int, in_order_end) -> Optional[TreeNode]:
            # 递归结束条件
            if post_order_start > post_order_end:
                return None

            root_val = post_order[post_order_end]
            in_order_root = in_order_map[root_val]
            left_subtree_size = in_order_root - in_order_start

            root = TreeNode(root_val)
            # 后序和中序的左子树索引范围一致
            root.left = dfs(
                post_order_start=post_order_start,
                post_order_end=post_order_start + left_subtree_size - 1,
                in_order_start=in_order_start,
                in_order_end=in_order_root - 1,
            )
            root.right = dfs(
                post_order_start=post_order_start + left_subtree_size,
                # 右子树的右边界就是剔除后序遍历的最后一个(根)
                post_order_end=post_order_end - 1,
                in_order_start=in_order_root + 1,
                in_order_end=in_order_end,
            )
            return root

        return dfs(
            post_order_start=0,
            post_order_end=in_order_len - 1,
            in_order_start=0,
            in_order_end=in_order_len - 1,
        )

    TEST_CASES = [
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], "3(9)(20(15)(7))")
    ]

    def test_build_tree(self):
        for in_order, post_order, binary_tree in self.TEST_CASES:
            root = self.build_tree(in_order, post_order)
            self.assertEqual(binary_tree, root.to_str())
