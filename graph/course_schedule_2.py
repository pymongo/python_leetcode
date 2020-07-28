import unittest
import collections
from typing import List
import enum


def course_order(courses_count: int, prerequisites: List[List[int]]) -> List[int]:
    """
    prerequisites可以理解成一种简单的有向图邻接表(adjacency list)
    Input: 4, [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]
    """
    # index: course_id, value: indegree's courses id
    courses_indegree = []
    # index: course_id, value: next_course require current course_id
    next_courses: List[List[int]] = []
    for _ in range(courses_count):
        courses_indegree.append(0)
        next_courses.append([])

    for course_id, pre_course_id in prerequisites:
        courses_indegree[course_id] += 1
        next_courses[pre_course_id].append(course_id)
    zero_indegree_queue = collections.deque()
    for course_id in range(courses_count):
        if courses_indegree[course_id] == 0:
            zero_indegree_queue.append(course_id)
    learn_order = []
    learn_order_len = 0
    while zero_indegree_queue:
        course_id = zero_indegree_queue.popleft()
        learn_order.append(course_id)
        learn_order_len += 1
        for next_course_id in next_courses[course_id]:
            courses_indegree[next_course_id] -= 1
            if courses_indegree[next_course_id] == 0:
                zero_indegree_queue.append(next_course_id)
    # 图中有死循环，不能完整地学完课程
    if learn_order_len != courses_count:
        return []
    return learn_order


# DFS过程中节点的状态
class State(enum.Enum):
    """
    对于图中的任意一个节点，它在搜索的过程中有三种状态，即：
    「未搜索」：我们还没有搜索到这个节点；
    「搜索中」：我们搜索过这个节点，但还没有回溯到该节点，即该节点还没有入栈，还有相邻的节点没有搜索完成
    「已完成」：我们搜索过并且回溯过这个节点，即该节点已经入栈，并且所有该节点的相邻节点都出现在栈的更底部的位置，满足拓扑排序的要求
    """
    UNVISITED = 0
    SEARCHING = 1
    VISITED = 2


def dfs(
    course_id: int,
    next_courses: List[List[int]],
    visited: List[State],
    result: List[int],
) -> bool:
    """
    @return: is_circular_dependency
    """
    visited[course_id] = State.SEARCHING
    for next_course_id in next_courses[course_id]:
        if visited[next_course_id] == State.UNVISITED:
            if dfs(next_course_id, next_courses, visited, result):
                return True
        elif visited[next_course_id] == State.SEARCHING:
            # 出现循环依赖
            # is_circular_dependency = True
            return True
    visited[course_id] = State.VISITED
    result.insert(0, course_id)
    return False


def dfs_helper(courses_count: int, prerequisites: List[List[int]]) -> List[int]:
    visited: List[State] = []
    # index: course_id, value: next_course require current course_id
    next_courses: List[List[int]] = []
    for _ in range(courses_count):
        visited.append(State.UNVISITED)
        next_courses.append([])
    for course_id, pre_course_id in prerequisites:
        next_courses[pre_course_id].append(course_id)
    result = []
    # is_circular_dependency = False
    for course_id in range(courses_count):
        if visited[course_id] == State.UNVISITED:
            if dfs(course_id, next_courses, visited, result):
                return []
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3])
    ]

    def test_course_order(self):
        for courses_count, prerequisites, learn_order in self.TEST_CASES:
            self.assertCountEqual(learn_order, course_order(courses_count, prerequisites))

    def test_dfs(self):
        for courses_count, prerequisites, learn_order in self.TEST_CASES:
            # two list contain the same elements but order is different
            # a and b have the same elements in the same number, regardless of their order
            # https://stackoverflow.com/questions/12813633/how-to-assert-two-list-contain-the-same-elements-in-python
            self.assertCountEqual(learn_order, dfs_helper(courses_count, prerequisites))
