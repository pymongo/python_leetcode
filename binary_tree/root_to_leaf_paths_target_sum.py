"""
lintcode only, locked: https://lintcode.com/problem/binary-tree-path-sum/description?_from=ladder&&fromId=161
枚举所有方案: 二叉树的根到叶子节点所有路径元素之和等于target
这题很显然，与[Binary Tree Paths]一题用同一个模板
"""

import unittest
from .binary_tree import TreeNode


def helper(root: TreeNode, target: int):
    if root is None:
        return []
    # 保存当前DFS中已经访问了几个数字
    # 这题就不用deque了，加到答案集合上还要将deque转为List，耗费性能
    data = {
        "target": target,
        "stack": [],
        "sum_cache": 0,
        "results": []
    }
    list_all_root_to_leaf_paths(root, data)
    return data['results']


# 这题不建议用BFS或迭代法，因为还得在队列中额外存储每个节点的nums信息(从根节点到当前节点的数字)
def list_all_root_to_leaf_paths(root: TreeNode, data):
    if root is None:
        return
    data["stack"].append(root.val)
    data["sum_cache"] += root.val
    if root.left is None and root.right is None:
        if data["sum_cache"] == data["target"]:
            data["results"].append(data["stack"].copy())
    else:
        list_all_root_to_leaf_paths(root.left, data)
        list_all_root_to_leaf_paths(root.right, data)
    # 本节点已遍历完了，手动将本节点的值出栈
    data["stack"].pop()
    data["sum_cache"] -= root.val


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("1(2(2)(3))(4)", 5, [[1, 2, 2], [1, 4]]),
    ]

    def test_list_all_root_to_leaf_paths(self):
        for binary_tree, target, expected_paths in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            print(root)
            paths = helper(root, target)
            print(paths)
            self.assertEqual(expected_paths, paths)
