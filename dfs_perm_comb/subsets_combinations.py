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

TODO 组合数的遍历树状图

TODO 左边的分支表示选择加上待选数字、右分支表示「不加」待选数字
待选数字                   []
1              [1]                 []
2      [1,2]        [1]       [2]      []
3 [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []

TODO 排列数的遍历树状图(排列数需要used/visited变量存储用过的数(每次都要从头到尾遍历数组)，而组合数是遍历数组的数作为下一层待选数字就行了)

                      []
       [1]            [2]            [3]
   [1,2] [1,3]    [2,1] [2,3]    [3,1] [3,2]
[1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]

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

TODO 本题相当于impl了哪些内置库
相当于让你求:
results = []
for i in range(len(nums)+1):
    results.append(itertools.combinations(nums, i))
return results
"""
import unittest
from typing import List
import collections


class Solution(unittest.TestCase):
    TESTCASES = [
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
        # 需要去重的测试用例
        ([1, 2, 2], [
            [2],
            [1],
            [1, 2, 2],
            [2, 2],
            [1, 2],
            []
        ]),
    ]

    @staticmethod
    def bfs_binary_tree_dummy_node(nums: List[int]) -> List[List[int]]:
        # 题目要求解集要升序
        nums.sort()
        # TODO 不推荐使用哨兵节点去层级遍历，刚拿出的节点又要放进去太愚蠢了
        q = collections.deque([[], None])
        for i in range(len(nums)):
            while True:
                subset = q.popleft()
                if subset is None:
                    q.append(None)
                    break
                new_subset = subset.copy()
                new_subset.append(nums[i])
                q.append(new_subset)
                # FIXME 刚拿出的节点又要放进去太愚蠢了
                q.append(subset)
        q.pop()  # 去掉末尾的None
        return list(q)

    @staticmethod
    def bfs_binary_tree_best(nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        subsets_len = 1
        for num in nums:
            for i in range(subsets_len):
                new_subset = subsets[i].copy()
                new_subset.append(num)
                subsets.append(new_subset)
            subsets_len *= 2
        return subsets

    def test_bfs_n_tree_search(self):
        for nums, subsets in self.TESTCASES:
            if nums == [1,2,2]:
                continue
            self.assertCountEqual(subsets, self.bfs_n_tree_search(nums))

    @staticmethod
    def bfs_n_tree_search(nums: List[int]) -> List[List[int]]:
        # N叉搜索树版本(全排列的搜索树)，如果是子集问题则需要收录「每一个节点」，不像子集的二叉树只需要记录最后一层
        if not nums:
            return []
        queue = [[]]
        index = 0
        while index < len(queue):
            print(queue)
            subset = queue[index]
            for num in nums:
                if subset and subset[-1] >= num:
                    # 因为subset是排好序的subset[-1] >= num说明有重复
                    continue
                queue.append(subset + [num])
            index += 1
        return queue

    def test_cascading(self):
        for nums, subsets in self.TESTCASES:
            self.assertCountEqual(subsets, self.bfs_binary_tree_with_duplicate(nums))

    @staticmethod
    def bfs_binary_tree_with_duplicate(nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        subsets_last_element_index = [-1]
        for i in range(len(nums)):
            for j in range(len(subsets)):
                # 去重，如果有重复数字出现，只有前上一个数字选了才能选当前数字
                if i > 0 and nums[i] == nums[i - 1] and subsets_last_element_index[j] != i - 1:
                    # 举个例子，假设输入是[1, 2, 2, 2, 3]，如果不加判断直接做的话，
                    # 那么就会出现[1, 第一个2, 第二个2, 3],[1, 第一个2, 第三个2, 3]这样的重复。
                    # 为了避免这样的重复，可以规定当有多个连续数字出现的时候，只有选了在数组中紧邻的前一个相同数字，才能够选当前数字。
                    # 比如例子中，只有选了第一个2，才能选第二个2,只有选了二个2，才能选第三个2，
                    # 这样一来，我们上面提到的[1, 第一个2, 第三个2, 3]这种情况就会被排除掉，从而达到去重效果。
                    continue
                new_subset = subsets[j].copy()
                new_subset.append(nums[i])
                subsets_last_element_index.append(i)
                subsets.append(new_subset)
        return subsets

    def test_dfs_solution(self):
        for nums, subsets in self.TESTCASES:
            self.assertCountEqual(subsets, self.dfs_solution(nums))

    @staticmethod
    def dfs_solution(nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        size = len(nums)

        def dfs(start: int, subset: List[int]):
            # 当前组合存入res
            results.append(subset.copy())

            # 当前的subset里还能往后加什么(为subset(当前组合)新增一位元素)，例如[1,2]往后只能加3
            for i in range(start, size):
                # 剪枝(去重)
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # [1] => [1,2]
                subset.append(nums[i])

                # 下一层搜索，去寻找所有以[1,2]开头的子集
                dfs(i + 1, subset)

                # [1,2] => [1]
                # 撤销掉上上个语句subset.append(nums[i])的影响，也就是回溯(或用subset.pop())
                # 只有这样子，第二遍for循环时才能跟第一遍for循环的开头时的subset一样
                # 或者用del subset[-1]
                # TODO 注意只有引用类型传参才需要复原, primitive types是值传递，所以本层调用的start回溯时不需要复原
                subset.pop()

        dfs(0, [])
        return results
