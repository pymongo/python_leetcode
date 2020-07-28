"""
Substring、Subsequence、Subsets
## 子序列
子序列可以是非连续的字符
对于长度为n的字符串的子序列，每个字符都有选或不选两种可能。
因此其子序列的数量是指数级别O(2^n)的
## 子集
子集长度为1公有C(n, 0)，子集长度为1公有C(n, 1)...
所有总共可以穷举出C(n, 0) + ... + C(n, n) = 2^n种，怎么跟子序列一样呢

既然决策总数是2^n，我们可以抽象成一个深度为n的二叉树，那么二叉树的最后一层就是我们想要的
DFS的过程出发点是空集，然后是否选1可以分岔为2个决策，第二层的每个决策根据是否选2又可以分岔为4个 ...
[]
[1] []
[1,2] [1] [2] []
[1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
这题也能用BFS来做，但BFS不适合解这种问题而且模板较难

# 去重
题目没有对返回值结果做要求，但是要求返回的结果要无重复，例如[1, 3]和[3, 1]不能重复出现
为什么对nums排序处理后就能保证无重复?
例如原数组是[1,3,1]如果不排序的话, [1,3]和[3,1]、[1]和[1]重复了
[]
[1] []
[1,3] [1] [3] []
[1,3,1] [1,3] [1,1] [1] [3,1] [3] [1] []
如果[1,3,1]排序成[1,1,3]
[]
[1] []
[1,1] [1] [1] [] (提前发现重复的[1]和[1])
干掉重复项之后再分岔
[1,1] [1] []
[1,1,3] [1,1] [1,3] [1] [3] []

如果没有重复元素，三行就搞定:
output = [[]]
for num in nums:
    output += [curr + [num] for curr in output]
return output
"""
import unittest
from typing import List
import collections


# 32 ms, 在所有 Python3 提交中击败了 96.94%
def cascading(nums: List[int]) -> List[List[int]]:
    # shadowing
    nums = sorted(nums)
    q = collections.deque([[], None])
    # q: List[Optional[List[int]]] = [[], None]
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            # 只有当前后有重复项时才要干掉重复项后分岔
            while True:
                subset = q.popleft()
                if subset is None:
                    q.append(None)
                    break
                new_subset = subset.copy()
                new_subset.append(nums[i])
                # subsets_1的输入用例没有重复元素，但是subsets_2的输入用例有重复元素
                if new_subset not in q:
                    q.append(new_subset)
                if subset not in q:
                    q.append(subset)
        else:
            while True:
                subset = q.popleft()
                if subset is None:
                    q.append(None)
                    break
                new_subset = subset.copy()
                new_subset.append(nums[i])
                q.append(new_subset)
                q.append(subset)
    # 去掉末尾的None
    q.pop()
    return list(q)


# 用递归版本(回溯的解法)
def dfs_helper(nums: List[int]) -> List[List[int]]:
    result = []
    # 排序
    nums.sort()
    # dfs搜索
    size = len(nums)
    dfs(nums=nums, nums_start_index=0, size=size, subset=[], result=result)
    return result


def dfs(nums: List[int], nums_start_index: int, size: int, subset: List[int], result: List[List[int]]):
    # 当前组合存入res
    result.append(subset.copy())
    # 为subset(当前组合)新增一位元素
    # 当前的subset里还能往后加什么，例如[1,2]往后只能加3
    for i in range(nums_start_index, size):
        # 剪枝(去重)
        if i > nums_start_index and nums[i] == nums[i - 1]:
            continue

        # [1] => [1,2]
        subset.append(nums[i])

        # 下一层搜索，去寻找所有以[1,2]开头的子集
        dfs(nums=nums, nums_start_index=i+1, size=size, subset=subset, result=result)

        # [1,2] => [1]
        # 撤销掉上上个语句subset.append(nums[i])的影响，也就是回溯(或用subset.pop())
        # 只有这样子，第二遍for循环时才能跟第一遍for循环的开头时的subset一样
        # 或者用del subset[-1]
        subset.pop()


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 1], [
            [1, 1, 3], [1, 1], [1, 3], [1], [3], []
        ]),
        ([1, 2, 3], [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]),
    ]

    def test_cascading(self):
        for nums, subsets in self.TEST_CASES:
            self.assertCountEqual(subsets, cascading(nums))

    def test_dfs(self):
        for nums, subsets in self.TEST_CASES:
            self.assertCountEqual(subsets, dfs_helper(nums))
