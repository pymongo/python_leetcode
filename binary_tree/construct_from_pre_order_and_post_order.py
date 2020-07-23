import unittest
from .binary_tree import TreeNode, dbg
from typing import List, Dict, Optional


# 这题遇到小困难，两个数组都知道自己的根节点，但是怎么确定各自划分左右子树的分隔线呢？
# 规律: 后序遍历倒数第二个是右子树的根，也就是pre_order(根左右)的右子树的开始位置
def my_dfs_helper(pre_order: List[int], post_order: List[int]) -> TreeNode:
    # HashMap加速查找pre_order中的根节点在in_order的索引位置
    pre_order_map: Dict[int, int] = {}
    pre_order_len = 0
    for i, val in enumerate(pre_order):
        pre_order_map[val] = i
        pre_order_len += 1
    return my_dfs(
        pre_order=pre_order,
        pre_order_start=0,
        pre_order_end=pre_order_len - 1,
        pre_order_map=pre_order_map,
        post_order=post_order,
        post_order_start=0,
        post_order_end=pre_order_len - 1
    )


def my_dfs(
    pre_order: List[int],
    pre_order_start: int,
    pre_order_end: int,
    pre_order_map: Dict[int, int],
    post_order: List[int],
    post_order_start: int,
    post_order_end: int,
) -> Optional[TreeNode]:
    # dbg((pre_order_start, pre_order_end))
    # dbg((post_order_start, post_order_end))
    # 递归结束条件: 无法在范围内找到pre_order右子树的根元素
    # 也就是这句代码`right_subtree_root_val = post_order[pre_order_end-1]`会越界
    # 实际刷题时要灵活推敲出递归结束条件
    if pre_order_start > pre_order_end - 1:
        return None

    # 规律: 后序遍历倒数第二个是右子树的根，也就是pre_order(根左右)的右子树的开始位置
    right_subtree_root_val = post_order[pre_order_end - 1]
    pre_order_right_subtree_root = pre_order_map[right_subtree_root_val]
    right_subtree_size = pre_order_end - pre_order_right_subtree_root + 1
    # dbg(right_subtree_size)

    root = TreeNode(pre_order[pre_order_start])
    # 后序和中序的左子树索引范围一致
    # print("left subtree")
    root.left = my_dfs(
        pre_order=pre_order,
        pre_order_start=pre_order_start + 1,  # OK(100%)
        pre_order_end=pre_order_end - right_subtree_size,  # OK
        pre_order_map=pre_order_map,
        post_order=post_order,
        post_order_start=post_order_start,  # OK(100%)
        post_order_end=post_order_end - right_subtree_size - 1
    )
    # print("right subtree")
    root.right = my_dfs(
        pre_order=pre_order,
        pre_order_start=pre_order_end - right_subtree_size + 1,
        pre_order_end=pre_order_end,  # OK(100%)
        pre_order_map=pre_order_map,
        post_order=post_order,
        post_order_start=post_order_end - right_subtree_size,
        post_order_end=post_order_end - 1  # OK(100%)
    )
    return root


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3], [3], [3]),
        ([3, 9, 20, 15, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7, None, None, None, None]),
        ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], [1, 2, 3, 4, 5, 6, 7]),
    ]

    def test_my_solution(self):
        for pre_order, post_order, binary_tree_list in self.TEST_CASES:
            root = my_dfs_helper(pre_order, post_order)
            self.assertEqual(binary_tree_list, root.to_list())
