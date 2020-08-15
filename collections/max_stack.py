import heapq


class MaxStack:
    def __init__(self):
        self.S = []
        self.M = []

    def push(self, x):
        self.S.append(x)
        if not self.M:
            self.M.append(x)
        else:
            self.M.append(max(self.M[-1], x))

    def pop(self):
        self.M.pop()
        return self.S.pop()

    def top(self):
        return self.S[-1]

    def peekMax(self):
        return self.M[-1]

    # TODO 如何将该操作降低到logn的时间复杂度
    # heap+HashSet+Stack: heap为了快点找到max, set用于标记(soft_delete)被删元素(类似限价交易中标记堆订单的被删除订单)
    # 如何处理重复元素——自增的ID
    def popMax(self):
        max_val = self.peekMax()
        temp = []
        while self.top() != max_val:
            # 注意两个栈都变
            temp.append(self.pop())
        self.S.pop()
        self.M.pop()
        if temp:
            # 注意两个栈都变
            self.push(temp.pop())
        return max_val


# 耗时56ms，而不用heap+set的版本耗时101ms
# 由于每个数最多在stack和heap中各删一次，所以除了push、popMax、peekMax(可能包含heappop)是O(logN)，其余都是O(1)
class MaxStackHeap:
    def __init__(self):
        self.heap = []
        self.stack = []
        self.popped_set = set()
        self.next_id = 0

    def push(self, x):
        # heapq只有小根堆，只能通过负数模拟大根堆
        item = (-x, -self.next_id)
        self.stack.append(item)
        heapq.heappush(self.heap, item)
        self.next_id += 1

    def _clear_popped_in_stack(self):
        while self.stack and self.stack[-1] in self.popped_set:
            self.popped_set.remove(self.stack[-1])
            self.stack.pop()

    def _clear_popped_in_heap(self):
        while self.heap and self.heap[0] in self.popped_set:
            self.popped_set.remove(self.heap[0])
            heapq.heappop(self.heap)

    def pop(self):
        self._clear_popped_in_stack()
        item = self.stack.pop()
        # 通知栈heap，栈这里删了其中一个元素
        self.popped_set.add(item)
        return -item[0]

    def top(self):
        self._clear_popped_in_stack()
        item = self.stack[-1]
        return -item[0]

    def peekMax(self):
        self._clear_popped_in_heap()
        item = self.heap[0]
        return -item[0]

    def popMax(self):
        self._clear_popped_in_heap()
        item = heapq.heappop(self.heap)
        # 通知栈，heap这里删了其中一个元素
        self.popped_set.add(item)
        return -item[0]
