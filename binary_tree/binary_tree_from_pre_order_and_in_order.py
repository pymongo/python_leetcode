"""
二叉树特性之: TODO 前序/后序+中序序列可以唯一确定一棵二叉树
注意: 你可以假设二叉树中没有重复的元素
"""
import unittest
from .binary_tree import TreeNode
from typing import List, Optional

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
    pass

def my_solution(pre_order: List[int], in_order: List[int]):
    pass

class Testing(unittest.TestCase):
    TEST_CASES = [
        ()
    ]
    def test_my_solution(self):
        pass