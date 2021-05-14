"""
## 牛客网Python刷题stdin问题
牛客网上面大部分题都不是像leetcode那样将解答写在Solution类的实例方法上
而是 从stdin读取测试用例，再通过stdout输出返回值

## 牛客网的Python版本不完全支持typehint

牛客网的python3版本是3.5，刚开始支持typehint，但仅在函数入参和返回值中支持typehint
不支持Python 3.6的typehint/variable annotations
[variable annotations](https://docs.python.org/3/whatsnew/3.6.html)

```
PEP 526: Syntax for variable annotations
PEP 484 introduced the standard for type annotations of function parameters, a.k.a. type hints. This PEP adds syntax to Python for annotating the types of variables including class variables and instance variables:

primes: List[int] = []

captain: str  # Note: no initial value!

class Starship:
    stats: Dict[str, int] = {}
```
"""
import sys


def int_array_split_whitespace():
    """
    [2019 PayPal实习生招聘编程卷 - [编程题]飞机最低可俯冲高度](https://nowcoder.com/test/16723511/summary)
    输入样例:
    1 1000
    """
    # split()方法默认会以空格作为分隔符
    nums = [int(num) for num in input().split()]
    print(nums)


def int_array_split_newline_1():
    """
    [牛客网-在线编程-连续子数组最大和](https://nowcoder.com/practice/03d341fb6c9d42debcdd38d82a0a545c)
    提示: 在IDEA的运行窗口，要通过cmd+D发送EOF，因为Ctrl+D是Debug的快捷键。在Terminal上Ctrl+D就能发送EOF了
    输入样例:
    1
    2
    """
    import fileinput
    nums = [int(line) for line in fileinput.input()] # or for line in sys.stdin.readlines()
    print(nums)


def multi_lines_multi_value():
    """
    [牛客网-在线编程-连续子数组最大和](https://nowcoder.com/practice/03d341fb6c9d42debcdd38d82a0a545c)
    输入样例:
    2.0
    5
    3.0 5.0
    6.0 13.0
    2.0 6.0
    7.0 12.0
    0.0 2.0

    输出样例:
    [[0, 2], [1, 3], [4]]
    """
    distance = float(sys.stdin.readline().rstrip('\n'))
    n = float(sys.stdin.readline().rstrip('\n'))
    coordinates = []
    for line in sys.stdin.readlines():
        values = line.rstrip('\n').split()
        coordinates.append((float(values[0]), float(values[1])))
    print(distance, n)
    print(coordinates)
    output = [[0, 2], [1, 3], [4]]
    print(output)


if __name__ == '__main__':
    # int_array_split_whitespace()
    # int_array_split_newline_1()
    # int_array_split_newline_2()
    multi_lines_multi_value()
