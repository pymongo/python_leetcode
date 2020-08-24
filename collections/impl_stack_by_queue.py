"""
方法1:
入栈: 正常入队q1
出栈:
1. 出栈时将队列前面n-1个元素入队到q2
2. 出队q1的最后一个元素并记为返回值
3. 再将q2的所有元素重新入队q1(拷贝回来)，q2相当于临时变量

方法2:
入栈:
1. q2为空，q1的出队顺序与栈相同，新元素入队q2
2. q1的队头逐个拼到q2
3. 将q2所有元素入队到q1(拷贝)
出栈:
出队的顺序就是出栈的顺序

方法3: (一个队列)
出队顺序与出栈保持一致，因此每次入队后都需要(循环入队size-1次)达到反转的效果
例如
3 -> [2,1]:
[2,1,3]
[1,3,2]
[3,2,1]
"""


class MyStack:

    def __init__(self):
        self.nums = []
        self.size = 0

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.size += 1

    def pop(self) -> int:
        # TODO 处理数组为空的情况
        self.size -= 1
        return self.nums.pop()

    def top(self) -> int:
        return self.nums[self.size - 1]

    def empty(self) -> bool:
        return self.size == 0
