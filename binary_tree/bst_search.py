from .binary_tree import TreeNode
from typing import Optional, List


class Solution:
    @staticmethod
    def search_target_recursive(root: TreeNode, target: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > target:
            return Solution.search_target_recursive(root.left, target)
        elif root.val < target:
            return Solution.search_target_recursive(root.right, target)
        else:
            return root

    @staticmethod
    def search_target_iterative(root: TreeNode, target: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val > target:
                curr = curr.left
            elif curr.val < target:
                curr = curr.right
            else:
                break
        return curr

    @staticmethod
    def search_node_val_in_range(root: TreeNode, lower: int, upper: int) -> List[int]:
        if root is None:
            return []

        res = []

        # 其实这题就等同于中序遍历一次，然后满足条件的加到返回值里
        def search_in_order(node: TreeNode):
            if node.left:
                # 题目要求搜索结果按小到大排序(中序遍历)，所以优先搜索左子树
                search_in_order(node.left)
            if lower <= node.val <= upper:
                res.append(node.val)
            if node.right:
                search_in_order(node.right)

        search_in_order(root)
        return res
