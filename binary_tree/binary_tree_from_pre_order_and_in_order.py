"""
二叉树特性之: TODO 前序/后序+中序序列可以唯一确定一棵二叉树
注意: 你可以假设二叉树中没有重复的元素
"""
import unittest
from .binary_tree import TreeNode
from typing import List, Dict, Optional


def copy_stack_solution(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    root = TreeNode(preorder[0])
    # 维护「当前节点的所有还没有考虑过右儿子的祖先节点」
    stack = [root]
    inorder_idx = 0
    for i in range(1, len(preorder)):
        preorder_val = preorder[i]
        node = stack[-1]
    return None


# 自强，自己推敲递归解法
def my_solution_helper(pre_order: List[int], in_order: List[int]) -> TreeNode:
    # HashMap加速查找pre_order中的根节点在in_order的索引位置
    in_order_map: Dict[int, int] = {}
    in_order_len = 0
    for i, val in enumerate(in_order):
        in_order_map[val] = i
        in_order_len += 1
    return my_solution(
        pre_order=pre_order,
        pre_order_start=0,
        # in_order和pre_order长度相同
        pre_order_end=in_order_len - 1,
        in_order=in_order,
        in_order_start=0,
        in_order_end=in_order_len - 1,
        in_order_map=in_order_map
    )


def my_solution(
    pre_order: List[int],
    pre_order_start: int,
    pre_order_end: int,
    in_order: List[int],
    in_order_start: int,
    in_order_end: int,
    in_order_map: Dict[int, int]
) -> Optional[TreeNode]:
    # 递归结束条件
    if pre_order_start > pre_order_end or in_order_start > in_order_end:
        return None
    # 找到根节点在in_order_map中的索引`in_order_root_index`
    # 以便将in_order、pre_order数组划分为:
    # in_order_左子树:  [in_order_start, in_order_root_index)
    # in_order_右子树:  [in_order_root_index+1, in_order_end]
    # pre_order_左子树: [pre_order_start+1, pre_order_start+1+len(in_order_左子树)-1]
    # pre_order_右子树: ...
    root_val = pre_order[pre_order_start]

    in_order_root = in_order_map[root_val]
    left_subtree_size = in_order_root - in_order_start

    root = TreeNode(root_val)
    root.left = my_solution(
        pre_order=pre_order,
        pre_order_start=pre_order_start + 1,
        pre_order_end=pre_order_start + left_subtree_size,
        in_order=in_order,
        in_order_start=in_order_start,
        in_order_end=in_order_root - 1,
        in_order_map=in_order_map
    )
    root.right = my_solution(
        pre_order=pre_order,
        pre_order_start=pre_order_start + left_subtree_size + 1,
        pre_order_end=pre_order_end,
        in_order=in_order,
        in_order_start=in_order_root + 1,
        in_order_end=in_order_end,
        in_order_map=in_order_map
    )
    return root


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7, None, None, None, None])
    ]

    def test_my_solution(self):
        for pre_order, in_order, binary_tree_list in self.TEST_CASES:
            root = my_solution_helper(pre_order, in_order)
            self.assertEqual(binary_tree_list, root.to_list())
