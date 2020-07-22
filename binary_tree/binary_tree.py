import unittest
import collections
import pickle
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __str__(self):
        """
        如果将二叉树漂亮地打印为"满"二叉树，没有
        """
        queue = collections.deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            if node is None:
                if queue:
                    queue.append(None)
                continue
        pass

    # noinspection DuplicatedCode
    def serialize(self) -> bytes:
        if self is None:
            return pickle.dumps([None])
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
        return pickle.dumps(binary_tree_arr)

    # noinspection DuplicatedCode
    @staticmethod
    def static_serialize(root: 'TreeNode') -> bytes:
        """
        想法: 将二叉树序列化为"满"二叉树的一维数组，数组第2-3项表示第二层，以此类推
        level index     explain
        0     0         None
        1     [1,2]     [2**1-1, 2**2-2]
        2     [3,4,5,6] [2**2-1, 2**3-2]
        """
        if root is None:
            return pickle.dumps([None])
        queue = collections.deque()
        queue.append(root)
        binary_tree_arr: List[Optional[int]] = []
        while queue:
            node = queue.popleft()
            if node is None:
                binary_tree_arr.append(None)
                continue
            binary_tree_arr.append(node.val)
            # 图: https://pic.leetcode-cn.com/f93235b0b74fbc481451954ea50a65fab347c602dd55ccb1df36ceed929136d5-image.png
            # 最后的叶子节点也会往下扩展成两个None才会结束
            queue.append(node.left)
            queue.append(node.right)
        return pickle.dumps(binary_tree_arr)

    @staticmethod
    def deserialize(data: bytes) -> Optional['TreeNode']:
        arr: List[Optional[int]] = pickle.loads(data)
        if arr[0] is None:
            return None
        root: TreeNode = TreeNode(arr[0])
        # 队列存储的是还不清楚有没有左子树或右子树的节点
        queue = collections.deque()
        queue.append(root)

        cursor: int = 1
        size = len(arr)
        while cursor < size:
            # 考察node的左右子树
            node: TreeNode = queue.popleft()
            left_val = arr[cursor]
            right_val = arr[cursor + 1]
            if left_val:
                left_node = TreeNode(left_val)
                node.left = left_node
                # 尚不清楚left_node有没有子树
                queue.append(left_node)
            if right_val:
                right_node = TreeNode(right_val)
                node.right = right_node
                # 尚不清楚right_node有没有子树
                queue.append(right_node)
            cursor += 2
        return root


class TestTreeNode(unittest.TestCase):
    def test_to_string(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        a: bytes = TreeNode.static_serialize(root)
        b = TreeNode.deserialize(a)
        print(b.val)
