import collections
import inspect
import math
import unittest
import os
# import pickle
from typing import List, Optional


def dbg(expression):
    for frame in inspect.stack():
        line = frame.code_context[0]
        if "dbg" in line:
            start = line.find('(') + 1
            end = line.rfind(')')
            if end == -1:
                end = len(line)
            print(f"[{os.path.basename(frame.filename)}:{frame.lineno}] {line[start:end]} = {expression!r}")
            break
    return expression


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __str__(self):
        """
        功能: 将二叉树打印成一个漂亮的「杨辉三角」
        实现思路: 将二叉树序列化为一维数组，数组第2-3项表示第二层，数组第3-6项表示第三层，以此类推
        level index     explain
        0     0         None
        1     [1,2]     [2**1-1, 2**2-2]
        2     [3,4,5,6] [2**2-1, 2**3-2]
        """
        # arr = pickle.loads(self.serialize())
        binary_tree_arr = self.to_list()
        # dbg(binary_tree_arr)
        size = len(binary_tree_arr)
        arr: List[str] = []
        for i in range(size):
            if binary_tree_arr[i] is None:
                arr.append('N')
            else:
                arr.append(str(binary_tree_arr[i]))
        # 例如[1,2,3,N,N,N,N]只有两层，但是长度+1取2的对数得到的是3
        log2_result = math.log2(size + 1)
        # level = 0
        if log2_result.is_integer():
            level = int(log2_result) - 1
        else:
            # 如果对数不能被整除，去掉尾巴的一对None
            # 例如: [3, 9, 20, None, None, 15, 7] 转为二叉树后再转为list，尾巴会多4个None
            new_len = size + 1 - 2
            while not math.log2(new_len).is_integer():
                new_len -= 2
            level = int(math.log2(new_len)) - 1
        output = " " * (level + 1) + arr[0] + '\n'
        for i in range(1, level + 1):
            padding_left = " " * (level - i)

            margin_between_num = ' ' * (2 * (level - i) + 1)
            curr_level_start_idx = 2 ** i - 1
            curr_level_end_idx = 2 ** (i + 1) - 2 + 1
            nums_str = margin_between_num.join(arr[curr_level_start_idx:curr_level_end_idx])

            output += (padding_left + nums_str + '\n')
        return output

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
        # print(binary_tree_arr)
        # return pickle.dumps(binary_tree_arr)
        return binary_tree_arr

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

    def test_serialize_deserialize(self):
        root = TreeNode.from_list([1, 2, 3, None, None, None, None])
        root_str = root.__str__()
        node = TreeNode.from_list(root.to_list())
        node_str = node.__str__()
        self.assertEqual(node_str, root_str)

    def test_serialize_deserialize_pre_order(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        node = deserialize_pre_order(serialize_pre_order_helper(root))
        self.assertEqual(root.__str__(), node.__str__())
