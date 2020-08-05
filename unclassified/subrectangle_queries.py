from typing import List


# noinspection SpellCheckingInspection,PyPep8Naming
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        """
        更新以(row1,col1)为左上角, (row2,col2)为右下角的子矩阵的所有值(一个矩形区域的值)
        """
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.data[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.data[row][col]


# noinspection SpellCheckingInspection,PyPep8Naming
class BestPerformance:

    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle
        self.log = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # 修改一个区域的值非常耗时，可以把每次对数组的修改记入到log中作为缓存
        # 查询时从后往前翻log，如果没有log修改过(row,col)，则返回数组的原值
        self.log.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for r1, c1, r2, c2, v in self.log[::-1]:
            if r1 <= row <= r2 and c1 <= col <= c2:
                return v
        return self.data[row][col]
