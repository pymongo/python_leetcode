"""
O(1)的min操作，很容易想到要用小根堆
但是堆不能满足题目的push/pop也要O(1)时间复杂度的要求
本题的巧妙在于要用两个栈, 原栈叫S，维护最低值的栈叫M(min_stack)
每当新元素push时，如果新元素小于M.peek()，则M.push(val)，否则M.push(M.peek())
M栈相当于记录了从加入1个元素、加入2个元素...加入n个元素的情况下的最小值
push(7)
M: 3 7
S: 3 3
push(2)
M: 3 7 2
S: 3 3 2
"""


class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []
        self.peek = -1

    def push(self, val: int):
        self.stack.append(val)
        if self.peek == -1:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[self.peek], val))
        self.peek += 1

    def pop(self) -> int:
        # 本题不用考虑pop空栈的问题
        self.min_stack.pop()
        self.peek -= 1
        return self.stack.pop()

    # noinspection PyPep8Naming
    def getMin(self) -> int:
        return self.min_stack[self.peek]

    def top(self) -> int:
        return self.stack[self.peek]


# 节约min_stack空间的算法
class MinStackBetter:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # 如果最小值需要更新或重复的元素出现，才push最小栈，节约空间
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val
