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
