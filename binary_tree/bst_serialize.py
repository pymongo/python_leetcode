"""
根据bst的左<跟<右特性可知: bst的中序遍历必为有序数组
所以本题的反序列化过程可以转为将前序遍历和排序后的前序遍历也就是中序遍历转为二叉树，既leetcode#105
"""
from .binary_tree import TreeNode
import unittest
import bisect
import collections
from typing import Dict, List, Optional


def pre_order_traversal(root: TreeNode, result: Dict[str, List[Optional[int]]]):
    if root is None:
        return
    result['pre_order'].append(root.val)
    bisect.insort(result['in_order'], root.val)

    pre_order_traversal(root.left, result)
    pre_order_traversal(root.right, result)


def pre_order_serialize(root: TreeNode) -> Dict[str, List[Optional[int]]]:
    result = {'pre_order': [], 'in_order': []}
    if root is None:
        result['pre_order'].append(None)
        result['in_order'].append(None)
        return result
    pre_order_traversal(root, result)
    # print(result)
    return result


def construct_bst(data: Dict[str, List[Optional[int]]]) -> Optional[TreeNode]:
    root_val = data['pre_order'][0]
    if root_val is None:
        return None
    root = TreeNode(root_val)
    stack = collections.deque()
    stack.append(root)
    in_order_idx = 0
    for i in range(1, len(data['pre_order'])):
        node = stack[-1]
        if node.val == data['in_order'][in_order_idx]:
            while stack and stack[-1].val == data['in_order'][in_order_idx]:
                node = stack.pop()
                in_order_idx += 1
            node.right = TreeNode(data['pre_order'][i])
            stack.append(node.right)
        else:
            node.left = TreeNode(data['pre_order'][i])
            stack.append(node.left)
    return root


class Testing(unittest.TestCase):
    def test(self):
        root = TreeNode.from_str("2(1)(3(2)(4))")
        data = pre_order_serialize(root)
        new_node = construct_bst(data)
        print(new_node)
