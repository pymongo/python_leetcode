from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 32 ms, faster than 94.25%
# 本题最有意思的解法是「有丝分裂」旧节点和新节点交错的方法:
# 1. 每个节点向右复制一个: A->B => A->A'->B->B'
# 2. 复制老节点的random、next指针
# 3. 将新节点从原链表中剥离出来
# 另一种解法是由于random指针的存在，链表很可能是个环，可以用图的DFS回溯或BFS遍历去复制
class Solution:
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def copyRandomList(self, head: 'Node') -> Optional[Node]:
        if head is None:
            return None
        # 与clone_graph一题类似，也需要一个key: 老节点, value: 新节点的字典
        old_new_mapping = dict()

        # 1. 复制所有点(分层处理，完整复制完点后就不会出现边/指针找不到的情况)
        old = head
        while old is not None:
            new = Node(old.val)
            old_new_mapping[old] = new
            old = old.next

        # 2. 复制所有边(next和random指针)
        old = head
        while old is not None:
            new = old_new_mapping[old]
            # get方法: 如果key不存在则返回None
            new.next = old_new_mapping.get(old.next)
            new.random = old_new_mapping.get(old.random)
            old = old.next

        return old_new_mapping[head]
