"""
牛客网上面大部分题都不是像leetcode那样将解答写在Solution类的实例方法上
而是 从stdin读取测试用例，再通过stdout输出返回值
"""


def int_array_split_whitespace():
    """
    [2019 PayPal实习生招聘编程卷 - [编程题]飞机最低可俯冲高度](https://www.nowcoder.com/test/16723511/summary)
    输入样例:
    1 1000
    """
    # split()方法默认会以空格作为分隔符
    nums = [int(num) for num in input().split()]
    print(nums)


def int_array_split_newline():
    """
    [牛客网-在线编程-连续子数组最大和](https://www.nowcoder.com/practice/03d341fb6c9d42debcdd38d82a0a545c)
    提示: 在IDEA的运行窗口，要通过cmd+D发送EOF，因为Ctrl+D是Debug的快捷键。在Terminal上Ctrl+D就能发送EOF了
    输入样例:
    1
    2
    3
    """
    import fileinput
    nums = [int(line) for line in fileinput.input()]
    print(nums)
    pass


if __name__ == '__main__':
    # int_array_split_whitespace()
    int_array_split_newline()
