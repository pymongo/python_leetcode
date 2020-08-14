import unittest
from typing import List, Tuple


# 既然每行只能有一个皇后，皇后的位置用的是一个一位数组: 数组下标表示皇后的行号，值表示皇后的纵坐标
class Solution(unittest.TestCase):
    PRINT_ALL_SOLUTIONS_TEST_CASES: List[Tuple[int, List[List[str]]]] = [
        (4, [[".Q..",
              "...Q",
              "Q...",
              "..Q."],
             ["..Q.",
              "Q...",
              "...Q",
              ".Q.."]]),
    ]

    def test_print_all_solutions(self):
        for n, output in self.PRINT_ALL_SOLUTIONS_TEST_CASES:
            self.assertEqual(output, self.print_all_solutions(n))

    # Runtime: 52 ms, faster than 95.44%
    @staticmethod
    def print_all_solutions(n: int) -> List[List[str]]:
        """
        入口函数: N皇后问题1的入口函数
        """
        results = []
        # TODO 优化思路: 初始化时设定Set的容量固定容量提高性能，例如Rust的: HashSet::with_capacity()
        # 斜率为左上到右下的直线方程的常系数b(x+y=b)
        row_col_sum_set = set()
        # 斜率为右上到左下的直线方程的常系数b(x-y=b)
        row_col_diff_set = set()
        # 已使用的列号
        used_cols = set()

        # 参数row表示下一个皇后的行号
        def search(queen_cols: List[int], row: int):
            if row == n:
                results.append(Solution.render_board(queen_cols, n))
                return

            for col in range(n):
                if col in used_cols:
                    continue
                row_col_sum = row + col
                if row_col_sum in row_col_sum_set:
                    continue
                row_col_diff = row - col
                if row_col_diff in row_col_diff_set:
                    continue

                queen_cols.append(col)
                used_cols.add(col)
                row_col_sum_set.add(row_col_sum)
                row_col_diff_set.add(row_col_diff)

                search(queen_cols, row+1)

                queen_cols.pop()
                used_cols.remove(col)
                row_col_sum_set.remove(row_col_sum)
                row_col_diff_set.remove(row_col_diff)

        search([], 0)
        return results

    # @staticmethod
    # def search(queens_col):
    #     pass

    @staticmethod
    def count_solutions():
        """
        入口函数: N皇后问题2的入口函数
        """
        pass

    @staticmethod
    def render_board(queen_cols, n: int) -> List[str]:
        board = []
        for col in queen_cols:
            row = ['.'] * n
            row[col] = 'Q'
            board.append(''.join(row))
        return board

    @staticmethod
    def itertools_permutations_n_queen_solution(n: int):
        """
        https://www.zhihu.com/question/37046157/answer/70747261
        http://wordaligned.org/articles/8-queens-puzzle
        https://leetcode.com/problems/n-queens/discuss/437421/Simple-python-3-solution-with-itertools.permutations
        首先`itertools.permutations`保证了每个皇后的列号都不一样
        因此只需要判断斜的方向有没有重合
        皇后斜的方向就只有两种，左上-右下 和 右上-左下
        而棋盘的左上-右下的直线方程的斜率为1、右上-左下的斜率为-1
        左上-右下的直线方程为: y= x+b => x-y=-b
        右上-左下的直线方程为: y=-x+b => x+y=b
        所以表达式`queen_cols[i] + i`能得到右上-左下直线方程的「常系数b」
        所以只要N皇后位置算出的斜率为1和斜率为-1的8条直线的常系数都不一样，则N皇后问题是正确的，否则必有两个皇后在同一条直线上
        """
        import itertools
        # for queen_cols in itertools.permutations(range(n)):
        #     # 一种通过斜率辨别法, 斜率为正的直线方程左上到右下，判断直线方程的常系数是否有相同的，相同说明两个皇后在一条斜线上
        #     if n == len({queen_cols[i] + i for i in range(n)}) \
        #          == len({queen_cols[i] - i for i in range(n)}):
        #         print({queen_cols[i] + i for i in range(n)})
        #         print({queen_cols[i] - i for i in range(n)})
        #         for col in queen_cols:
        #             s = ['.'] * n
        #             s[col] = 'Q'
        #             print(''.join(s))
        #         print()
        solutions = []
        # TODO itertools.permutations不用迭代器铁超时，只是这题时间限制放的很松
        for queen_cols in itertools.permutations(range(n)):
            if Solution.check_queen_cols_permutations(queen_cols):
                solutions.append(Solution.render_board(queen_cols, n))
        return solutions

    @staticmethod
    def check_queen_cols_permutations(queen_cols) -> bool:
        """
        仅用于检测itertools.permutations的皇后们斜方向是否有两个皇后在同一条直线上
        DFS解法中除了需要检测斜方向，还要检测列坐标有没有重复
        而且这里检测斜方向的过程跟DFS回溯里不太一样
        这里用的是HashSet方法，DFS里更多的是遍历一遍新坐标与老皇后逐个比较
        """
        # 左上-右下方向的直线方程的常系数
        constant_of_minus_slope_of_liner = set()
        # 左上-右下方向的直线方程的常系数
        constant_of_positive_slope_of_liner = set()
        for x, y in enumerate(queen_cols):
            s = x + y
            if s in constant_of_minus_slope_of_liner:
                return False
            constant_of_minus_slope_of_liner.add(s)
            d = x - y
            if d in constant_of_positive_slope_of_liner:
                return False
            constant_of_positive_slope_of_liner.add(d)
        return True

    def test_itertools_permutations_n_queen_solution(self):
        self.itertools_permutations_n_queen_solution(4)


"""
N皇后的问题在LeetCode上DFS回溯的算法题里不算特别难，相比word_ladder_2代码量也很少

只要代码结果拆分合理，这道题就很难写错，我认为这题可以拆为4个部分:

- 入口函数
- DFS搜索回溯函数(search)
- 判断当前放置皇后的位置是否合法(is_invalid)
- 将正确的皇后位置渲染成棋盘字符串(render_board)，然后在DFS搜索回溯函数里加到答案集内

我认为主要难点就两个 通过什么数据结构存储皇后的位置 和 如何判断某个位置是否合法

既然每行只能有一个皇后，皇后的位置用的是一个一位数组: 数组下标表示皇后的行号，值表示皇后的纵坐标

所以`for x, y in enumerate(queen_cols)`就能得到皇后们的行号和列号

先看一段打印8皇后的简单版代码:

```python
import itertools
for queen_cols in itertools.permutations(range(n)):
    if n == len({queen_cols[i] + i for i in range(n)}) \
         == len({queen_cols[i] - i for i in range(n)}):
        for col in queen_cols:
            s = ['.'] * n
            s[col] = 'Q'
            print(''.join(s))
        print()
```

解释下`len({queen_cols[i] + i for i in range(n)})`这行为什么能验证N皇后

首先`itertools.permutations`保证了每个皇后的列号都不一样

因此只需要判断斜的方向有没有重合

可以将棋盘看做一个初中数学的xoy坐标系，只不过顺时针转动了90度，y轴是横着的

皇后斜的方向就只有两种，左上-右下 和 右上-左下

而xoy坐标系下棋盘的左上-右下的直线方程的斜率为1、右上-左下的斜率为-1

左上-右下的直线方程为: y= x+b => x-y=-b

右上-左下的直线方程为: y=-x+b => x+y=b

所以表达式`queen_cols[i] + i`能得到右上-左下直线方程的「常系数b」

初中数学学过点-斜式方程，通过一点和斜率可以的得到直线方程

所以只要N皇后位置算出的斜率为1和斜率为-1的8条直线的常系数都不一样，则N皇后问题是正确的，否则必有两个皇后在同一条直线上
"""
