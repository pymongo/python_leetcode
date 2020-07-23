"""
二叉树特性之: TODO 前序/后序/中序知道其中2个可以唯一确定一棵二叉树
3选2必有先序或后序，所以可以知道根是什么
注意: 你可以假设二叉树中没有重复的元素
"""
import unittest
import collections
from .binary_tree import TreeNode
from typing import List, Dict, Optional


# pre_order遍历中，pre_order[i]和pre_order[i-1]的关系只可能是:
# 1. i是i-1的左儿子
# 2. i-1没有左儿子
# 2.1 i-1有右儿子，那么接下来遍历的i就是i-1的右儿子
# 2.2 i-1没有右儿子，i是i-1的某个祖先的右儿子(而且i-1不在这个祖先的右子树中)
def copy_stack_solution(pre_order: List[int], in_order: List[int]) -> Optional[TreeNode]:
    root = TreeNode(pre_order[0])
    # 维护「当前节点的所有还没有考虑过右儿子的祖先节点」
    stack = [root]
    in_order_idx = 0
    for i in range(1, len(pre_order)):
        pre_order_val = pre_order[i]
        node = stack[-1]
        if node.val != in_order[in_order_idx]:
            # 1. i是i-1的左儿子
            node.left = TreeNode(pre_order_val)
            stack.append(node.left)
        else:
            while stack and stack[-1].val == in_order[in_order_idx]:
                node = stack.pop()
                in_order_idx += 1
            node.right = TreeNode(pre_order_val)
            stack.append(node.right)
    return root


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
    # 递归结束条件等于`in_order_map[root_val]`中无法找到根元素的索引的下标范围
    if pre_order_start > pre_order_end:
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

# 44 ms 击败了98.77%的用户，再次证明pop()和append()操作deque的性能优于list
def recipe_stack(pre_order: List[int], in_order: List[int]) -> Optional[TreeNode]:
    if not pre_order:
        return None
    root = TreeNode(pre_order[0])
    in_order_idx = 0
    stack = collections.deque()
    stack.append(root)
    # Round: 1
    # pre: [3,  9, 20, 15, 7]
    #           ^
    # in:  [20, 9, 15,  3, 7]
    #        ^
    for i in range(1, len(pre_order)):
        node = stack[-1]
        if node.val == in_order[in_order_idx]:
            # pre_order[i]是pre_order[i-1]的右子树
            while stack and stack[-1].val == in_order[in_order_idx]:
                node = stack.pop()
                in_order_idx += 1
            node.right = TreeNode(pre_order[i])
            stack.append(node.right)
        else:
            # pre_order[i]是pre_order[i-1]的左子树
            node.left = TreeNode(pre_order[i])
            stack.append(node.left)
    return root


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7, None, None, None, None])
    ]

    def test_my_solution(self):
        for pre_order, in_order, binary_tree_list in self.TEST_CASES:
            root = my_solution_helper(pre_order, in_order)
            self.assertEqual(binary_tree_list, root.to_list())

    def test_stack(self):
        for pre_order, in_order, binary_tree_list in self.TEST_CASES:
            root = recipe_stack(pre_order, in_order)
            self.assertEqual(binary_tree_list, root.to_list())
