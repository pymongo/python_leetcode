import unittest
from .binary_tree import TreeNode
import collections
from typing import List


def helper(root: TreeNode):
    paths: List[str] = []
    if root is None:
        return paths
    # 保存当前DFS中已经访问了几个数字，
    stack = collections.deque()
    list_all_root_to_leaf_paths(root, stack, paths)
    return paths


def list_all_root_to_leaf_paths(root: TreeNode, stack, paths: List[str]):
    if root is None:
        return
    stack.append(root.val)
    if root.left is None and root.right is None:
        # 没有左子树和右子树的节点才叫叶子节点
        # 需要将当前栈的所有元素加到解答集
        paths.append('->'.join(iter(map(lambda x: str(x), stack))))
    else:
        list_all_root_to_leaf_paths(root.left, stack, paths)
        list_all_root_to_leaf_paths(root.right, stack, paths)
    # 需要手动pop还原状态的才叫「回溯」
    # 本节点已遍历完了，要将本节点的值出栈
    stack.pop()


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3, None, 5, None, None], ["1->2->5", "1->3"]),
    ]

    def test_list_all_root_to_leaf_paths(self):
        for binary_tree, paths in self.TEST_CASES:
            root = TreeNode.from_list(binary_tree)
            print(root)
            paths = helper(root)
            print(paths)
