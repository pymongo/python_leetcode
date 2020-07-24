"""
如果有左子树为空(例如根节点没有左子树)，二叉树工具类生成或读取BFS的数组不是"满"二叉树，而且二叉树数组的最后一行还可能是颠倒的
于是我需要一个不会错+可读性更好的二叉树表示方式，[Construct Binary Tree from String]这题用括号区分字符串的子树就很不错
"""
import unittest
import collections
from .binary_tree import TreeNode, dbg


# FIXME 解析字符串成二叉树这题用递归做真的有点难，我还没想到寻找左右子树分割位置的办法
def str_to_tree_recursive(s: str):
    if not s:
        return None
    if '(' not in s:
        return TreeNode(int(s))
    left_parentheses = s.find('(')
    right_parentheses = s.rfind(')')
    subtree = s[left_parentheses + 1:right_parentheses]
    root = TreeNode(int(s[1:left_parentheses]))
    if subtree[:2] == '()':
        root.left = None
        root.right = str_to_tree_recursive(subtree[2:])
    elif ')(' in subtree:
        pass
    return root


# 99.59%
def str_to_tree_iterative_lintcode_best(s: str):
    stack = collections.deque()
    token = ""
    for char in s:
        if char != '(' and char != ')':
            token += char
            continue
        if token:
            node = TreeNode(int(token))
            if stack:
                stack_peek = stack[-1]
                if stack_peek.left is None:
                    stack_peek.left = node
                else:
                    stack_peek.right = node
            stack.append(node)
            token = ""
        if char == ')':
            stack.pop()
    return stack[0] if stack else None


# 用val_len取代token，去掉了字符串拼接操作，性能更优
def str_to_tree_iterative_best_performance(s: str):
    stack = collections.deque()
    val_len = 0
    for i in range(len(s)):
        if s[i] != '(' and s[i] != ')':
            val_len += 1
            continue
        if val_len:
            node = TreeNode(int(s[i - val_len:i]))
            if stack:
                stack_peek = stack[-1]
                if stack_peek.left is None:
                    stack_peek.left = node
                else:
                    stack_peek.right = node
            stack.append(node)
            val_len = 0
        if s[i] == ')':
            stack.pop()
    return stack[0] if stack else None


# 56 ms 击败了95.32%
def my_tree_to_str_recursive(root: TreeNode):
    """
    root不为None时，主要区分三种情况:
    1. 没有左右子树: 只返回root的值
    2. 没有左子树，但有右子树: 左子树要写成括号
    3. 有左子树，没有右子树: 左子树正常写，右子树要写成括号
    @return:
    """
    if root is None:
        return ""
    if root.left is None and root.right is None:
        return str(root.val)
    elif root.left is None and root.right is not None:
        # 如果没有左子树但是有右子树
        return f"{root.val}()({my_tree_to_str_recursive(root.right)})"
    elif root.left is not None and root.right is None:
        # 有左子树没有右子树
        return f"{root.val}({my_tree_to_str_recursive(root.left)})"
    else:
        return f"{root.val}({my_tree_to_str_recursive(root.left)})({my_tree_to_str_recursive(root.right)})"


def tree_to_str_iterative(root: TreeNode):
    s = ""
    if root is None:
        return s
    visited = set()
    stack = collections.deque()
    stack.append(root)
    while stack:
        node = stack[-1]
        if node in visited:
            stack.pop()
            s += ')'
            # dbg(s)
            continue
        visited.add(node)
        s += '(' + str(node.val)
        # dbg(s)
        if node.left is None and node.right is not None:
            s += '()'
            # dbg(s)
        # 这里有个细节，先入栈左子树节点再入栈右子树节点，那么出栈时还是按左节点优先
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    # 去掉头尾的括号
    return s[1:-1]


class Testing(unittest.TestCase):
    def test_tree_to_str_iter(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        tree_to_str_iterative(root)
