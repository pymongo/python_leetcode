"""
不要在遍历list的时候 插入或删除元素
哪怕用 nums.copy() 或 nums[:] 也不能安全地删除元素
>>> nums = [1, 2, 4, 4, 5]
>>> for index, value in enumerate(nums):
...     if value == 4:
...         del nums[index]
...
>>> print(nums)
[1, 2, 4, 5]
>>> # 数组的4并没有被删干净
"""


def iseven(number):
    """
    Checks if a number is even or odd

    >>> iseven(5)
    False
    >>> assert iseven(6)

    >>> iseven(6)
    True
    """
    return number % 2 == 0


if __name__ == "__main__":
    __import__("doctest").testmod()
