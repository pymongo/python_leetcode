import unittest
from .binary_tree import TreeNode
from typing import List


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
