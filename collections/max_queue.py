import collections

class MaxQueue:

    def __init__(self):
        self.q = collections.deque()
        # 单调递减队列，队头是最大值
        self.m = collections.deque()

    def max_value(self) -> int:
        if not self.m:
            return -1
        return self.m[0]

    def push_back(self, value: int) -> None:
        # m是单调递减队列
        while self.m and self.m[-1] < value:
            self.m.pop()
        # 如果最大值有重复，需要记录重复项
        self.m.append(value)
        self.q.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        pop_val = self.q.popleft()
        if self.m[0] == pop_val:
            self.m.popleft()
        return pop_val
