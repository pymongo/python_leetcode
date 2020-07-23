"""
如果有左子树为空(例如根节点没有左子树)，二叉树工具类生成或读取BFS的数组不是"满"二叉树，而且二叉树数组的最后一行还可能是颠倒的
于是我需要一个不会错+可读性更好的二叉树表示方式，[Construct Binary Tree from String]这题用括号区分字符串的子树就很不错
"""
import unittest
import collections
from .binary_tree import TreeNode


def str_to_tree_iterative(s: str):
    if not s:
        return None
    # 没有左子树和右子树
    if '(' not in s:
        return TreeNode(int(s))

    # 栈主要用来匹配括号
    stack = collections.deque()
    index = 0
    size = len(s)
    while index < size:
        if s[index] == ')':
            # TODO pop是干啥？
            stack.pop()
            index += 1
            continue

        if s[index] == '(':
            index += 1
            continue

        # next_idx = index
        val_end_idx = index
        while s[val_end_idx] != '(' and s[val_end_idx] != ')':
            val_end_idx += 1
        node = TreeNode(int(s[index:val_end_idx]))
        if stack:
            father = stack[-1]
            if father.left is None:
                father.left = node
            else:
                father.right = node
        stack.append(node)
        index = val_end_idx
    return stack[0]


# 56 ms 击败了95.32%
def my_tree_to_str(root: TreeNode):
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
        return f"{root.val}()({my_tree_to_str(root.right)})"
    elif root.left is not None and root.right is None:
        # 有左子树没有右子树
        return f"{root.val}({my_tree_to_str(root.left)})"
    else:
        return f"{root.val}({my_tree_to_str(root.left)})({my_tree_to_str(root.right)})"


