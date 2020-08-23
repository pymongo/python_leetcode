import collections
from typing import List


# 将一个嵌套数组改成一位数组
class Solution:

    @staticmethod
    def flatten(lists: List[int]):
        res = []
        q = collections.deque(lists)
        while q:
            item = q.popleft()
            if isinstance(item, list):
                # 保证重新扔回队列头部时是按照数组原有顺序
                for each in reversed(item):
                    q.appendleft(each)
                continue
            res.append(item)
        return res
