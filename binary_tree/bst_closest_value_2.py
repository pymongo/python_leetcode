import unittest
from .binary_tree import TreeNode, dbg
from typing import List
import collections


# 我的思路: 先找到中序遍历的数组，然后根据有序数组最接近目标值的k项这题的二分法进行数据筛选
# 其它思路: 将对BST的操作抽象成对一位数组的操作，move_upper和move_lower是镜像操作，left 和 right 互相换一下就行。 相当于在 bst 里get next node & get previous node
# 我的思路背下来后可以同时解决迭代中序遍历+[Find K Closest Elements]两题
def bst_closest_1(root: TreeNode, target: float, k: int) -> List[int]:
    in_order = []
    if root is None:
        return in_order
    size = 0
    stack = collections.deque()
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        in_order.append(node.val)
        size += 1
        curr = node.right

    # 第二部分，在中序遍历的有序数组中查找与target最接近的k项，参考[Find K Closest Elements]这题
    start, end = 0, size - k
    while start < end:
        mid = start + (end - start) // 2
        if target - in_order[mid] > in_order[mid + k] - target:
            start = mid + 1
        else:
            end = mid
    return in_order[start:start + k]


def move_upper(stack: List[TreeNode]):
    print("In move_upper")
    print(stack)
    if stack[-1].right:
        # 例如"3(1()(2))(4)", target=0.2, 初始化后stack=[3,1], 2还没被访问过，此时把2入栈并将所有比2小而且比1大的入栈
        node = stack[-1].right
        while node:
            stack.append(node)
            node = node.left
    else:
        # 已经没有upper节点了，开始剔除栈中元素，这些被剔除的元素都应该是之前调用move_upper时访问过的，一定是从node的父节点一路往右走过来的，那我们从node一直删到node的父节点
        # 栈顶元素已经是最大节点了?
        node = stack.pop()
        # 例如"3(1()(2))(4)", target=0.2, 初始化后stack=[3,4], 这里会把3也清掉
        while stack and stack[-1].right == node:
            node = stack.pop()
    print(stack)


def move_lower(stack: List[TreeNode]):
    print("In move_lower")
    print(stack)
    if stack[-1].left:
        node = stack[-1].left
        while node:
            stack.append(node)
            node = node.right
    else:
        # 已经没有lower的节点了，所以把栈"清空"，，开始剔除栈中元素，这些被剔除的元素都应该是之前调用move_lower时访问过的
        # 一定是从node的父节点一路往左走过来的，那我们从node一直删到node的父节点
        node = stack.pop()
        while stack and stack[-1].left == node:
            node = stack.pop()
    print(stack)


def is_lower_closer(lower_stack: List[TreeNode], upper_stack: List[TreeNode], target: float) -> bool:
    if not lower_stack:
        return False
    if not upper_stack:
        return True
    return target - lower_stack[-1].val < upper_stack[-1].val - target


def bst_closest_2(root: TreeNode, target: float, k: int) -> List[int]:
    if root is None:
        return []

    lower_stack = []
    while root:
        lower_stack.append(root)
        if target < root.val:
            root = root.left
        else:
            root = root.right
    # 为什么要用两个stack? 因为一个逆序走一个正序走，必须用两个栈隔离开各自的操作
    upper_stack = lower_stack.copy()
    print("由于初始化后lower_stack和upper_stack相同，所以要让lower_stack和upper_stack不同(错开一个值)")
    if lower_stack[-1].val < target:
        # 由于初始化后lower_stack和upper_stack相同，所以要让lower_stack和upper_stack不同(错开一个值)
        move_upper(upper_stack)
    else:
        move_lower(lower_stack)

    result: List[int] = []
    print("Before for i in range(k):")
    for i in range(k):
        if is_lower_closer(lower_stack, upper_stack, target):
            result.append(lower_stack[-1].val)
            # lower_stack栈顶的值已被记入，应该往下移动
            move_lower(lower_stack)
        else:
            result.append(upper_stack[-1].val)
            move_upper(upper_stack)
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("3(1()(2))(4)", 0.275000, 2, [1, 2]),
        # ("2(1)(3)", 5.571429, 2, [2, 3]),
    ]

    def test_bst_closest_1(self):
        for binary_tree, target, k, expected in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            print(root)
            self.assertEqual(expected, bst_closest_1(root, target, k))

    def test_bst_closest_2(self):
        for binary_tree, target, k, expected in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            self.assertEqual(expected, bst_closest_2(root, target, k))
