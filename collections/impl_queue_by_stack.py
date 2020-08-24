# 临摹了leetcode解法二
class MyQueue:

    def __init__(self):
        """
        因为栈没法实现像队列那样可以循环走的特性，所以还得要两个栈
        """
        self.s1 = []
        self.s2 = []
        self.front = None
        self.size = 0

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        s1 中栈底元素就变成了 s2 的栈顶元素，这样就可以直接从 s2 将它弹出了
        TODO 一旦 s2 变空了，我们只需把 s1 中的元素再一次转移到 s2 就可以了
        均摊时间复杂度是O(1)，最好和最坏情况不会同时出现
        """
        # deque.popleft() is faster than list.pop(0)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self) -> bool:
        return not self.s1 and not self.s2


class TwoStackQueue:
    def __init__(self):
        # 新元素加到s1
        self.s1 = []
        # 出队从s2这里出
        self.s2 = []

    def _s1_to_s2(self):
        if self.s2:
            # 如果s2不空，说明有先入队的在栈顶
            # 所以不需要将刚入队的s1元素倒入到s2
            return
        while self.s1:
            self.s2.append(self.s1.pop())

    def push(self, val):
        self.s1.append(val)

    def pop(self):
        self._s1_to_s2()
        return self.s2.pop()

    def peek(self):
        self._s1_to_s2()
        return self.s2[-1]