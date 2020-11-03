import unittest
from .binary_tree import TreeNode


# 这题不建议用BFS或迭代法，因为还得在队列中额外存储每个节点的nums信息(从根节点到当前节点的数字)
class Solution(unittest.TestCase):
    TESTCASES = [
        ("1(2()(5))(3)", ["1->2->5", "1->3"]),
    ]

    def test_list_all_root_to_leaf_paths(self):
        for binary_tree, expected_paths in self.TESTCASES:
            root = TreeNode.from_str(binary_tree)
            print(root)
            paths = self.binary_tree_paths(root)
            print(paths)
            self.assertListEqual(expected_paths, paths)

    @staticmethod
    def binary_tree_paths(root):
        res = []
        # 保存当前DFS中已经访问的节点
        curr_path = []

        def list_all_root_to_leaf_paths(node: TreeNode):
            if node is None:
                return
            curr_path.append(node.val)
            if node.left is None and node.right is None:
                # 没有左子树和右子树的节点才叫叶子节点
                # 需要将当前栈的所有元素加到解答集
                res.append('->'.join(iter(map(lambda x: str(x), curr_path))))
            else:
                list_all_root_to_leaf_paths(node.left)
                list_all_root_to_leaf_paths(node.right)
            # 需要手动pop还原状态的才叫「回溯」
            # 本节点已遍历完了，要将本节点的值出栈
            curr_path.pop()

        list_all_root_to_leaf_paths(root)
        return res
