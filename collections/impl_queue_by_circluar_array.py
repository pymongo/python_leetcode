class CircularQueue:
    """
    Enquue
    0 1 2 3
      ^ ^
      F R
    0 1 2 3
      ^   ^
      F   R
    """

    def __init__(self, n):
        self.size = 0
        self.n = n
        self.front = 0
        self.rear = 0
        self.nums = [None] * self.n

    def isFull(self):
        return self.size == self.n

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, val):
        self.nums[self.rear] = val
        self.rear = (self.rear + 1) % self.n
        self.size += 1

    def dequeue(self):
        # 不用清空被删元素，下次入队时会覆盖掉原有的值
        pop_item = self.nums[self.front]
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return pop_item