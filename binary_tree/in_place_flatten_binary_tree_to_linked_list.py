"""
用left=None, right=next的二叉树节点来模拟链表，将一个二叉树In-Place地转为pre-order的链表
    1
   / \
  2   5
 / \   \
3   4   6
(pre-order): The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
from .binary_tree import TreeNode
import unittest
import collections


# 这题递归用pre-order容易丢失节点信息，只能用右左根的顺序+previous_node指针，previous_node.right = curr_node这样
def bfs(root: TreeNode) -> None:
    """
    1. 切开root.right
    2. 将root.left拼到root.right
    3. 将步骤1切开的root.right拼到root.right(也就是步骤2的左子树)的最右子树(most_right)末尾
    上述1.2.3过程实际上都不需要用到栈或堆
    """
    while root is not None:
        # 可以优化的空间: temp变量其实可以不要
        # 1. 切开root.right
        temp = root.right
        # 2. 将root.left拼到root.right
        root.right = root.left
        root.left = None
        # 3. 将步骤1切开的root.right拼到root.right(也就是步骤2的左子树)的最右子树(most_right)末尾
        # 注意将right_most设为root能规避右边是None的问题
        right_most = root
        while right_most.right:
            right_most = right_most.right
        right_most.right = temp
        root = root.right


# 算法和 94 题中序遍历的 Morris 算法有些神似
# 不用临时变量temp保存被剪掉的root.right，而是先将root.right拼到root.left，再更新root.right和root.left
def other_bfs(root: TreeNode) -> None:
    """
    1. 找到root.left的right_most
    2. 将root.right复制拼接到root.left的right_most
    3. root.right, root.left = root.left, None
    """
    while root:
        if root.left is None:
            root = root.right
            continue
        right_most = root.left
        while right_most.right:
            right_most = right_most.right
        right_most.right = root.right
        root.right, root.left = root.left, None
        root = root.right


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("1(2(3)(4))(5()(6))", "1()(2()(3()(4()(5()(6)))))")
    ]

    def test_bfs(self):
        for binary_tree, expected in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            bfs(root)
            self.assertEqual(expected, root.to_str())
