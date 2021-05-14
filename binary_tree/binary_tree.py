import collections
import inspect
import math
import unittest
import os
# import pickle
from typing import List, Optional, TypeVar

ExprType = TypeVar('ExprType')


def dbg(expression: ExprType) -> ExprType:
    for frame in inspect.stack():
        line = frame.code_context[0]
        if "dbg" in line:
            start = line.find('(') + 1
            end = line.rfind(')')
            if end == -1:
                end = len(line)
            # print(f"[{os.path.basename(frame.filename)}:{frame.lineno}] {line[start:end]} = {expression!r}")
            print(f"[:{frame.lineno}] {line[start:end]} = {expression!r}")
            break
    return expression


# 常见的序列化形式除了json/xml，还有Google/ProtoBuf,Facebook/Thrift,Alibaba/Dubbo，后面这三个除了序列化还有RPC
class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    # noinspection DuplicatedCode
    @staticmethod
    def from_str(s: str) -> Optional['TreeNode']:
        stack = collections.deque()
        val_len = 0
        is_left_subtree_empty = False
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                val_len += 1
                continue
            if val_len:
                node = TreeNode(int(s[i - val_len:i]))
                if stack:
                    stack_peek = stack[-1]
                    if is_left_subtree_empty:
                        stack_peek.right = node
                        is_left_subtree_empty = False
                    else:
                        if stack_peek.left is None:
                            stack_peek.left = node
                        else:
                            stack_peek.right = node
                stack.append(node)
                val_len = 0
            if s[i] == ')':
                if s[i - 1] == '(':
                    is_left_subtree_empty = True
                else:
                    stack.pop()
        return stack[0] if stack else None

    def __str__(self):
        s = ""
        if self is None:
            return s
        # visited + stack可以匹配括号
        visited = set()
        stack = collections.deque()
        stack.append(self)
        while stack:
            node = stack[-1]
            if node in visited:
                s += ')'
                stack.pop()
                continue
            s += f"({node.val}"
            if node.left is None and node.right:
                s += "()"
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            visited.add(node)
        if len(s) == 3:
            # 如果只有根节点一个，返回值要补上一对括号，否则读取字符串时会解析成None
            return s[1:-1] + "()"
        else:
            return s[1:-1] # 去掉头尾的括号

    def __repr__(self):
        return self.__str__()

    # noinspection DuplicatedCode
    # 为了方便单元测试，我就不序列化成二进制了
    # def serialize(self) -> bytes:
    def to_list(self) -> List[Optional[int]]:
        if self is None:
            return [None]
            # return pickle.dumps([None])
        queue = collections.deque()
        queue.append(self)
        binary_tree_arr: List[Optional[int]] = []
        while queue:
            node = queue.popleft()
            if node is None:
                binary_tree_arr.append(None)
                continue
            binary_tree_arr.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        # dbg(binary_tree_arr)
        # return pickle.dumps(binary_tree_arr)
        return binary_tree_arr

    def to_str(self) -> str:
        return self.__str__()

    # binary-tree-level-order-traversal: 112ms, 95.43%
    # serialize-and-deserialize-bfs:     76ms , 99.12%
    @staticmethod
    # def deserialize(data: bytes) -> Optional['TreeNode']:
    def from_list(data: List[Optional[int]]) -> Optional['TreeNode']:
        # arr: List[Optional[int]] = pickle.loads(data)
        arr = data
        if arr[0] is None:
            return None
        root: TreeNode = TreeNode(arr[0])
        # 队列存储的是还不清楚有没有左子树或右子树的节点
        queue = collections.deque()
        queue.append(root)

        size = len(arr)
        cursor: int = 1
        while cursor < size:
            # 考察node的左右子树
            node: TreeNode = queue.popleft()
            left_val = arr[cursor]
            right_val = arr[cursor + 1]
            # 不能用`if left_val:`，否则val是0的情况下这个分支不会被执行
            if left_val is not None:
                left_node = TreeNode(left_val)
                node.left = left_node
                # 尚不清楚left_node有没有子树
                queue.append(left_node)
            if right_val is not None:
                right_node = TreeNode(right_val)
                node.right = right_node
                queue.append(right_node)
            cursor += 2
        return root


# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/
def serialize_pre_order_helper(root: 'TreeNode') -> List[Optional[int]]:
    result = []
    serialize_pre_order(root, result)
    return result


# TODO 为了方便测试，就不序列化成bytes了
def serialize_pre_order(root: 'TreeNode', result: List[Optional[int]]):
    if root is None:
        result.append(None)
        return
    result.append(root.val)
    # 不要在递归中拼接字符串，字符串拼接耗时开辟额外空间后拼接耗时O(n)
    # 每层递归字符串拼接的时间复杂度之和是n+n-1+...+1=n**2
    serialize_pre_order(root.left, result)
    serialize_pre_order(root.right, result)


def deserialize_pre_order(arr: List[Optional[int]]) -> Optional[TreeNode]:
    # shift list first element
    node_val = arr.pop(0)
    if node_val is None:
        return None
    node = TreeNode(node_val)
    node.left = deserialize_pre_order(arr)
    node.right = deserialize_pre_order(arr)
    return node


class TestTreeNode(unittest.TestCase):
    def test_to_string(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        print(root)

    def test_tree_to_parentheses_str(self):
        s = "1(2(4)(5))(3)"
        node = TreeNode.from_str(s)
        print(node)
        self.assertEqual(s, TreeNode.from_str(s).to_str())

    def test_serialize_deserialize(self):
        root = TreeNode.from_list([1, 2, 3, None, None, None, None])
        node = TreeNode.from_list(root.to_list())
        self.assertEqual(node.to_str(), root.to_str())

    def test_serialize_root_has_not_left_subtree(self):
        root = TreeNode.from_str("1()(2(3)(4))")
        root_to_list = root.to_list()
        node = TreeNode.from_list(root_to_list)
        print(node)

    def test_serialize_deserialize_pre_order(self):
        root = TreeNode.from_str("3(9)(20(15)(7))")
        node = deserialize_pre_order(serialize_pre_order_helper(root))
        self.assertEqual(root.to_str(), node.to_str())

    def test_bug_str(self):
        """
           1
         N   2
        N N N 3
        FIXME 实际上3是2的左子树，__str__()方法错了，to_str()是对的
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        print(root)
        print(root.pretty())
